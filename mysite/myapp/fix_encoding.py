import chardet
import json

input_file = "items.json"

# Step 1: Read raw bytes
with open(input_file, "rb") as f:
    raw_data = f.read()

# Step 2: Detect encoding
detection = chardet.detect(raw_data)
encoding = detection['encoding']
confidence = detection['confidence']
print(f"Detected encoding: {encoding} (Confidence: {confidence})")

if encoding is None:
    raise Exception("Encoding could not be detected")

# Step 3: Decode bytes to string safely
try:
    text = raw_data.decode(encoding)
except Exception as e:
    print(f"Decoding error: {e}")
    # As fallback try utf-8 ignoring errors
    text = raw_data.decode('utf-8', errors='ignore')
    print("Decoded using utf-8 with ignoring errors")

# Step 4: Try loading JSON
try:
    data = json.loads(text)
    print("JSON loaded successfully")
except Exception as e:
    print(f"JSON load error: {e}")

# Optionally write cleaned JSON to file
with open("items_fixed.json", "w", encoding="utf-8") as f:
    f.write(text)
