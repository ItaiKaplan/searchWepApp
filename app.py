from flask import Flask, request, render_template, flash
import redis
app = Flask(__name__)
app.secret_key = "itai123456enlightEx$$$"
r = redis.Redis(host='localhost', port=6379, db=0)


@app.route('/', methods=['POST', 'GET'])
@app.route("/home", methods=["POST", "GET"])
@app.route("/index", methods=["POST", "GET"])
def search():
    if request.method == 'POST' and request.form['search'] != "":
        search = request.form['search']
        r.incr('searches_counter')
        r.lpush('searches', search)
        flash(f'Searching "{search}"', "info")
    searches_counter = int(r.get('searches_counter'))
    return render_template("index.html", num_of_queries=searches_counter)


if __name__ == "__main__":
    app.run(debug=True)
