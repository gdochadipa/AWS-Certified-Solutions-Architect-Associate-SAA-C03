#!/usr/bin/env python3
"""Fix diagram rendering issues in DIAGRAMS.md files."""
import re
import os

def fix_diagram_rendering(filepath):
    """Fix common diagram rendering errors."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Fix 1: Replace &lt;&lt;&lt;BR_SLASH&gt;&gt;&gt; with <br/>
    content = content.replace('&lt;&lt;&lt;BR_SLASH&gt;&gt;&gt;', '<br/>')

    # Fix 2: Fix malformed node brackets - [" at end of line should be "]
    # Match patterns like: Node["text"[ or Node["text with<br/>breaks"[
    content = re.sub(r'\["([^"]*)"(\[)(?=\s*$|(?:\n))', r'["\1"]', content, flags=re.MULTILINE)

    # Fix 3: Fix node definitions with trailing [
    # Pattern: text[ at end of line or before arrow/newline
    content = re.sub(r'(\w+)\["([^"]+)"(\[)(?=\s|$|\n|-->|->|\||\.)', r'\1["\2"]', content)

    # Fix 4: Fix standalone nodes with trailing [
    # Pattern: word[ followed by whitespace or newline (not part of subgraph)
    lines = content.split('\n')
    fixed_lines = []
    for line in lines:
        # Skip subgraph lines
        if 'subgraph' in line.lower():
            fixed_lines.append(line)
            continue

        # Fix pattern: Word[ at end or before connection/newline
        # But not inside brackets like ["text["]
        if re.search(r'\w+\[(?!\[|")(?=\s*$|\s+-->|\s+->|\s*\n)', line):
            line = re.sub(r'(\w+)\[(?=\s*$|\s+-->|\s+->)', r'\1]', line)

        fixed_lines.append(line)

    content = '\n'.join(fixed_lines)

    # Fix 5: Fix mindmap syntax - (( at start should be paired with ))
    # Pattern: root((Text() should be root((Text))
    content = re.sub(r'\(\(([^)]+)\(\)(?!\))', r'((\1))', content)

    # Fix 6: Fix decision node syntax - "{ should be {"
    # Pattern: node"{ should be node{" and "{ should be "{
    content = re.sub(r'(\w+)"(\{)', r'\1\2"', content)
    content = re.sub(r'"(\{[^}]+)\{(?=\s|$)', r'\1{"', content)

    # Fix 7: Fix curly brace decision nodes - text{ should be text}
    # Pattern: {Text{ should be {Text}
    content = re.sub(r'\{([^}]+)\{(?=\s|$|\n)', r'{\1}', content)

    # Fix 8: Fix parentheses in regular nodes - (Text([ should be (Text)]
    content = re.sub(r'\(([^)]+)\(\["([^"]+)"\[', r'(["\2"]', content)
    content = re.sub(r'\(([^)]+)\(\[(?!\[)', r'([\1]', content)

    # Fix 9: Fix malformed subgraph endings with Group[ instead of Group"]
    content = re.sub(r'subgraph\s+(\w+_Group)\["([^"]+)"(\[)', r'subgraph \1["\2"]', content)

    # Fix 10: Fix sequence diagram syntax - (( at end should be ()
    # Pattern: text( at end of line in sequence diagrams
    content = re.sub(r'([A-Za-z0-9\s]+)\(\((?=\s*$)', r'\1()', content, flags=re.MULTILINE)

    # Fix 11: Additional bracket fixes for specific patterns
    # Pattern: Node[Text[ should be Node[Text]
    content = re.sub(r'(\w+)\[([^\]"]+)\[(?=\s*$|\s*\n)', r'\1[\2]', content, flags=re.MULTILINE)

    # Fix 12: Fix "(""[" patterns to proper node syntax
    content = re.sub(r'\(""(\w+)\[', r'(["\1"]', content)

    # Fix 13: Fix state diagram [*[ should be [*]
    content = re.sub(r'\[\*\[', r'[*]', content)

    # Fix 14: Fix node definitions where closing bracket is [
    # Pattern: S3["text[ should be S3["text"]
    content = re.sub(r'(\w+)\["([^"]+)"\[', r'\1["\2"]', content)

    # Fix 15: Fix nodes like IA[text[ to IA[text]
    content = re.sub(r'(\w+)\[([^\]"]+)\[', r'\1[\2]', content)

    # Fix 16: Fix decision nodes with malformed braces
    # Pattern: node{"text"{ should be node{"text"}
    content = re.sub(r'(\w+)\{"([^"]+)"\{', r'\1{"\2"}', content)

    # Fix 17: Fix parentheses nodes like (text([ to (text)]
    content = re.sub(r'\(([^)]+)\(\["', r'(["', content)
    content = re.sub(r'\(([^)]+)\(\[(?=[^a-zA-Z])', r'([\1]', content)

    # Fix 18: Fix sequence diagram parentheses (( to ()
    lines = content.split('\n')
    fixed_lines = []
    in_sequence = False
    for line in lines:
        if 'sequenceDiagram' in line:
            in_sequence = True
        elif line.strip().startswith('```'):
            in_sequence = False

        if in_sequence:
            # Fix (( at end of line to ()
            line = re.sub(r'\(\((?=\s*$)', '()', line)

        fixed_lines.append(line)
    content = '\n'.join(fixed_lines)

    # Fix 19: Fix double-quote node definitions like Node[""text"[
    content = re.sub(r'(\w+)\[""([^"]+)"\[', r'\1["\2"]', content)

    # Fix 20: Fix standalone (( and ()) patterns in mindmap
    content = re.sub(r'\(\(([^)]+)\(\)\)', r'((\1))', content)

    # Check if changes were made
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Fixed: {filepath}")
        return True
    else:
        print(f"ℹ️  No changes needed: {filepath}")
        return False

def main():
    """Fix diagram rendering issues in folders 03-13."""
    # Change to repository root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    os.chdir(repo_root)

    # Target folders 03-13
    folders = [f"{i:02d}-*" for i in range(3, 14)]

    diagram_files = []
    for folder_pattern in folders:
        import glob
        matches = glob.glob(f"{folder_pattern}/DIAGRAMS.md")
        diagram_files.extend(matches)

    diagram_files.sort()

    print(f"Found {len(diagram_files)} DIAGRAMS.md files to process\n")

    fixed_count = 0
    for filepath in diagram_files:
        if fix_diagram_rendering(filepath):
            fixed_count += 1

    print(f"\n{'='*60}")
    print(f"Summary: Fixed {fixed_count} out of {len(diagram_files)} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()

