# Dice rolling game

[![Build Status](https://travis-ci.org/Pythonian/bsawf.svg?branch=master)](https://travis-ci.org/Pythonian/bsawf) [![Coverage Status](https://coveralls.io/repos/github/Pythonian/bsawf/badge.svg?branch=master)](https://coveralls.io/github/Pythonian/bsawf?branch=master)

A dice rolling web application game built with Flask

## Requirements

- Python 3.7+
- A Heroku hobby-dev plan and Heroku CLI installed locally
- PostgreSQL database installed locally
- Redis server installed locally
- Sentry account for Error logging
- Mailtrap account for sending test emails during development

## Local Setup

This walkthrough assumes you're using a Windows OS

**Step 1**: Clone the git repository

    $ git clone https://github.com/Pythonian/bsawf.git
    $ cd bsawf

**Step 2**: Create a virtual environment.

    $ python -m venv venv
    $ venv\scripts\activate
    (venv) > pip install -r requirements.txt

**Step 3**: Setup Flask environment variables

    $ set FLASK_APP=snakeeyes.app
    $ set FLASK_ENV=development

**Step 4**: Setup a .env file and modify the default settings

    $ cp .env.example .env

**Step 5**: Create a PostgreSQL table for the application

**Step 6**: Run the database migration command

    $ flask db upgrade

**Step 7**: Open up the redis-server installed

**Step 8**: Install the custom command tools

    $ pip install --editable .

**Step 9**: Start the development server

    $ flask run


## Heroku Setup

This guide walks you through deployment on Heroku.

**Step 1**: Login to heroku via your command prompt and enter your credentials

    $ heroku login

**Step 2**: Create a new application on Heroku

    $ heroku create

**Step 3**: Deploy the app to heroku

    $ git push heroku master

**Step 4**: Configure the addons required for this project

    $ heroku addons:create heroku-postgresql:hobby-dev
    $ heroku addons:create heroku-redis:hobby-dev

**Step 5**: Set configuration variables for the app replacing default values with yours

    $ heroku config:set SECRET_KEY=8ajs892jsskaloepst3y
    $ heroku config:set DEBUG=False
    $ heroku config:set FLASK_ENV=production
    $ heroku config:set MAIL_DEFAULT_SENDER=no-reply@example.com
    $ heroku config:set MAIL_PASSWORD=mypassword
    $ heroku config:set MAIL_USERNAME=myusername
    $ heroku config:set MAIL_PORT=2525
    $ heroku config:set MAIL_SERVER=smtp.mailtrap.io
    $ heroku config:set MAIL_USE_SSL=False
    $ heroku config:set MAIL_USE_TLS=True
    $ heroku config:set SENTRY_SDK=https://80@321.ingest.sentry.io/85
    $ heroku config:set ANALYTICS_GOOGLE_UA=XXX

**Step 6**: Allocate a web and worker process to run our app

    $ heroku ps:scale web=1
    $ heroku ps:scale worker=1

**Step 7**: Run the database migration

    $ heroku run flask db upgrade

**Step 8**: Open your application in a browser

    $ heroku open
