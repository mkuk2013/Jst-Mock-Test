import json
import re
import os

# Load new questions
with open('/tmp/questions.json', 'r', encoding='utf-8') as f:
    new_questions = json.load(f)

# Read quiz 9
with open('jst-quiz9.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update title
content = content.replace("<title>IBA STS Junior Science Teacher Mock Test 9</title>", "<title>IBA STS Junior Science Teacher Mock Test 10</title>")
content = content.replace("IBA STS Mock Test 9 Completed", "IBA STS Mock Test 10 Completed") # For results section
content = content.replace("Mock Test 9 Completed!", "Mock Test 10 Completed!")
content = content.replace("IBA STS JST Mock Test 9</h1>", "IBA STS JST Mock Test 10</h1>")

# Remove passage text content (keep variable)
content = re.sub(r'const passageText = `.*?`;', 'const passageText = ``;', content, flags=re.DOTALL)

# Replace questions array
qs_json = json.dumps(new_questions, indent=4, ensure_ascii=False)
content = re.sub(r'const questions = \[.*?\];', f'const questions = {qs_json};', content, flags=re.DOTALL)

# Save as quiz 10
with open('jst-quiz10.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Created jst-quiz10.html")
