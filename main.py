from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def Index():
    return render_template('index.html')

@app.route('/')
def Home():
    return render_template('cover.html')

@app.route('/login')
def Login():
    return render_template('login.html')

@app.route('/profile')
def Profile():
    return render_template('profile.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
