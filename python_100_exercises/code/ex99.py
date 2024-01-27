from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def ex99():
    return render_template('my-form.html')


@app.route('/', methods=['POST'])
def form_post():
    text = request.form['text']
    with open("flask_output.txt", "a") as file:
        file.write(f"{text}\n")
        return ex99()

