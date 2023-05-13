from flask import Flask, request, render_template, flash
from Databases.DatabasesManager import get_database
from Readers.ReadersManager import get_reader
from fuzzywuzzy import fuzz
import yaml

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

app = Flask(__name__)
app.secret_key = config['secret_key']


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
        try:
            content = reader.read()
            result = search(search_from_user, content)
            if result != "":
                flash(f'""{search_from_user}" is in the {result} page"', "secondary")
            else:
                flash(f'Could not find "{search_from_user}"', 'warning')
        except:
            flash(f'Could not read from Confluence', 'danger')

    searches_counter = db.get_num_of_queries()
    return render_template("index.html", num_of_queries=searches_counter)


if __name__ == "__main__":
    db = get_database()
    reader = get_reader()

    app.run(debug=True)
