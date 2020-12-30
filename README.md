# comic-tracker

A way to track your favourite Image comics and get notified when a new release is out!

Follow development here: https://trello.com/b/ohvWVpsP/comic-tracker

Note:
This is using Comic Vine API. Because of their requirements, I have to "reuse" the request's `User-Agent` to not appear like a web scraper/bot. This seems sketchy/not right, but doing it anyways to get this working.

## Installation:

> Requires Python3, pip, venv, and sqlite (apparently comes with python3)

I'm using VS Code and will include some project settings/extension recommendations that I found helpful!

**Setup**


1. Create an `.env` file in your local copy of the repo, and make sure it includes the following:

```
export FLASK_APP=flaskr
export FLASK_ENV=development
export COMIC_VINE_API_KEY=<your_secret_key>
```

You can get a Comic Vine API key here: https://comicvine.gamespot.com/api/ (Note: you'll need to sign up with them)

1. Create a virtual environment using either:

```
# Unix
$ python3 -m venv venv

# Windows
> py -3 -m venv venv
```

2. Activate virtual env with

```
# Unix
$ . venv/bin/activate

# Windows
> venv\Scripts\activate
```

3. Install dependencies by `pip install -r requirements.txt`

**Running Server**
1. Source dev env variables by running `source .env`
1. Run `flask init-db` to clear and setup tables.
1. Run `flask run` to start your server on `http://127.0.0.1:5000/`

## Running Tests
Uses pytest.

1. Just run `pytest` for a basic overview.
    + For more verbose results, run `pytest -v`

## Building App

Follows Flask's doc which follows Python's standard distribution "wheel" file.

1. Build by running `python setup.py bdist_wheel`
1. Find in `/dist` with project name and version number!

## Deploying

TODO! Follow Flask's instructions here once ready to deploy: https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/`
