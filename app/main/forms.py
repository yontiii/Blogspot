from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title = StringField("Blog Title", validators=[Required()])
    content = TextAreaField("Add Content", validators=[Required()])
    submit = SubmitField('Post Blog')
    
class CommentsForm(FlaskForm):
    comment = TextAreaField("Add A Comment", validators=[Required()])
    submit = SubmitField('Post Blog') 