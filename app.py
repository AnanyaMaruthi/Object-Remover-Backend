from flask import Flask
import argparse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, help='Server Port Number, default=4000')
    args = parser.parse_args()

    port = args.port if args.port is not None else 4000
    
    app.run(port=port, debug=True)