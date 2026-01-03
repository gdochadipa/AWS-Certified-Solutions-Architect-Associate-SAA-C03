#!/usr/bin/env python3
"""Fix common Mermaid diagram errors."""
import re
import glob

def fix_mermaid_diagrams(filepath):
    """Fix common Mermaid diagram errors."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Fix 1: Convert quoted subgraph names to ID-based syntax
    # Only fix lines that match exactly: whitespace + subgraph + space + "Label"
    def fix_subgraph_line(match):
        indent = match.group(1)
        label = match.group(2)
        # Create ID from label (remove spaces, special chars)
        id_name = re.sub(r'[^a-zA-Z0-9]', '_', label)
        id_name = re.sub(r'_+', '_', id_name).strip('_')
        if not id_name:
            id_name = "Group"
        if not id_name.endswith("_Group"):
            id_name = id_name + "_Group"
        return f'{indent}subgraph {id_name}["{label}"]'

    # Apply line by line to avoid breaking other content
    lines = content.split('\n')
    fixed_lines = []
    for line in lines:
        # Only match subgraph lines with quoted labels
        if re.match(r'^(\s*)subgraph\s+"[^"]+"(\s*)$', line):
            fixed_line = re.sub(r'^(\s*)subgraph\s+"([^"]+)"(\s*)$', fix_subgraph_line, line)
            fixed_lines.append(fixed_line)
        else:
            fixed_lines.append(line)
    content = '\n'.join(fixed_lines)

    # Fix 2: Replace < and > with &lt; and &gt; in node text (except for arrows and <br/>)
    # Only fix within node definitions like Node["text < 10"]
    def fix_html_in_nodes(match):
        node_id = match.group(1)
        node_text = match.group(2)

        # Skip if already escaped
        if '&lt;' in node_text or '&gt;' in node_text:
            return match.group(0)

        # Preserve <br/> and <br> tags with unique placeholders
        protected_text = node_text.replace('<br/>', '___PLACEHOLDER_BR_SLASH___')
        protected_text = protected_text.replace('<br>', '___PLACEHOLDER_BR___')

        # Replace unescaped < and >
        protected_text = protected_text.replace('<', '&lt;')
        protected_text = protected_text.replace('>', '&gt;')

        # Restore <br> tags
        protected_text = protected_text.replace('___PLACEHOLDER_BR_SLASH___', '<br/>')
        protected_text = protected_text.replace('___PLACEHOLDER_BR___', '<br>')

        return f'{node_id}["{protected_text}"]'

    # Apply to quoted node text: Node["text with < or >"]
    content = re.sub(r'(\w+)\["([^"]*[<>][^"]*)"\]', fix_html_in_nodes, content)


    # Fix 3: Remove style statements from sequence diagrams
    def remove_styles_from_sequence(match):
        diagram_content = match.group(0)
        # Remove style statements from sequence diagrams
        diagram_content = re.sub(r'\n    style \w+ fill:#[A-F0-9]+', '', diagram_content)
        diagram_content = re.sub(r'\n    classDef \w+ fill:#[A-F0-9]+', '', diagram_content)
        diagram_content = re.sub(r'\n    class \w+ \w+', '', diagram_content)
        return diagram_content

    content = re.sub(
        r'```mermaid\nsequenceDiagram.*?```',
        remove_styles_from_sequence,
        content,
        flags=re.DOTALL
    )

    # Fix 4: Convert style statements to classDef in non-sequence diagrams
    # Match single style statements and convert them
    def fix_style_statements(match):
        full_match = match.group(0)
        # Skip if inside sequenceDiagram
        if 'sequenceDiagram' in full_match:
            return full_match

        # Replace individual style statements
        lines = full_match.split('\n')
        new_lines = []
        style_map = {}

        for line in lines:
            style_match = re.match(r'^(\s+)style (\w+) fill:(#[A-F0-9]+)$', line)
            if style_match:
                indent = style_match.group(1)
                node = style_match.group(2)
                color = style_match.group(3)
                class_name = f"{node.lower()}Style"

                # Track styles to apply
                if color not in style_map:
                    style_map[color] = []
                style_map[color].append((node, class_name))
            else:
                new_lines.append(line)

        # Add classDef and class statements at the end (before closing ```)
        if style_map:
            # Find the closing ``` and insert before it
            closing_idx = len(new_lines) - 1
            while closing_idx >= 0 and not new_lines[closing_idx].startswith('```'):
                closing_idx -= 1

            indent = '    '
            insert_lines = []
            counter = 0
            for color, nodes in style_map.items():
                for node, class_name in nodes:
                    counter += 1
                    unique_class = f"style{counter}"
                    insert_lines.append(f"{indent}classDef {unique_class} fill:{color}")
                    insert_lines.append(f"{indent}class {node} {unique_class}")

            if closing_idx >= 0:
                new_lines = new_lines[:closing_idx] + insert_lines + new_lines[closing_idx:]
            else:
                new_lines.extend(insert_lines)

        return '\n'.join(new_lines)

    content = re.sub(
        r'```mermaid.*?```',
        fix_style_statements,
        content,
        flags=re.DOTALL
    )

    # Fix 5: Quote nodes with special characters (emojis, bullets, etc.)
    # This regex finds node definitions and wraps content in quotes if it contains special chars
    special_chars = r'[⚠️💰⚡📊🛡️✅❌🔑🔒📦💾📁🪟📏🎯🔐🔋📡☁️💪🔄•→@/]'

    # Fix regular nodes: Node[text...]
    def quote_node_if_needed(match):
        prefix = match.group(1)
        content = match.group(2)
        suffix = match.group(3)

        # Skip if already quoted
        if content.startswith('"') and content.endswith('"'):
            return match.group(0)

        # Quote if contains special characters
        if re.search(special_chars, content):
            return f'{prefix}["{content}"]{suffix}'

        return match.group(0)

    # Match: word[content] or word([content])
    content = re.sub(
        r'(\w+)\[([^\]]+)\](\s|$|-->|->|\||,)',
        quote_node_if_needed,
        content
    )

    content = re.sub(
        r'(\w+)\(\[([^\]]+)\]\)(\s|$|-->|->|\||,)',
        lambda m: f'{m.group(1)}(["{m.group(2)}"]){m.group(3)}' if re.search(special_chars, m.group(2)) and not (m.group(2).startswith('"') and m.group(2).endswith('"')) else m.group(0),
        content
    )

    # Fix decision nodes {text}
    content = re.sub(
        r'(\w+)\{([^\}]+)\}(\s|$|-->|->|\||,)',
        lambda m: f'{m.group(1)}{{"{m.group(2)}"}}{m.group(3)}' if re.search(special_chars, m.group(2)) and not (m.group(2).startswith('"') and m.group(2).endswith('"')) else m.group(0),
        content
    )

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {filepath}")
        return True
    else:
        print(f"No changes: {filepath}")
        return False

# Change to repository root directory (parent of scripts/)
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
os.chdir(repo_root)

# Find all DIAGRAMS.md files
diagram_files = glob.glob('**/DIAGRAMS.md', recursive=True)

fixed_count = 0
for filepath in sorted(diagram_files):
    if fix_mermaid_diagrams(filepath):
        fixed_count += 1

print(f"\nTotal files fixed: {fixed_count}/{len(diagram_files)}")

