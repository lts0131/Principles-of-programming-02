from flask import render_template, abort, jsonify
from flask import request
from app import app
import json
import os
import signal
import base64
import pandas as pd
import matplotlib.pyplot as plt
from app.databaseConnection import DatabaseConnection
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/data')
def get_data():
    data = {'foo': 'bar'}
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.route('/kill', methods=["POST"])
def kill():
    pid = os.getpid()
    os.kill(pid, signal.SIGINT)
    return 'Flask app has been killed!'


@app.route('/top10_file', methods=["POST"])
def top10_file():
    db = DatabaseConnection()
    c = db.conn.cursor()
    query = 'SELECT (select vi.video_name from video_info vi where vi.id=vt.video_id) as video_name, COUNT(vt.video_id) AS count FROM video_income_table vt GROUP BY vt.video_id ORDER BY count DESC LIMIT 10;'
    df = pd.read_sql(query, db.conn)
    df.plot(kind='bar')
    plt.savefig('./chart1.jpeg')
    base64_str = img_base64("./chart1.jpeg")
    image_obj = {
        'base64_str': f"data:image/jpeg;base64,{base64_str}"
    }
    return image_obj


@app.route('/top5_customers', methods=["POST"])
def top5_customers():
    db = DatabaseConnection()
    c = db.conn.cursor()
    query = 'SELECT (select vi.user_nickname from user_info vi where vi.user_name=vt.users_name) as user_nickname, COUNT(vt.users_name) AS count FROM video_income_table vt GROUP BY vt.users_name ORDER BY count DESC LIMIT 5;'
    df2 = pd.read_sql(query, db.conn)
    df2.plot(kind='bar')
    plt.savefig('./chart2.jpeg')
    base64_str = img_base64("./chart2.jpeg")
    image_obj = {
        'base64_str': f"data:image/jpeg;base64,{base64_str}"
    }
    return image_obj


@app.route('/_404')
def _404():
    abort(404, 'Oops, 404.')


@app.route('/login', methods=["POST"])
def login():
    db = DatabaseConnection()
    username = request.json.get("username")
    password = request.json.get("password")
    c = db.conn.cursor()
    query = "SELECT * FROM user_info WHERE user_name = '%s' AND password = '%s'" % (username, password)
    posts = c.execute(query).fetchall()
    results = []
    for row in posts:
        results.append(dict(zip([column[0] for column in c.description], row)))
    json_str = json.dumps(results)
    c.close()
    return json_str


@app.route('/video_history', methods=["POST"])
def video_history():
    db = DatabaseConnection()
    user_name = request.json.get("user_name")
    c = db.conn.cursor()
    query = " select vi.* from video_info vi,(SELECT * FROM video_income_table vt WHERE vt.users_name = '%s' ) as vii where vi.id = vii.video_id " % (
        user_name)
    posts = c.execute(query).fetchall()
    results = []
    for row in posts:
        results.append(dict(zip([column[0] for column in c.description], row)))
    json_str = json.dumps(results)
    c.close()
    return json_str


@app.route('/get_all_user', methods=["POST"])
def get_all_user():
    db = DatabaseConnection()
    c = db.conn.cursor()
    query = "SELECT * FROM user_info "
    posts = c.execute(query).fetchall()
    results = []
    for row in posts:
        results.append(dict(zip([column[0] for column in c.description], row)))
    json_str = json.dumps(results)
    c.close()
    return json_str


@app.route('/sum_num', methods=["POST"])
def sum_num():
    db = DatabaseConnection()
    c = db.conn.cursor()
    query = "SELECT SUM(video_income) as sum_num FROM video_income_table;"
    posts = c.execute(query).fetchall()
    results = []
    for row in posts:
        results.append(dict(zip([column[0] for column in c.description], row)))
    json_str = json.dumps(results)
    c.close()
    return json_str


@app.route('/get_all_video', methods=["POST"])
def get_all_video():
    db = DatabaseConnection()
    c = db.conn.cursor()
    query = "SELECT * FROM video_info "
    posts = c.execute(query).fetchall()
    results = []
    for row in posts:
        results.append(dict(zip([column[0] for column in c.description], row)))
    json_str = json.dumps(results)
    c.close()
    return json_str


