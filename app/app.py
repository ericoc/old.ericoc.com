from flask import Flask, render_template, send_from_directory, request, url_for

# List of valid pages and their proper titles
pages = {
            'projects'  :   'Projects',
            'about'     :   'About',
            'resume'    :   'Résumé'
        }

# Initialize Flask
app = Flask(__name__)

# Define function to render Jinja2 template for all pages
# Logic within the Jinja2 template includes which ever pages content .html file
@app.route('/')
def index(page='about', title=None, code=200):
    return render_template('index.html.j2', page=page, title=title, pages=pages), code

# Define function to handle page requests if they are valid routes
@app.route('/<page>/')
def specific(page):

        # Only pass page information to the main template function if it is a valid page from our list
        if page in pages:
            return jawn(page=page, title=pages[page])

        # Otherwise, pass the page information to the 404 error handler
        else:
            return page_not_found(page)

# Serve some static files
@app.route('/robots.txt')
@app.route('/sitemap.xml')
@app.route('/favicon.ico')
@app.route('/icon.png')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

# Handle 404 Not Found using a custom page with the main template function
@app.errorhandler(404)
def page_not_found(error):
    return index(page='404', title='Page Not Found', code=404)

# Run Flask
if __name__ == "__main__":
    app.run()
