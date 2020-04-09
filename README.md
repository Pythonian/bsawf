# Dice rolling game [![Build Status](https://travis-ci.org/Pythonian/bsawf.svg?branch=master)](https://travis-ci.org/Pythonian/bsawf)

A dice rolling web application game built with Flask

## Requirements

- Python 3.7+ on any supported OS (even Windows!)
- venv on Python 3.7+
- git (Github)
- Sentry for Error logging
- Mailtrap for sending test emails during development

## Setup

This walkthrough is for Windows 10 users in a command prompt

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

**Step 4**: Setup a .env file and modify the required settings

    $ cp .env.example .env

**Step 5**: Start the development server

    $ flask run
