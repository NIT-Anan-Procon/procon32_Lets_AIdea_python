import sys
import time

from flask import Flask, jsonify, request  # flaskを使って実装

sys.path.append("../")
from catr import predict
from url_image.url_image import image

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # jsonの文字化け防止


@app.route("/test", methods=["POST"])
def ngword():
    url = request.json["url"]
    subject = request.json["subject"]
    synonym = request.json["synonym"]
    image_name = image(url)
    time.sleep(1)
    return jsonify(predict.pre(subject, synonym, image_name))


if __name__ == "__main__":
    app.run(port=5000, debug="True", threaded=True)
