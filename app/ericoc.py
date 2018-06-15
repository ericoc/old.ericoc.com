from flask import Flask, render_template

pages = { 'projects': 'Projects', 'about': 'About', 'resume': 'Résumé' }

ericoc = Flask(__name__)


def jawn(page='about', title=None, code=200):
    return render_template('index.html.j2', page=page, title=title, pages=pages), code


@ericoc.route('/')
def index():
    return jawn()


@ericoc.route('/<page>/')
def specific(page):

        if page in pages:
            return jawn(page=page, title=pages[page])
        else:
            return page_not_found(page);


@ericoc.errorhandler(404)
def page_not_found(error):
    return jawn(page='404', title='Page Not Found', code=404)


if __name__ == "__main__":
    ericoc.run()
