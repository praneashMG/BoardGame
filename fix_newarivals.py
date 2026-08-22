content = open('newarivals.html', encoding='utf-8').read()

# Fix grid for "Back on the Shelves"
content = content.replace(
    'class="grid md:grid-cols-3 gap-6"',
    'class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"'
)

# Add flex-shrink-0 to images in "Back on the Shelves"
content = content.replace(
    'class="w-24 h-24 object-cover rounded-lg border border-border shadow-sm"',
    'class="w-24 h-24 object-cover rounded-lg border border-border shadow-sm flex-shrink-0"'
)

# Add flex-shrink-0 to the w-10 h-10 thumbnail container in the pre-order table
content = content.replace(
    'class="w-10 h-10 bg-gray-200 rounded object-cover overflow-hidden"',
    'class="w-10 h-10 bg-gray-200 rounded object-cover overflow-hidden flex-shrink-0"'
)

# Also fix the top section form which might not be responsive enough
# <form class="flex flex-col sm:flex-row justify-center gap-3 max-w-md mx-auto">
# That looks perfectly responsive actually.

with open('newarivals.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated newarivals.html')
