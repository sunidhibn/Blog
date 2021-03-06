from flask import Flask,render_template,request,redirect
from models import blogs

app=Flask("blog")

@app.route('/',methods=['GET','POST'])
def info():
	if request.method=='POST':
		new_user= blogs()
		new_user.username= request.form['user_name']
		new_user.content= request.form['content']
		new_user.title= request.form['title']
		new_user.save()
		return redirect('/')
	else:
		posts= blogs.select().order_by(blogs.posttime.desc())	
		return render_template("home.html",posts=posts)

@app.route('/<username>')
def getPost(username):
	data= blogs.select().where(blogs.username==username).order_by(blogs.posttime.desc())
	return render_template("posts.html",posts=data)

@app.route('/delete/<int:post_id>')
def delete(post_id):
	print post_id
	data= blogs.delete().where(blogs.id==post_id)
	data.execute()
	return redirect('/')

@app.route('/edit/<int:post_id>',methods=['GET','POST'])
def edit(post_id):
	if request.method=='POST':
		content=request.form['content']
		title= request.form['title']
		print content,title
		data=blogs.update(content=content,title=title).where(blogs.id==post_id)
		data.execute()
		return redirect('/')
	else:
		data=blogs.select().where(blogs.id==post_id)
		return render_template("edit.html",posts=data)



app.run(debug=True)