from flask import Flask, render_template, url_for
from os import listdir
from os.path import isfile, join

app = Flask(__name__)

articles = [ f for f in listdir('static/') if isfile(join('static/', f))]


@app.route('/')
def index():
	return render_template('index.html', articles=articles)

@app.route('/<title>')
def blog(title):
	print(title)
	markdown = open('static/'+title, 'r').read()
	return render_template('blog.html', markdown=markdown, title=title)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
