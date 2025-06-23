# app.py
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the default URL ("/")
@app.route('/')
def hello_world():
    """This function runs when someone visits the homepage."""
    return 'Hello from the pipeline!'

# This block allows running the app directly from the command line
# with `python app.py`
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)