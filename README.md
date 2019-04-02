# Heroku example

This repo provides an example of a [heroku deployable application](https://devcenter.heroku.com/categories/python-support) made with [Bocadillo](https://bocadilloproject.github.io).

## Install

You'll need [heroku-cli](https://devcenter.heroku.com/articles/heroku-cli) installed on your machine.

Install dependencies with:

```python
pip install -r requirements.txt
```

Note: this particular example project deploys the application with Python 3.6.8. You can edit the `runtime.txt` file to specify which version of Python Heroku should use.

## Usage

First, login & create an app via [heroku-cli](https://devcenter.heroku.com/articles/heroku-cli) or in the [Heroku dashboard](https://dashboard.heroku.com).

```
heroku login
heroku apps:create my-bocadillo-app
```

Then add the Heroku git remote:

```
heroku git:remote -a my-bocadillo-app
```

Finally, push & deploy to Heroku:

```
git push heroku master
```

The app will then be accessible at https://my-bocadillo-app.herokuapp.com/. 🚀
