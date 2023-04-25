import pyrebase
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for

app = Flask(__name__)

config = {
  "apiKey": "AIzaSyDVWZjhGeHUpxc08PKN3LvLj2a3B9anDMA",
  "authDomain": "minorproject2-c0d61.firebaseapp.com",
  "projectId": "minorproject2-c0d61",
  "storageBucket": "minorproject2-c0d61.appspot.com",
  "messagingSenderId": "277081147302",
  "appId": "1:277081147302:web:8855962fdcb87a3843b167",
  "measurementId": "G-XQWSPMD8TQ",
  "databaseURL": "https://minorproject2-c0d61-default-rtdb.firebaseio.com/"
}

firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
db=firebase.database()

person={"is_logged_in":False,"name":"","email":"","uid":""}

@app.route('/')
def Home():
    return render_template('cover.html')

@app.route('/login')
def Login():
    return render_template('login.html')

@app.route('/home')
def Index():
    if person["is_logged_in"]==False:
        return render_template("index.html")
    else:
        return redirect(url_for('Login'))



@app.route('/profile')
def Profile():
    return render_template('profile.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
