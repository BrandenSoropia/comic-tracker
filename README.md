# comic-tracker

A way to track your favourite Image comics and get notified when a new release is out!

Follow development here: https://trello.com/b/ohvWVpsP/comic-tracker

Note:
This is using Comic Vine API. Because of their requirements, I have to "reuse" the request's `User-Agent` to not appear like a web scraper/bot. This seems sketchy/not right, but doing it anyways to get this working.

## Installation:

> I'm using VS Code and will include some project settings/extension recommendations that I found helpful!

Requires Python3, pip, venv, and sqlite (apparently comes with python3).

**Accounts/API Access Sign Up**
1. Also, you'll need a MailTrap account to test emails. They have a free tier, find out more about them on their site: https://mailtrap.io/
2. This is powered by Comic Vine's API. Sign up to get your own access key here: https://comicvine.gamespot.com/api/

**Setup**

1. Create an `.env` file in your local copy of the repo, and make sure it includes the following:

```
export FLASK_APP=flaskr
export FLASK_ENV=development
export COMIC_VINE_API_KEY=<your_comic_vine_api_key>
export SMTP_SERVER_URL=smtp.mailtrap.io
export SMTP_SERVER_PORT=2525
export SMTP_SERVER_SENDER_USER=<your_mailtrap_user>
export SMTP_SERVER_SENDER_PASSWORD=<your_mailtrap_password>
```

2. Create a virtual environment using either:

```
# Unix
$ python3 -m venv venv

# Windows
> py -3 -m venv venv
```

3. Activate virtual env with

```
# Unix
$ . venv/bin/activate

# Windows
> venv\Scripts\activate
```

4. Install dependencies by `pip install -r requirements.txt`

**Running Server**
1. Source dev env variables by running `source .env`
1. Run `flask init-db` to clear and setup tables.
1. Run `flask run` to start your server on `http://127.0.0.1:5000/`

**Testing Emails**
> Followed this tutorial https://thepythonguru.com/sending-emails-in-python-tutorial-with-code-examples/

1. Go to the "email_manager" package: `cd ./flaskr/email_manager`. Do this so images can be sourced appropriately when the send email script is run.
1. Run the script: `python email_manager.py`
1. Login in to your MailTrap account. Emails should be sent to their!

## Running Tests
Uses pytest.

1. Just run `pytest` for a basic overview.
    + For more verbose results, run `pytest -v`

## Building and Deploying App
TODO! Follow Flask's instructions here once ready to deploy: https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/`
