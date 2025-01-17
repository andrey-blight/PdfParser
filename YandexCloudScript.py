import base64
import requests
import json
import pprint


# encode pdf to base64
def encode_file(file_path):
    with open(file_path, "rb") as fid:
        file_content = fid.read()
    return base64.b64encode(file_content).decode("utf-8")


# config const
iam = None
catalog_id = None

content = encode_file("done/Погосян_Семантика_триумфа_в_птеровскую_эпоху.PDF")

data = {"mimeType": "application/pdf",
        "languageCodes": ["*"],
        "content": content}

url = "https://ocr.api.cloud.yandex.net/ocr/v1/recognizeTextAsync"
headers = {"Content-Type": "application/json",
           "Authorization": "Bearer {:s}".format(iam),
           "x-folder-id": catalog_id,
           "x-data-logging-enabled": "true"}

# resp = requests.post(url=url, headers=headers, data=json.dumps(data))
# resp_id = resp.json()["id"]
# pprint.pprint(resp.json())

req_url = f"https://ocr.api.cloud.yandex.net/ocr/v1/getRecognition?operationId=cfrenq7pqnicvcjrp5km"
pdf_resp = requests.get(url=req_url, headers=headers)
print(pdf_resp.text)
pdf_text_json = json.loads(pdf_resp.text)
pprint.pprint(pdf_text_json)

with open('save.json', 'w') as outfile:
    json.dump(pdf_text_json, outfile)
