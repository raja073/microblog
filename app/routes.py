from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'raja'}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Post 1'
		},
		{
			'author': {'username': 'Nolan'},
			'body': 'Post2'
		}
		]
	return render_template('index.html', title='Home', user=user, posts=posts)