def img_base64(img_path):
    with open(img_path, "rb") as f:
        base64_str = base64.b64encode(f.read())
    return str(base64_str, 'utf-8')


@app.route('/edit_user', methods=["POST"])
def edit_user():
    db = DatabaseConnection()
    c = db.conn.cursor()
    membership_grade = request.json.get("membership_grade")
    password = request.json.get("password")
    id = request.json.get("id")
    c.execute('UPDATE user_info SET membership_grade = ?, password = ?'
              ' WHERE id = ?',
              (membership_grade, password, id))
    db.conn.commit()
    c.close()
    return "edit ok"


@app.route('/edit_video', methods=["POST"])
def edit_video():
    db = DatabaseConnection()
    c = db.conn.cursor()
    video_name = request.json.get("video_name")
    video_type = request.json.get("video_type")
    video_language = request.json.get("video_language")
    video_length = request.json.get("video_length")
    video_fps = request.json.get("video_fps")
    video_clarity = request.json.get("video_clarity")
    video_decoding_rate = request.json.get("video_decoding_rate")
    video_description = request.json.get("video_description")
    id = request.json.get("id")
    c.execute(
        'UPDATE video_info SET video_name = ?, video_type = ? ,video_language=?,video_length=?,video_fps=?,video_clarity=?,video_decoding_rate=?,video_description=?'
        ' WHERE id = ?',
        (video_name, video_type, video_language, video_length, video_fps, video_clarity, video_decoding_rate,
         video_description, id))
    db.conn.commit()
    c.close()
    return "edit ok"


@app.route('/delete_video', methods=('GET', 'POST'))
def delete_video():
    db = DatabaseConnection()
    c = db.conn.cursor()
    id = request.json.get("id")
    c.execute('DELETE FROM video_info WHERE id = ?', (id,))
    db.conn.commit()
    c.close()
    return "delete ok"


@app.route('/delete_user', methods=["POST"])
def delete_user():
    db = DatabaseConnection()
    c = db.conn.cursor()
    id = request.json.get("id")
    c.execute('DELETE FROM user_info WHERE id = ?', (id,))
    db.conn.commit()
    c.close()
    return "delete ok"


@app.route('/add_payment', methods=["POST"])
def add_payment():
    db = DatabaseConnection()
    c = db.conn.cursor()
    video_id = request.json.get("video_id")
    video_income = request.json.get("video_income")
    users_name = request.json.get("users_name")
    c.execute('INSERT INTO video_income_table (video_id, video_income,users_name) VALUES (?, ?,?)',
              (video_id, video_income, users_name))
    db.conn.commit()
    c.close()
    return "INSERT ok"


'''
The tf-idf feature vector was calculated for each film and the similarity 
between films was calculated using the cosine similarity of.
'''


def get_recommendations(title):
    db = DatabaseConnection()
    c = db.conn.cursor()
    query = "SELECT * FROM video_info "
    tfidf = TfidfVectorizer(stop_words='english')
    df3 = pd.read_sql(query, db.conn)
    tfidf_matrix = tfidf.fit_transform(df3['video_description'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(df3.index, index=df3['video_name']).drop_duplicates()
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1].all(), reverse=True)
    sim_scores = sim_scores[1:9]
    movie_indices = [i[0] for i in sim_scores]
    print(movie_indices)
    return df3.iloc[movie_indices]


@app.route('/for_video', methods=["POST"])
def for_video():
    user_name = request.json.get("user_name")
    sql = "SELECT (select vi.video_name from video_info vi where vi.id=vt.video_id) as video_name, " \
          "COUNT(vt.video_id) AS count FROM video_income_table vt " \
          "where vt.users_name = '%s' GROUP BY vt.video_id ORDER BY count DESC LIMIT 1;" % (user_name)
    print(sql)
    db = DatabaseConnection()
    c = db.conn.cursor()
    df4 = pd.read_sql(sql, db.conn)
    value = df4.iloc[0, 0]
    list_recommended = get_recommendations(value)
    json_data = list_recommended.to_json(orient='records')
    return json_data

