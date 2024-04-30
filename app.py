from flask import Flask
app = Flask(__name__)

import routes.routes

if __name__ == '__main__':
    app.run()
