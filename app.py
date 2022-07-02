from flask import Flask
import reactsrv
import challenges

# We want the react app to serve static files
app = Flask(__name__, static_folder=None)


reactsrv.init(app, 'frontend')
challenges.init(app)


if __name__ == "__main__":
    app.run(debug=True)
