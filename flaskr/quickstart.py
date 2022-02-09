from urllib import request
from flask import Flask
from flask import abort, redirect, url_for
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    # username = request.cookies.get('username')
    app.logger.info('Requested index page')
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return '<p>Hello World</p>'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('./uploads/' + secure_filename(f.filename))

@app.route('/tologin')
def tologin():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    app.logger.error('This is never executed')
    this_is_never_executed()