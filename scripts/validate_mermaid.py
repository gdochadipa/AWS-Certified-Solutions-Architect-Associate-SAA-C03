#!/usr/bin/env python3
"""Validate Mermaid diagrams for common syntax issues."""

import re
import glob
import sys

def validate_mermaid_file(filepath):
    """Check a file for common Mermaid syntax issues."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    issues = []
    lines = content.split('\n')
    in_mermaid = False
    in_sequence = False
    diagram_start = 0
    current_diagram = []
    diagram_line_start = 0

    for i, line in enumerate(lines, 1):
        if '```mermaid' in line:
            in_mermaid = True
            diagram_start = i
            in_sequence = False
            current_diagram = []
            diagram_line_start = i
        elif '```' in line and in_mermaid:
            # Validate the complete diagram before closing
            diagram_issues = validate_diagram_structure('\n'.join(current_diagram), diagram_line_start)
            issues.extend(diagram_issues)

            in_mermaid = False
            in_sequence = False
            current_diagram = []
        elif in_mermaid:
            current_diagram.append(line)

            # Check if it's a sequence diagram
            if 'sequenceDiagram' in line:
                in_sequence = True

            # Check for old-style syntax (should use classDef)
            if re.match(r'^\s+style \w+ fill:#', line):
                if in_sequence:
                    issues.append(f"Line {i}: Sequence diagrams don't support style statements")
                else:
                    issues.append(f"Line {i}: Use 'classDef' instead of 'style' syntax")

            # Check for quoted subgraph names (old syntax)
            if re.match(r'^\s+subgraph\s+"[^"]+"', line):
                issues.append(f"Line {i}: Use ID-based subgraph syntax: subgraph ID[\"Label\"] instead of subgraph \"Label\"")

            # Check for unescaped comparison operators (< >) in node text
            # Match nodes with [...] that contain < or > but not &lt; &gt; or <br/>
            if '[' in line and ']' in line:
                # Extract text between [ and ]
                node_text_match = re.search(r'\[([^\]]+)\]', line)
                if node_text_match:
                    node_text = node_text_match.group(1)
                    # Remove <br/> and <br> tags first to avoid false positives
                    cleaned_text = node_text.replace('<br/>', '').replace('<br>', '')
                    # Check if remaining text contains unescaped < or >
                    if re.search(r'[<>]', cleaned_text) and not re.search(r'&lt;|&gt;', cleaned_text):
                        # Make sure the line itself is not a connection line (check outside the brackets)
                        line_outside_brackets = re.sub(r'\[[^\]]+\]', '', line)
                        if not re.search(r'^\s*\w+.*(?:-->|<--|===|\.\.>|---)', line_outside_brackets):
                            issues.append(f"Line {i}: Use &lt; and &gt; for comparison operators in node text")


            # Check for unquoted nodes with special characters
            special_chars = r'[⚠️💰⚡📊🛡️✅❌🔑🔒📦💾📁🪟📏🎯🔐🔋📡☁️💪🔄•→@]'
            if re.search(r'\w+\[[^\]"]*' + special_chars, line):
                # Make sure it's properly quoted
                if not re.search(r'\w+\["[^\]]*"\]', line):
                    issues.append(f"Line {i}: Node with special character should be quoted: {line.strip()[:60]}")

            # Check for mismatched quotes
            if line.count('"') % 2 != 0 and '--' not in line:
                issues.append(f"Line {i}: Mismatched quotes: {line.strip()[:60]}")

            # Check classDef/class indentation
            if line.startswith('classDef ') or line.startswith('class '):
                if not line.startswith('    '):
                    issues.append(f"Line {i}: classDef/class should be indented with 4 spaces")

    return issues

def validate_diagram_structure(diagram_text, start_line):
    """Validate overall diagram structure for floating nodes and disconnected components."""
    issues = []

    # Skip empty diagrams
    if not diagram_text.strip():
        return issues

    # Extract subgraph IDs to exclude them from floating node detection
    subgraph_ids = set()
    for match in re.finditer(r'subgraph\s+(\w+)[\[\s]', diagram_text):
        subgraph_ids.add(match.group(1))

    # Extract all node definitions and connections
    nodes_defined = set()
    nodes_connected = set()

    # Find all node definitions (Node[...], Node(...), Node{...}, etc.)
    node_pattern = r'(\w+)[\[\(\{]'
    for match in re.finditer(node_pattern, diagram_text):
        node_id = match.group(1)
        # Skip keywords and subgraph IDs
        if node_id not in ['graph', 'subgraph', 'end', 'classDef', 'class', 'TB', 'LR', 'TD', 'RL'] and node_id not in subgraph_ids:
            nodes_defined.add(node_id)

    # Find all connections (A --> B, A -.-> B, A --- B, etc.)
    connection_pattern = r'(\w+)\s*(?:-->|\.->|-\.-?>|---|->|<--|<-\.|\|)'
    for match in re.finditer(connection_pattern, diagram_text):
        node_id = match.group(1)
        if node_id not in ['graph', 'subgraph', 'end', 'classDef', 'class'] and node_id not in subgraph_ids:
            nodes_connected.add(node_id)

    # Also find nodes on the right side of connections
    right_connection_pattern = r'(?:-->|\.->|-\.-?>|---|->|<--|<-\.)\s*(?:\|[^\|]+\|)?\s*(\w+)'
    for match in re.finditer(right_connection_pattern, diagram_text):
        node_id = match.group(1)
        if node_id not in ['graph', 'subgraph', 'end', 'classDef', 'class'] and node_id not in subgraph_ids:
            nodes_connected.add(node_id)

    # Check for floating nodes (defined but not connected)
    floating_nodes = nodes_defined - nodes_connected

    # Filter out common intentional floating nodes (Features, Decision, Notes, Summary)
    intentional_floating = {'Features', 'Decision', 'Notes', 'Summary', 'Legend', 'KeyFeatures'}
    floating_nodes = floating_nodes - intentional_floating

    # Warn if there are multiple floating nodes
    if len(floating_nodes) > 2:
        issues.append(f"Line {start_line}: Warning - {len(floating_nodes)} floating nodes detected (not connected): {', '.join(sorted(floating_nodes)[:5])}")

    return issues

def main():
    # Change to repository root directory (parent of scripts/)
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    os.chdir(repo_root)

    # Find all DIAGRAMS.md files
    diagram_files = sorted(glob.glob('**/DIAGRAMS.md', recursive=True))

    total_issues = 0
    files_with_issues = 0

    for filepath in diagram_files:
        issues = validate_mermaid_file(filepath)
        if issues:
            files_with_issues += 1
            total_issues += len(issues)
            print(f"\n❌ {filepath}:")
            for issue in issues[:5]:  # Show first 5 issues per file
                print(f"   {issue}")
            if len(issues) > 5:
                print(f"   ... and {len(issues) - 5} more issues")
        else:
            print(f"✅ {filepath}")

    print(f"\n{'='*60}")
    print(f"Summary: {len(diagram_files) - files_with_issues}/{len(diagram_files)} files passed validation")
    if total_issues > 0:
        print(f"Found {total_issues} issue(s) in {files_with_issues} file(s)")
        sys.exit(1)
    else:
        print("All files are valid! 🎉")
        sys.exit(0)

if __name__ == '__main__':
    main()

