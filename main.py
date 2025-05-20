import os
from flask import Flask, render_template, url_for, make_response

app = Flask(__name__)

@app.route('/')
def index():
    made_used = os.listdir(r'static/img/made-used')
    print(made_used)
    return render_template('index.html', made_used=made_used)

if __name__ == '__main__':
    app.run(debug=True)