from flask import render_template,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from .. models import User,Blog,Comments
from .forms import BlogForm,CommentsForm

@main.route("/index")
def index():
    title = "G-Blogs"
    blogs = Blog.query.all()
    return render_template("index.html", title = title, blogs = blogs)


@main.route('/blogs', methods = ['GET','POST'])
@login_required
def blogs():
    
    form = BlogForm()
    
    if form.validate_on_submit():
        title = form.title.data 
        content = form.content.data
        
        blog = Blog(title = title, content = content, author = current_user )
        blog.save_blog()
        
        return redirect(url_for("main.index"))
    return render_template('blog.html', form = form)

@main.route('/blogs/<int:blog_id>', methods = ['GET','POST'])
@login_required
def details(blog_id):
    blogs = Blog.query.get_or_404(blog_id)
    
    return render_template('blog_review.html' blogs = blogs)
    