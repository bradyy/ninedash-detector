import argparse
import io

import torch
from flask import Flask, request
from PIL import Image
import json

app = Flask(__name__)

DETECTION_URL = "/v1/ninedash/detect"

@app.route(DETECTION_URL, methods=["POST"])
def predict():
    if request.method != "POST":
        return

    if request.files.get("image"):
        # Method 1
        # with request.files["image"] as f:
        #     im = Image.open(io.BytesIO(f.read()))

        # Method 2
        im_file = request.files["image"]
        im_bytes = im_file.read()
        im = Image.open(io.BytesIO(im_bytes))

        results = model(im, size=640)  # reduce size=320 for faster inference

        returned_response = {}

        if (len(results.pandas().xywh[0]) > 0):
            returned_response['have_ninedash'] = 1
            returned_response['locations'] = []

            for indx, rows in results.pandas().xywh[0].iterrows():
                returned_response['locations'].append({
                    'bbox': {
                        'x_center': rows[0],
                        'y_center': rows[1],
                        'width': rows[2],
                        'height': rows[3]
                    },
                    'score': rows[4]
                })
        
        else:
            returned_response['have_ninedash'] = 0

        print(returned_response)
            

        return json.dumps(returned_response)


parser = argparse.ArgumentParser(
description="Flask API exposing YOLOv5 model")
parser.add_argument("--port", default=5000, type=int, help="port number")
opt = parser.parse_args()

# Fix known issue urllib.error.HTTPError 403: rate limit exceeded https://github.com/ultralytics/yolov5/pull/7210
torch.hub._validate_not_a_forked_repo = lambda a, b, c: True

model = torch.hub.load("ultralytics/yolov5", "custom",
                        force_reload=True, path = '.weights/yolov5m.pt')  # force_reload to recache
# debug=True causes Restarting with stat
app.run(host="0.0.0.0", port=opt.port)
