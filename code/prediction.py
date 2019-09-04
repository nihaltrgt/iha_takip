import requests, os, sys
from PIL import Image , ImageDraw


model_id = "370ba5d1-e64d-4294-9822-a4c85412197c"
api_key = os.environ.get('NANONETS_API_KEY')
image_path = sys.argv[1]
IM_WIDTH=640
IM_HEIGHT=480

url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/' + model_id + '/LabelFile/'

data = {'file': open(image_path, 'rb'), 'modelId': ('', model_id)}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth(api_key, ''), files=data)
result=response.json()["result"][0]
TL_mainrect=(int(IM_WIDTH*0.25),int(IM_HEIGHT*0.10),[128,0,128])
BR_mainrect=(int(IM_WIDTH*0.75),int(IM_HEIGHT*0,90),[128,0,128])

im=Image.open(image_path)
draw=ImageDraw.Draw(im)
for b in result ["prediction"]:
    box=(b["xmin=32"],b["ymin=24"],b["xmax=320"],b["ymax=384"])
    draw.rectangle(box , fill=None , outline=[255,0,0])
im.show()
print(response.text)