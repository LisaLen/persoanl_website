from jinja2 import StrictUndefined
from flask import (Flask, request, render_template, redirect, flash, session,jsonify)
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.secret_key = 'ABC'

@app.route('/')
def main_page():
    '''renders main page '''

    return render_template('home.html')

@app.route('/about')
def about():
    '''renders about page'''
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')





if __name__ == '__main__':
    app.debug = False
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    DebugToolbarExtension(app)
    #connect_to_db(app)
    app.run(port=5000, host="0.0.0.0")
