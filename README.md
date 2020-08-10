# python_api
An API for something


## Frameworks used
- flask https://flask.palletsprojects.com/en/1.1.x/installation/#installation
    - https://simplejson.readthedocs.io/en/latest/
    - https://github.com/theskumar/python-dotenv#readme
    - https://pythonhosted.org/watchdog/
- jinja templates for html views 
    - https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
    - https://jinja.palletsprojects.com/en/2.11.x/templates/

## Steps to install
1. `git clone https://github.com/DannnB/python_api.git`
2. `cd python_api`
3. `py -3 -m venv venv` for Windows or `python3 -m venv venv` for Linux
4. `venv\Scripts\activate` for Windows or `. venv/bin/activate` for Linux
5. `pip install Flask`
6. `pip install -U python-dotenv`  
7. create `.env` file
8. In the `.env` file add `FLASK_ENV=development` and `FLASK_APP=main.py` 
9. `pip install watchdog`
10. `pip install simplejson`
11. `flask run` this should run the server on port 5000 (default)
12. Build away!

## GIT CMD STEPS
To see your local changes unstaged/staged(eg set with `git commit`)


#### To get changes
1. `git pull`

#### To Push (add) changes
1. `git add FILENAME` or `git add -A` to add all
2. `git commit -m "your message here"`
3. `git pull`


## Routes
- `/` home page
    -`/<name>` test dynamic param to html
