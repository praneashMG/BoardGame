import glob
import re

replacements = [
    # Desktop
    (r'<a href="#" class="nav-link">Products</a>', r'<a href="products.html" class="nav-link">Products</a>'),
    (r'<a href="#" class="nav-link">Picks</a>', r'<a href="picks.html" class="nav-link">Picks</a>'),
    (r'<a href="#" class="nav-link">New Arrivals</a>', r'<a href="newarivals.html" class="nav-link">New Arrivals</a>'),
    (r'<a href="#" class="nav-link">Game Nights</a>', r'<a href="gamenights.html" class="nav-link">Game Nights</a>'),
    
    # Mobile
    (r'<a href="#" class="py-2 font-medium">Products</a>', r'<a href="products.html" class="py-2 font-medium">Products</a>'),
    (r'<a href="#" class="py-2 font-medium">Picks</a>', r'<a href="picks.html" class="py-2 font-medium">Picks</a>'),
    (r'<a href="#" class="py-2 font-medium">New Arrivals</a>', r'<a href="newarivals.html" class="py-2 font-medium">New Arrivals</a>'),
    (r'<a href="#" class="py-2 font-medium">Game Nights</a>', r'<a href="gamenights.html" class="py-2 font-medium">Game Nights</a>')
]

count = 0
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    original = content
    for old, new in replacements:
        content = content.replace(old, new)
        
    if content != original:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
        count += 1
print(f"Total updated: {count}")
