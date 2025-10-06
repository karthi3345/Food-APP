with open("items.json", "rb") as f:
    data = f.read()

with open("items_fixed.json", "w", encoding="utf-8") as f:
    f.write(data.decode("utf-8-sig"))
