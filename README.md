# Markdown Blog

## Why and motivation
First of all, I needed a new personal project; second, blogging seemed cool; third, I like writing in markdown. So as a summation of all of these things i decided to make a system whereby a blogger could just drop .md files into a static folder and render them to a user.

## How
Markdown is parsed in python by [python-markdown2](https://github.com/trentm/python-markdown2) 
Code blocks are done with pygments and latex is rendered through [mathjax](https://www.mathjax.org/)
Site is served by [flask](https://palletsprojects.com/p/flask/) which grabs a markdown file and parses it to markdown2 for rendering
A title page is made and md files are listed automatically each page is just markdown and some *eyecandy*

## Get started 
* Clone the repo with `git clone https://github.com/manfromth3m0oN/mdblog.git`
* Install depencies with `pip install -r requirements.txt` **or** `pip3 install -r requirements.txt`
* Edit the `index.html` file to adjust it to your liking
* Fill the `blog` folder with some content (markdown files to be used as blog posts)
* Run `app.py` with python(3) to start the server
**Its that easy**

## Notes
* There may be issues with the requirements.txt. If it doesent work or has issues, let me know
    * It was generated with [pipdeptree](https://pypi.org/project/pipdeptree/) using `pipdeptree -f --warn silence | grep -P '^[\w0-9\-=.]+' > requirements.txt`
