from flask import Flask, request, jsonify
import argparse

app = Flask(__name__)

@app.route("/")
def home():
    return "Automatic Object Remover API"

@app.route("/inpaint", methods=["POST"])  
def inpaint_image():
    try:
        image = request.files["image"]
        object_label = request.form["object_label"]
        response = jsonify({})
        response.status_code = 200
        return response
    except:
        response = jsonify({"error": "Something went wrong"})
        response.status_code(400)
        return response


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, help='Server Port Number, default=4000')
    args = parser.parse_args()

    port = args.port if args.port is not None else 4000
    
    app.run(port=port, debug=True)