import re
login = open('login.html', encoding='utf-8').read()
signup = open('signup.html', encoding='utf-8').read()

print('login Title:', re.findall(r'<title>.*?</title>', login))
print('login Subtitle:', re.findall(r'<p class="text-secondary mt-1 text-xs">.*?</p>', login))
print('signup Title:', re.findall(r'<title>.*?</title>', signup))
print('signup Subtitle:', re.findall(r'<p class="text-secondary mt-1 text-xs">.*?</p>', signup))
