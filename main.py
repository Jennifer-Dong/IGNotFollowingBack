'''
import re

with open('followers.html') as file:
    for line in file:
        urls = re.findall('https?://\S+)', line)
        print(urls)

'''

f=open('followers.html', 'r')
print(f.read(5))