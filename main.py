from flask import Flask
from app.config.server_message import print_server_message
from app.router import api_blueprint


app = Flask(__name__)
app.register_blueprint(api_blueprint, url_prefix="/api")

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    print_server_message()
    app.run(debug=True)
