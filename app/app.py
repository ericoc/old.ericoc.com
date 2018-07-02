from flask import Flask, render_template, send_from_directory, request, url_for

pages = { 'projects': 'Projects', 'about': 'About', 'resume': 'Résumé' }

app = Flask(__name__)

def jawn(page='about', title=None, code=200):
    return render_template('index.html.j2', page=page, title=title, pages=pages), code

@app.route('/')
def index():
    return jawn()

@app.route('/<page>/')
def specific(page):

        if page in pages:
            return jawn(page=page, title=pages[page])
        else:
            return page_not_found(page);

@app.route('/robots.txt')
@app.route('/sitemap.xml')
@app.route('/favicon.ico')
@app.route('/icon.png')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.errorhandler(404)
def page_not_found(error):
    return jawn(page='404', title='Page Not Found', code=404)

if __name__ == "__main__":
    app.run()
