import re

def update_file(filename, title_replace, subtitle_replace):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update title
    content = re.sub(
        r'<title>.*?\| GameNest.*?</title>',
        f'<title>{title_replace}</title>',
        content,
        flags=re.IGNORECASE
    )
    
    # Update subtitle (usually under h1)
    content = re.sub(
        r'(<p class="text-secondary mt-1 text-xs">)(.*?)(</p>)',
        rf'\g<1>{subtitle_replace}\g<3>',
        content,
        flags=re.IGNORECASE
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

update_file('login.html', 'Sign In | GameNest - Hobby & Board Games Store', 'Sign in to track your orders, manage your wishlist & connect with the community')
update_file('signup.html', 'Sign Up | GameNest - Hobby & Board Games Store', 'Create a profile & join GameNest to discover your next favorite board game')

