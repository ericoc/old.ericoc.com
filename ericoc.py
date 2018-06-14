from flask import Flask, request
from pprint import pprint

#pages = { 'projects': 'Projects', 'about': 'About', 'resume': 'Résumé' }
#default_page = 'about'

ericoc = Flask(__name__)

@ericoc.route('/')
def index():
    return "Hello, world!"


@ericoc.route('/hello/<name>')
def hello(name):

    if name == 'test':
#        pprint(request)
        print(request.__dict__)
        return "stuff: %s" % format(request)

    else:
        return "Hello, {}!".format(name)

if __name__ == "__main__":
    ericoc.run() # this is never run
