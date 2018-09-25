from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <!-- create your form here -->
        <form action="/" method="POST">
            <label>Rotate by:
                <input type="text" name="rot" value="0"/>
            </label>
            <textarea name="text">{encrypted_text}</textarea>
            <input type="submit" value="Submit Query"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format(encrypted_text="")

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    if rot.isdecimal():
        rot = int(rot)
    else:
        rot = 0
    
    text = request.form['text']

    return form.format(encrypted_text = rotate_string(text, rot))


app.run()