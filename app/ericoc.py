from flask import Flask, request, url_for, render_template
from pprint import pprint

pages = { 'projects': 'Projects', 'about': 'About', 'resume': 'Résumé' }

ericoc = Flask(__name__)


@ericoc.route('/')
def index():
    return render_template('index.html.j2', page_title=None)

@ericoc.route('/<page>/')
def jawn(page):

        if page in pages:
            return render_template('index.html.j2', page_title=pages[page])
        else:
            return "Not found!", 404

if __name__ == "__main__":
    ericoc.run() # this is never run
