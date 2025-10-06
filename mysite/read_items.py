import chardet

with open("items.json", "rb") as f:
    rawdata = f.read()

result = chardet.detect(rawdata)
print(f"Encoding: {result['encoding']}, Confidence: {result['confidence']}")

print(rawdata[:20])  # print first 20 bytes


import json

with open("items.json", "r", encoding="utf-16") as f:
    data = json.load(f)

print(data)

# convert_utf16_to_utf8.py
input_file = "items.json"
output_file = "items_utf8.json"

with open(input_file, "r", encoding="utf-16") as f:
    data = f.read()

with open(output_file, "w", encoding="utf-8") as f:
    f.write(data)

print(f"File converted and saved as {output_file}")
