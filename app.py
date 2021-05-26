from flask import Flask, request, jsonify
import argparse
import base64
import cv2
import numpy as np
import io

app = Flask(__name__)


@app.route("/")
def home():
    return "Automatic Object Remover API"


@app.route("/inpaint", methods=["POST"])
def inpaint_image():
    try:
        object_label = request.form["object_label"]

        image = request.files["image"].read()
        npimg = np.fromstring(image, np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
        cv2.imwrite("images/sample.jpg", img)

        img = cv2.imread("images/sample.jpg")
        _, buffer = cv2.imencode(".jpg", img)
        image_string = base64.b64encode(buffer)

        response = jsonify({"image_string": str(image_string)})
        response.status_code = 200
        return response
    except:
        response = jsonify({"error": "Something went wrong"})
        response.status_code = 500
        return response


@app.after_request
def after_request(response):

    response.headers.add("Access-Control-Allow-Origin", "*")
    # response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    # response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE")
    return response


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, help="Server Port Number, default=4000")
    args = parser.parse_args()

    port = args.port if args.port is not None else 4000

    app.run(port=port, debug=True)
