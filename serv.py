import Flask
app = Flask.Flask(__name__, static_url_path="")

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/blog")
def about():
    return app.send_static_file("about.html")

@app.route("/about")
def blog():
    return app.send_static_file("blog.html")

@app.route("/blog/<path:path>")
def blogpost():
    return app.send_from_directory("blog", path+".html")

if __name__ == "__main__":
    app.run()