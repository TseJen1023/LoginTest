#Back-end:
#v1. Gets requests from front-end and verify if the credentials match.
#v2. Response match or not to front-end.
#v3. Write it with python and flask framework.
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if login_check(request.form['username'] , request.form['password']):
            return redirect(url_for('right', username=request.form.get('username')))
        else:
            return redirect(url_for('error', username=request.form.get('password')))
    return render_template('login.html')

def login_check(username, password):
    if username == 'aaaa' and password == 'aaaa':
        return True
    else:
        return False

@app.route('/right/<username>')
def right(username):
    return render_template('right.html', username=username)

@app.route('/error/<username>')
def error(username):
    return render_template('error.html', username=username)

if __name__ == '__main__':
    app.debug = True
    app.secret_key = "Your Key"
    app.run()
