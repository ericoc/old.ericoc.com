from flask import Flask, request, url_for, render_template
from pprint import pprint

pages = { 'projects': 'Projects', 'about': 'About', 'resume': 'Résumé' }

ericoc = Flask(__name__)


def fill_page(page, title):
    template = page + '.html.j2'
    return render_template(template, page=page, title=title, pages=pages)


@ericoc.route('/')
def index():
    default_page = 'about'
    return fill_page(page=default_page, title=None)


@ericoc.route('/<page>/')
def jawn(page):

        if page in pages:
            return fill_page(page=page, title=pages[page])
        else:
            return "Not found!", 404


if __name__ == "__main__":
    ericoc.run() # this is never run
