from flask import *
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    with open("manga.json", "r") as f:
        return f.read()


@app.route("/manga/", methods=["GET"])
def mangaRequest():
    manga_query = int(request.args.get("manga"))

    with open("manga.json", "r") as f:
        data = json.load(f)
        json_dump = json.dumps(data[manga_query])
        return json_dump


if __name__ == "__main__":
    app.run(port=7777)
