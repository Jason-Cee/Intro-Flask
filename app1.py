from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return """<body style = background-color:aqua><h1>This is my first Flask app</h1>
            <a href='http://127.0.0.1:5000/index/'><button>Index</button>
            </body>"""


@app.route("/index/")
def index_page():
    return """<body style = background-color:aqua><h1>This is my Index page</h1>
            <a href='http://127.0.0.1:5000/about/'><button>About</button>
            <a href='http://127.0.0.1:5000/'><button>Back</button>
            </body>"""


@app.route("/about/")
def about_page():
    return """<body style = background-color:aqua><h1>This is my About page</h1>
            <a href='http://127.0.0.1:5000/project/'><button>Project</button>
            <a href='http://127.0.0.1:5000/index/'><button>Back</button>
            </body>"""


@app.route("/project/")
def project_page():
    return """<body style = background-color:aqua><h1>This is my Project page</h1>
            <a href='http://127.0.0.1:5000/contact/'><button>Contact</button>
            <a href='http://127.0.0.1:5000/about/'><button>Back</button>
            </body>"""


@app.route("/contact/")
def contact_page():
    return """<body style = background-color:aqua><h1>This is my Project page</h1>
            <a href='http://127.0.0.1:5000/project/'><button>Back</button>
            </body>"""


if __name__ == "__main__":
    app.debug = True
    app.run()
