from flask import Flask, request, render_template, flash
from Databases.RedisDB import RedisDB
from fuzzywuzzy import fuzz

from Readers.ConfluenceReader import ConfluenceReader


app = Flask(__name__)
app.secret_key = "itai123456enlightEx$$$"
app.config['DATABASE_TYPE'] = 'redis'
app.config['READER_TYPE'] = 'confluence'


def get_database():
    if app.config['DATABASE_TYPE'] == 'redis':
        return RedisDB('localhost', 6379, 0)
    elif app.config['DATABASE_TYPE'] == 'sqlalchemy':
        # Implement a SQLAlchemy based DB
        pass
    else:
        raise ValueError(f"Unknown database type: {app.config['DATABASE_TYPE']}")

def get_reader():
    if app.config['READER_TYPE'] == 'confluence':
        BASE_URL = 'https://enlight-exercise.atlassian.net'
        USERNAME = 'iykaplan1@gmail.com'
        API_TOKEN = "ATATT3xFfGF0kP3fduclL5h6M40z8FA8cJAKNtl-fxKJhkSRGGSDBARIbMb_Pz4q_6P8aL116cukj1xlIFn8V7ZtnWwU0g9C5sC2o46j3EgzP0TLHkpmhH1I-zsvp2kK_vEVef2WKJpbm2aHmmx1JZBFJjziSBsXvxMuQmYz-077tdaWXomuAZc=A279DF23"
        SPACE = 'Exercise'
        return ConfluenceReader(BASE_URL,USERNAME,API_TOKEN,SPACE)
    else:
        raise ValueError(f"Unknown reader type: {app.config['READET_TYPE']}")


db = get_database()
reader = get_reader()


def search(query, content):
    best_match = {
        'match': "",
        'score': 0
    }
    for content in content['page']['results']:
        title = content['title']
        body = content['body']['storage']['value']
        score = fuzz.token_set_ratio(body.lower(), query.lower())
        if score > 80 and score > best_match['score']:
            best_match['score'] = score
            best_match['match'] = title

    return best_match['match']


@app.route('/', methods=['POST', 'GET'])
@app.route("/home", methods=["POST", "GET"])
@app.route("/index", methods=["POST", "GET"])
def search_page():
    if request.method == 'POST' and request.form['search'] != "":
        search_from_user = request.form['search']
        db.insert_search(search_from_user)
        content = reader.read()
        result = search(search_from_user, content)
        if result != "":
            flash(f'"{search_from_user} is in the {result} page"', "success")
        else:
            flash(f'Could not find {search_from_user}', 'warning')
    searches_counter = db.get_num_of_queries()
    return render_template("test.html", num_of_queries=searches_counter)


if __name__ == "__main__":
    app.run(debug=True)
