from flask_wtf import Form

from wtforms.fields import StringField
# from wtforms.fields import URLField
# from flask.ext.wtf.html5 import URLField
from wtforms.validators import DataRequired,url

class BookmarkForm(Form):
    url=StringField('url', validators=[DataRequired()])
    description = StringField('description')
