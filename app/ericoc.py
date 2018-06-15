from flask import Flask, render_template

pages = { 'projects': 'Projects', 'about': 'About', 'resume': 'Résumé' }

ericoc = Flask(__name__)


def fill_page(page, title, code=200):
    template = page + '.html.j2'
    return render_template(template, page=page, title=title, pages=pages), code


@ericoc.route('/')
def index():
    default_page = 'about'
    return fill_page(page=default_page, title=None)


@ericoc.route('/<page>/')
def jawn(page):

        if page in pages:
            return fill_page(page=page, title=pages[page])
        else:
            return fill_page(page='404', title='Page Not Found', code=404)


if __name__ == "__main__":
    ericoc.run()
