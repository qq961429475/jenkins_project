import re

text = 'a.my_function()'
match = re.search(r'\.(.*?)\(', text)
print(match)
print(match.group(1))
print(re.findall(r'\.(.*?)\(', text))
