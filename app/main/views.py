from flask import render_template,redirect,url_for,abort,request, flash
from . import main
from flask_login import login_required, current_user
from .. models import User,Blog,Comments
from .forms import BlogForm,CommentsForm
from app import db
from ..requests import get_quote

@main.route("/")
def index():
    title = "G-Blogs"
    blogs = Blog.query.all()
    show_quote = get_quote()
    quote = show_quote['quote']
    quote_author = show_quote['author']
    
    return render_template("index.html", title = title, blogs = blogs, quote = quote,quote_author = quote_author )


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
    return render_template('blog.html', form = form,legend = 'Create Post')

@main.route('/details/<int:id>', methods = ['GET','POST'])
@login_required
def details(id):
    blog = Blog.query.get_or_404(id)
    # form = CommentsForm()
    # comments = Comments.query.all()
    
    # if form.validate_on_submit():
    #     comment = form.comment.data
    #     new_comment = Comments(comment = comment)
    #     new_comment.save_comment()
        
    #     return redirect(url_for('main.details'))
        
    
    return render_template('blog_review.html', blog = blog)


@main.route('/details/<int:id>/update', methods = ['GET','POST'])
@login_required
def update_details(id):
    blog = Blog.query.get_or_404(id)
    if blog.author != current_user:
        abort(403)
        
    form = BlogForm()
    if form.validate_on_submit:
        blog.title = form.title.data
        blog.content = form.content.data
        db.session.commit()
        flash("Your Post Has Been Updated!")
        return redirect(url_for('main.update_details'))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    
    return render_template('blog.html', title = 'Update Post', form = form, legend = 'Update Post')
    
    
@main.route('/details/<int:id>/delete', methods = ['POST'])
@login_required
def delete_post(id):
    blog = Blog.query.get_or_404(id)
    if blog.author != current_user:
        abort(403)
    db.session.delete(blog)
    db.session.commit()
    flash("Your Post Has Been Deleted")
    return redirect(url_for('main.index'))
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
     