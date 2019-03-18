from bocadillo import App, Templates

app = App()
templates = Templates(app)

@app.route("/")
async def index(req, res):
    res.text = "Hello, world!"

@app.route("/home")
async def home(req, res):
    res.html = await templates.render("home.html", title='Hello, from Heroku!')


if __name__ == "__main__":
    app.run()