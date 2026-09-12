import os
import glob

html_files = glob.glob('*.html')
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if '::-webkit-calendar-picker-indicator' not in content:
        target = "html[data-theme='dark'] {"
        replacement = """html[data-theme='dark'] input[type="date"]::-webkit-calendar-picker-indicator {
            filter: invert(1) brightness(100%);
        }

        html[data-theme='dark'] {"""
        new_content = content.replace(target, replacement, 1)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
