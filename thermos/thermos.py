from flask import Flask,render_template,url_for,request,redirect
from User import User
from datetime import  datetime
from logging import DEBUG
app=Flask(__name__)

bookmark=[]

def store_bookmark(url):
    bookmark.append(dict(url=url,user="John",date = datetime.utcnow()))



@app.route('/')
@app.route('/index')
def index():
    user = User("jan", "kowalski")
    return render_template('index.html',Title="Title passed",user=user,Text=["asd","bcd","123"])

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmark(url)
        app.logger.debug('stored url %s' % url)
        return  redirect(url_for('index'))
    return render_template('add.html',Text="1232")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500

if __name__== "__main__":
    app.run(debug=True)
    app.logger.setLevel(DEBUG)

