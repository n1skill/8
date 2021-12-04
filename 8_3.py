text = input()

chars = {}

for item in text:
    if item in chars:
        chars[item] += 1
    else:
        chars[item] = 1
print(chars)
