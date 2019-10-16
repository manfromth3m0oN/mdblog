from flask import Flask, render_template, url_for, send_from_directory
from os import listdir
from os.path import isfile, join
import os

app = Flask(__name__)

articles = [ f for f in listdir('static/blog/') if isfile(join('static/blog', f))]

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
	return render_template('index.html', articles=articles)

@app.route('/blog/<title>')
def blog(title):
	print(title)
	markdown = open('static/blog/'+title, 'r').read()
	return render_template('blog.html', markdown=markdown, title=title)

@app.route('/video', defaults={'folder': ''})
@app.route('/video/<path:folder>')
def videoselect(folder):
	print(folder)
	videos = [f for f in listdir('static/videos/'+folder) if isfile(join('static/videos'+folder, f))]
	for i in range(1, len(videos)):
		videos[i-1] = url_for(videos[i])
	dirs = [x[0] for x in os.walk('static/videos/'+folder)]
	for i in range(0, len(dirs)):
		dirs[i] = dirs[i].strip('static/videos/')
	print('vids:')
	print(videos)
	print('dirs:')
	print(dirs)
	return render_template('video.html', dirs=dirs, videos=videos)

@app.route('/play/<path:vidfile>')
def play(vidfile):
	vid = url_for('static/videos', filename=vidfile)
	return render_template('play.html', vidfile=vid)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
