from flask import Flask,render_template,url_for
from User import User

app=Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = User("jan", "kowalski")
    return render_template('index.html',Title="Title passed",user=user,Text=["asd","bcd","123"])

@app.route('/add')
def add():
    return render_template('add.html',Text="1232")


if __name__== "__main__":
    app.run(debug=True)

