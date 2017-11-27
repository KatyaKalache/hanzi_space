 #!/usr/bin/python3
# starts a Flask web application
from flask import Flask, render_template, request
from dev import decompose
from dev import etymology
import re


decom = decompose.decom
ele = decompose.ele
etymol = etymology.etymol
character_print = decompose.character_print
app = Flask(__name__)

@app.route('/', strict_slashes=False, methods=['GET'])
def display():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def char():
    argument = request.form["character"]
    valid = re.findall(r'[\u4e00-\u9fff]+', argument)
    if len(argument) < 1:
        message_no_argument = "Please enter at least one character"
        return render_template('index.html',  **locals())
    if valid == []:
        message_not_valid = "Please enter a Chinese character"
        return render_template('index.html',  **locals())
    character = character_print(argument)
    word_associations = decom(argument)
    radicals = ele(argument)
    etymology = etymol(argument)

    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
