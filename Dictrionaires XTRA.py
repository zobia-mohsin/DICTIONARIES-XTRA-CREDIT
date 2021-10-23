keywords = ['Father', 'God', 'Christ', 'Spirit', 'life', 'man']
dict = {}

with open(r'C:\Users\zobia\Desktop\MIS 4322 01 Advanced Python\Advanced Python\DICTIONARIES HW\book of John text.txt', 'r') as f:
    text = f.read().split(' ')  # or f.read().split(',')

for word in text:
    dict[word] = dict[word]+1 if word in dict else 1

print([{x, dict[x]} for x in keywords])
