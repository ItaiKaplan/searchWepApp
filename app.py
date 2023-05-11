from flask import Flask, request, render_template, flash
import redis
# from flask_sqlalchemy import SQLAlchemy
# from models import Query

app = Flask(__name__)
app.secret_key = "itai123456enlightEx$$$"
r = redis.Redis(host='localhost', port=6379, db=0)
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///queries.sqlite3'
# app.config['SQLALCHEMY_TRAK_MODIFICATIONS'] = False
# db = SQLAlchemy()
# db.init_app(app)


@app.route('/', methods=['POST', 'GET'])
def search():
    if request.method == 'POST' and request.form['query'] != "":
        query = request.form['query']
        r.incr('queries')
        r.lpush('searches', query)
        flash(f'Searching for "{query}"', "info")
    return render_template("index.html")

@app.route('/stats')
def show_stats():
    queries = r.get('queries')
    return f'Total searches: {queries}'

# @app.route("/home", methods=["POST", "GET"])
# @app.route("/index", methods=["POST", "GET"])
# def home():
#     # if request.method == 'POST':
#     #     query = request.form['query']
#     #     q = Query(query=query)
#     #     db.session.add(q)
#     #     db.session.commit()
#     # return render_template('index.html')


if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
