import os
import re

# Count practice questions
modules = [
    "01-AWS-Fundamentals",
    "02-IAM",
    "03-Compute",
    "04-Storage",
    "05-Database",
    "06-Networking",
    "07-Security",
    "08-Application-Integration",
    "09-Monitoring",
    "10-Migration",
    "11-Analytics",
    "12-Architecture-Patterns",
    "13-Cost-Optimization",
]

print("=== PRACTICE QUESTIONS COUNT ===")
total_questions = 0
for module in modules:
    file_path = f"{module}/PRACTICE-QUESTIONS.md"
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            count = len(re.findall(r'^### Question \d+', content, re.MULTILINE))
            print(f"{module}: {count} questions")
            total_questions += count

print(f"\n✅ Total Practice Questions: {total_questions}")

# Count diagrams
print("\n=== DIAGRAMS COUNT ===")
total_diagrams = 0
for module in modules:
    file_path = f"{module}/DIAGRAMS.md"
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            count = content.count('```mermaid')
            print(f"{module}: {count} diagrams")
            total_diagrams += count

print(f"\n✅ Total Diagrams: {total_diagrams}")

# Count ULTRA-FAST-LEARN files
print("\n=== ULTRA-FAST-LEARN FILES ===")
ultra_fast_count = 0
for module in modules:
    file_path = f"{module}/ULTRA-FAST-LEARN.md"
    if os.path.exists(file_path):
        ultra_fast_count += 1
        print(f"✓ {module}")

print(f"\n✅ Total ULTRA-FAST-LEARN files: {ultra_fast_count}")

# Count FAST-LEARN files
print("\n=== FAST-LEARN FILES ===")
fast_learn_count = 0
for module in modules:
    file_path = f"{module}/FAST-LEARN.md"
    if os.path.exists(file_path):
        fast_learn_count += 1
        print(f"✓ {module}")

print(f"\n✅ Total FAST-LEARN files: {fast_learn_count}")

# Count README files (comprehensive)
print("\n=== COMPREHENSIVE README FILES ===")
readme_count = 0
for module in modules:
    file_path = f"{module}/README.md"
    if os.path.exists(file_path):
        readme_count += 1

print(f"✅ Total README files: {readme_count}")

print("\n" + "="*50)
print("SUMMARY FOR README UPDATE")
print("="*50)
print(f"✅ {len(modules)} comprehensive modules covering all SAA-C03 exam domains")
print(f"✅ 3 learning speeds: Ultra-Fast (3-4 hrs), Fast (11-14 hrs), Comprehensive (40-60 hrs)")
print(f"✅ {total_diagrams}+ interactive diagrams with Mermaid visualizations")
print(f"✅ Ultra-condensed bullet points for extreme fast learning")
print(f"✅ Multiple quick learning guides with mnemonics and visual aids")
print(f"✅ {total_questions}+ practice questions with detailed explanations")
print(f"✅ 40+ hands-on labs suggestions")
print(f"✅ Complete exam coverage for SAA-C03")

