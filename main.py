from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/teksts")
def te():
    return render_template("teksts.html")


@app.route("/saraksts")
def saraksts():
    saraksts = ["big", "Black", "Balls"]
    bildes = ["https://play-lh.googleusercontent.com/jnutN_x8MZeuK_N5qrq6KjUa8ecuaFisDY49VCB3tV4OrcqN0euqzIlGYIzsITo5dcZS", "https://blackdesign.world/app/uploads/2020/07/BLACK-icon.jpg", "https://d5wt70d4gnm1t.cloudfront.net/media/a-s/artworks/gardar-eide-einarsson/44155-176986968416/gardar-eide-einarsson-black-balls-800x800.jpg"]
    return render_template("saraksts.html", vardi = saraksts)


if __name__ == '__main__':
    app.run(port = 5000)
    
print("Hello world")