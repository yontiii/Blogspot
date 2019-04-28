from flask import render_template,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from .. models import User,Blog,Comments
from .forms import BlogForm,CommentsForm

@main.route("/")
def index():
    title = "G-Blogs"
    blogs = Blog.query.all()
    return render_template("index.html", title = title, blogs = blogs)


@main.route('/blogs', methods = ['GET','POST'])
@login_required
def blogs():
    
    form = BlogForm()
    
    if form.validate_on_submit():
        
    
    return render_template('blog.html')
    