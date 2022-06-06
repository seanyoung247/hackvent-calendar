from flask import Flask
from reactsrv import reactsrv

app = Flask(__name__, static_folder=None)


reactsrv.init(app, 'frontend')


if __name__ == "__main__":
    app.run(debug=True)