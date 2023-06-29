from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    a = 4
    print("Hello!", a)
    return render_template('test-0.html')


if __name__ == "__main__":
    app.run(debug=True)
