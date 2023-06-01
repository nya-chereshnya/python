
hui = {}
amount, gavno = map(int, input().split())
for i in range(amount):
    key, value = map(str, input().split(": "))
    hui[key] = value

compressed_text = str(input())

default_text = ''


huffman_codes = {value: key for key, value in hui.items()}

code = ''
while compressed_text:
    code += compressed_text[:1]
    compressed_text = compressed_text[1:]
    if code in huffman_codes:
        default_text += huffman_codes[code]
        code = ''

print(default_text)
