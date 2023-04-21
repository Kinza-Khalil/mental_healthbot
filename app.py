from sanic import Sanic, response
from sanic_cors import CORS

app = Sanic(__name__)
CORS(app)

@app.route("/")
async def index(request):
    with open("templates/index.html") as f:
        return response.html(f.read())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
