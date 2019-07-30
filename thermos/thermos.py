from flask import Flask,render_template
from User import User

app=Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = User("jan", "kowalski")
    return render_template('index.html',Title="Title passed",user=user,Text=["asd","bcd","123"])

if __name__== "__main__":
    app.run(debug=True)

