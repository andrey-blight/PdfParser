import json

with open("test.json") as f:
    data = json.load(f)

res_data = ""
for page in data["pages"]:
    page_text = page["result"]["textAnnotation"]["fullText"] + "\n\n"
    res_data += page_text

with open("res/Погосян_Семантика_триумфа_в_птеровскую_эпоху.txt", "w") as f:
    f.write(res_data)
