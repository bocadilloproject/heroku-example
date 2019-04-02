from bocadillo import App

app = App()


@app.route("/")
async def index(req, res):
    res.text = "Hello, from Heroku!"


if __name__ == "__main__":
    app.run()
