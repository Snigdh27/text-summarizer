from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from pymongo import MongoClient
from text_summary import summarizer


app = Flask(__name__)
client = MongoClient('localhost', 27017)

db = client.text_sum
sgnup = db.credentials



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

@app.route('/signup', methods=('GET', 'POST'))
def signup():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['passwd']
        mob=request.form['mob']
        # print(name,email,pwd,mob)
        sgnup.insert_one({'name':name, 'email':email, 'password':pwd,'mobile':mob})
        session['username']
    return render_template("index.html")

@app.route('/signin', methods=('GET', 'POST'))
def signin():
    if request.method=='POST':
        email = request.form['email']
        pwd = request.form['pass']
        # print(email,pwd)
        userdata = sgnup.find({'email':email})
        us=[user for user in userdata]
        if(us[0]['password']==pwd):
            return render_template("index.html")
        else:
            # print('invalid credentials')
            return render_template("login.html")
    return render_template("cover.html")

@app.route('/analyze',methods=['GET','POST'])
def analyze():
    if request.method=='POST':
        rawtext=request.form['name']
        summary,original_txt,len_orig_txt,len_summary=summarizer(rawtext)

    return render_template('index.html',summary=summary,original_txt=original_txt,len_orig_txt=len_orig_txt,len_summary=len_summary)

@app.route('/profile')
def Profile():
    return render_template('profile.html')

if __name__ == "__main__":
    app.run()
