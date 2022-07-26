from flask import *
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/", methods=["GET"])
@cross_origin()
def index():
    with open("manga.json", "r") as f:
        return f.read()


@app.route("/manga/", methods=["GET"])
@cross_origin()
def mangaRequest():
    manga_query = int(request.args.get("manga"))

    with open("manga.json", "r") as f:
        data = json.load(f)
        json_dump = json.dumps(data[manga_query])
        return json_dump


if __name__ == "__main__":
    app.run()
