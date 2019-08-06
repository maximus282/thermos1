from flask import Flask,render_template,url_for,request,redirect,flash
from User import User
from datetime import  datetime
from forms import BookmarkForm

app=Flask(__name__)

bookmarks=[]
app.config['SECRET_KEY']="b'D%\xf31\x82 \xed\xd4\x99i\x95\xed\xd6\x91\x82\x1cA#\xe8gb\xa4-\xd3'"

def store_bookmark(url,description):
    bookmarks.append(dict(url=url,user="John",date = datetime.utcnow(),description=description))

def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm:['date'],reverse=True)[:num]

@app.route('/')
@app.route('/index')
def index():
    user = User("jan", "kowalski")
    return render_template('index.html',Title="Title passed",user=user,Text=["asd","bcd","123"],new_bookmarks=new_bookmarks(5))

# @app.route('/add', methods=['GET','POST'])
# def add():
#     if request.method == "POST":
#         url = request.form['url']
#
#         store_bookmark(url)
#         # app.logger.debug('stored url %s' % url)
#         flash("Stored bookmark '{}'".format(url))
#         return  redirect(url_for('index'))
#     return render_template('add.html',Text="1232")

@app.route('/add', methods=['GET','POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description=form.description.data

        store_bookmark(url,description)
        # app.logger.debug('stored url %s' % url)
        flash("Stored bookmark '{}'".format(description))
        return  redirect(url_for('index'))
    return render_template('add.html',Text="1232",form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500

if __name__== "__main__":
    app.run(debug=True)
    # app.logger.setLevel(DEBUG)

