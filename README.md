# Heroku example

This repo provides an example of a [heroku deployable application](https://devcenter.heroku.com/categories/python-support) made with [Bocadillo](https://bocadilloproject.github.io).

## Install
- You just need [heroku-cli](https://devcenter.heroku.com/articles/heroku-cli) installed on your machine. 

## Requirements
- python==3.6.8
- bocadillo==0.13.0
- gunicorn==19.9.0

## Usage
First, login & create an app via [heroku-cli](https://devcenter.heroku.com/articles/heroku-cli) or in [heroku dashboard](https://dashboard.heroku.com).
```
heroku login 
heroku apps:create my-bocadillo-app
```

Then add heroku git remote.
```
heroku git:remote -a my-bocadillo-app
```

Finally, push & deploy to Heroku.
```
git push heroku master
```

The app will then be accessible at https://my-bocadillo-app.herokuapp.com/
