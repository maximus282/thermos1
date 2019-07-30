from flask import Flask,render_template,url_for

app=Flask(__name__)


@app.route('/123')

@app.route('/index')
def index():
    render_template('templates/index.html')
    print("test")

if __name__== "__main__":
    app.run()

