from flask import Flask, send_file, request

app = Flask(__name__)

# Use the route() decorator to bind a function to a URL.
@app.route("/")
def hello_world():
    return "Hello, World!"

#The canonical URL for the projects endpoint has a trailing slash. It’s similar to a folder in a file system. If you
# access the URL without a trailing slash (/projects), Flask redirects you to the canonical URL with the trailing slash
# (/projects/).
@app.route('/projects/')
def projects():
    return 'The project page'


# You can add variable sections to a URL by marking sections with <variable_name>. Your function then receives the
# <variable_name> as a keyword argument
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    print(username)
    return username

#HTTP Methods
@app.route('/melody', methods = ['GET','POST'])
def generate_melody_song():
    if request.method == 'POST':
        f = request.files['song']
        print(f)
        filename = f.filename
        print(filename)
        f.save(filename )
        path_to_file = 'song.wav'
        return send_file(path_to_file,mimetype='audio/wav', as_attachment=True,attachment_filename='song.wav')


app.run(host='0.0.0.0')
