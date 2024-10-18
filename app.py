

from flask import Flask

# create a flask app instance 
app = Flask(__name__)

# define the home route ('/')
@app.route('/')
def home():
    return "Hello,flask!"

#define another route ('/about')
@app.route('/about')
def about():
    return "This is the about page."

#run the flask app 
if __name__ == '_main_':
    app.run(debug=True)
