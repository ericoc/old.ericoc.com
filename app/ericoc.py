from flask import Flask, request
from pprint import pprint

pages = { 'projects': 'Projects', 'about': 'About', 'resume': 'Résumé' }

ericoc = Flask(__name__)


@ericoc.route('/')
def index():
    return "Hello, world!"


@ericoc.route('/<page>/')
def jawn(page):

        if page in pages:
            return "Hello, {}!".format(pages[page])
        else:
            return "Not found!", 404

if __name__ == "__main__":
    ericoc.run() # this is never run
