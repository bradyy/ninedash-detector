import os
from re import template
from flask import Flask, jsonify, redirect, request, render_template, make_response, send_from_directory
from PIL import Image
import os
import shutil
from api import APICheck
import sys


app = Flask(__name__, static_folder='static', template_folder='templates')
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSON_SORT_KEYS'] = False



@app.route("/")
def init():
    return render_template('./index.html')


@app.route('/test', methods=['GET', 'POST'])
def testfn():
    if 'file' not in request.files:
        print('no file')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        print('empty file name')
        return redirect(request.url)

    if file:
        file.save(os.path.join(
            app.config['UPLOAD_FOLDER'], f"upload.jpg"))

        result = APICheck()

        if (len(result) > 1):
            # Move file from result[1] to static folder
            shutil.move(result[1] + "/upload.jpg", os.path.join("./static/upload.jpg"))

        return make_response(jsonify([result[0]]), 200)

    return 'Sucesss', 200


