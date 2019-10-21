from flask import Flask, render_template, url_for
from os import listdir
from os.path import isfile, join
import markdown2
app = Flask(__name__)

articles = [ f for f in listdir('static/blogs/') if isfile(join('static/blogs/', f))]

@app.route('/')
def index():
	return render_template('index.html', articles=articles)

@app.route('/<title>')
def blog(title):
	print(title)
	markdownstr = open('static/blogs/'+title, 'r').read()
	markdownstr = markdown2.markdown(markdownstr, extras=["codehilite","fenced-code-blocks"])
	return render_template('blog.html', markdown=markdownstr, title=title)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
