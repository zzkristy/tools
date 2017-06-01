from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/password', methods=['GET'])
def PwdIndexView():
    return render_template('password.html')


@app.route('/password', methods=['POST'])
def PwdGenView():
    orig_key = request.form['origin']
    salt = request.form['salt']
    content = {
        'origin': orig_key,
        'salt': salt,
        'pwd': '123456'
    }
    return render_template('password.html', **content)


if __name__ == '__main__':
    app.run()
