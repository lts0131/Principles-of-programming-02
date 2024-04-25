import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO user_info (user_name, password,user_type,user_nickname,membership_grade) VALUES (?, ?,?,?,?)",
            ('lts', '123456', 'admin', 'George Liu', 0))

cur.execute("INSERT INTO user_info (user_name, password,user_type,user_nickname,membership_grade) VALUES (?, ?,?,?,?)",
            ('yjj', '123456', 'user', 'JingJing Yang', 3))

cur.execute("INSERT INTO user_info (user_name, password,user_type,user_nickname,membership_grade) VALUES (?, ?,?,?,?)",
            ('see', '123456', 'admin', 'SanSan Han', 3))

cur.execute("INSERT INTO user_info (user_name, password,user_type,user_nickname,membership_grade) VALUES (?, ?,?,?,?)",
            ('yxj', '123456', 'user', 'XueJing Yang', 2))

cur.execute("INSERT INTO user_info (user_name, password,user_type,user_nickname,membership_grade) VALUES (?, ?,?,?,?)",
            ('test', '123456', 'admin', 'WENYU Han', 1))

cur.execute("INSERT INTO user_info (user_name, password,user_type,user_nickname,membership_grade) VALUES (?, ?,?,?,?)",
            ('test2', '123456', 'admin', 'George Liu', 0))

cur.execute("INSERT INTO user_info (user_name, password,user_type,user_nickname,membership_grade) VALUES (?, ?,?,?,?)",
            ('test3', '123456', 'user', 'JingJing Yang', 3))

cur.execute("INSERT INTO user_info (user_name, password,user_type,user_nickname,membership_grade) VALUES (?, ?,?,?,?)",
            ('test4', '123456', 'admin', 'SanSan Han', 3))

cur.execute("INSERT INTO user_info (user_name, password,user_type,user_nickname,membership_grade) VALUES (?, ?,?,?,?)",
            ('test5', '123456', 'user', 'XueJing Yang', 2))

cur.execute("INSERT INTO user_info (user_name, password,user_type,user_nickname,membership_grade) VALUES (?, ?,?,?,?)",
            ('test6', '123456', 'admin', 'WENYU Han', 1))


cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Changjin Lake', 'china', 'chinese', '22214', '5213', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Wandering Earth', 'china', 'chinese', '32121', '3222', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('A Man Called Otto', 'usa', 'english', '22123', '4311', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('The Whale', 'usa', 'english', '24111', '2233', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('M3GAN', 'usa', 'english', '25111', '1231', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Changjin Lake', 'china', 'chinese', '22214', '5213', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Wandering Earth', 'china', 'chinese', '32121', '3222', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('A Man Called Otto', 'usa', 'english', '22123', '4311', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('The Whale', 'usa', 'english', '24111', '2233', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Changjin Lake', 'china', 'chinese', '22214', '5213', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Wandering Earth', 'china', 'chinese', '32121', '3222', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('A Man Called Otto', 'usa', 'english', '22123', '4311', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('The Whale', 'usa', 'english', '24111', '2233', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('M3GAN', 'usa', 'english', '25111', '1231', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Changjin Lake', 'china', 'chinese', '22214', '5213', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Wandering Earth', 'china', 'chinese', '32121', '3222', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('A Man Called Otto', 'usa', 'english', '22123', '4311', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('The Whale', 'usa', 'english', '24111', '2233', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Changjin Lake', 'china', 'chinese', '22214', '5213', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Wandering Earth', 'china', 'chinese', '32121', '3222', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('A Man Called Otto', 'usa', 'english', '22123', '4311', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('The Whale', 'usa', 'english', '24111', '2233', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('M3GAN', 'usa', 'english', '25111', '1231', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Changjin Lake', 'china', 'chinese', '22214', '5213', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Wandering Earth', 'china', 'chinese', '32121', '3222', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('A Man Called Otto', 'usa', 'english', '22123', '4311', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('The Whale', 'usa', 'english', '24111', '2233', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Changjin Lake', 'china', 'chinese', '22214', '5213', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Wandering Earth', 'china', 'chinese', '32121', '3222', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('A Man Called Otto', 'usa', 'english', '22123', '4311', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('The Whale', 'usa', 'english', '24111', '2233', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('M3GAN', 'usa', 'english', '25111', '1231', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Changjin Lake', 'china', 'chinese', '22214', '5213', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Wandering Earth', 'china', 'chinese', '32121', '3222', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('A Man Called Otto', 'usa', 'english', '22123', '4311', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('The Whale', 'usa', 'english', '24111', '2233', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Changjin Lake', 'china', 'chinese', '22214', '5213', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Wandering Earth', 'china', 'chinese', '32121', '3222', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('A Man Called Otto', 'usa', 'english', '22123', '4311', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('The Whale', 'usa', 'english', '24111', '2233', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('M3GAN', 'usa', 'english', '25111', '1231', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Changjin Lake', 'china', 'chinese', '22214', '5213', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Wandering Earth', 'china', 'chinese', '32121', '3222', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('A Man Called Otto', 'usa', 'english', '22123', '4311', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('The Whale', 'usa', 'english', '24111', '2233', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Changjin Lake', 'china', 'chinese', '22214', '5213', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Wandering Earth', 'china', 'chinese', '32121', '3222', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('A Man Called Otto', 'usa', 'english', '22123', '4311', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('The Whale', 'usa', 'english', '24111', '2233', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('M3GAN', 'usa', 'english', '25111', '1231', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Changjin Lake', 'china', 'chinese', '22214', '5213', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Wandering Earth', 'china', 'chinese', '32121', '3222', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('A Man Called Otto', 'usa', 'english', '22123', '4311', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('The Whale', 'usa', 'english', '24111', '2233', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Changjin Lake', 'china', 'chinese', '22214', '5213', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Wandering Earth', 'china', 'chinese', '32121', '3222', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('A Man Called Otto', 'usa', 'english', '22123', '4311', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('The Whale', 'usa', 'english', '24111', '2233', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('M3GAN', 'usa', 'english', '25111', '1231', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Changjin Lake', 'china', 'chinese', '22214', '5213', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('Wandering Earth', 'china', 'chinese', '32121', '3222', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('A Man Called Otto', 'usa', 'english', '22123', '4311', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_info (video_name, video_type,video_language,video_length,video_fps,video_clarity,video_decoding_rate,video_description) VALUES (?,?,?,?,?,?,?,?)",
    ('The Whale', 'usa', 'english', '24111', '2233', '1024', '265','no description'))

cur.execute(
    "INSERT INTO video_income_table (video_id, video_income,users_name) VALUES (?,?,?)",
    ('1', '20', 'yjj'))
cur.execute(
    "INSERT INTO video_income_table (video_id, video_income,users_name) VALUES (?,?,?)",
    ('2', '15', 'yjj'))
cur.execute(
    "INSERT INTO video_income_table (video_id, video_income,users_name) VALUES (?,?,?)",
    ('3', '11', 'yjj'))
cur.execute(
    "INSERT INTO video_income_table (video_id, video_income,users_name) VALUES (?,?,?)",
    ('4', '25', 'yjj'))
cur.execute(
    "INSERT INTO video_income_table (video_id, video_income,users_name) VALUES (?,?,?)",
    ('5', '19', 'yjj'))

cur.execute(
    "INSERT INTO video_income_table (video_id, video_income,users_name) VALUES (?,?,?)",
    ('1', '40', 'test'))
cur.execute(
    "INSERT INTO video_income_table (video_id, video_income,users_name) VALUES (?,?,?)",
    ('2', '30', 'test'))
cur.execute(
    "INSERT INTO video_income_table (video_id, video_income,users_name) VALUES (?,?,?)",
    ('3', '22', 'test'))

cur.execute(
    "INSERT INTO video_income_table (video_id, video_income,users_name) VALUES (?,?,?)",
    ('1', '40', 'test'))
cur.execute(
    "INSERT INTO video_income_table (video_id, video_income,users_name) VALUES (?,?,?)",
    ('2', '30', 'test'))
cur.execute(
    "INSERT INTO video_income_table (video_id, video_income,users_name) VALUES (?,?,?)",
    ('3', '22', 'test'))

cur.execute(
    "INSERT INTO video_income_table (video_id, video_income,users_name) VALUES (?,?,?)",
    ('1', '35', 'test2'))
cur.execute(
    "INSERT INTO video_income_table (video_id, video_income,users_name) VALUES (?,?,?)",
    ('2', '30', 'test2'))
cur.execute(
    "INSERT INTO video_income_table (video_id, video_income,users_name) VALUES (?,?,?)",
    ('3', '22', 'test2'))

cur.execute(
    "INSERT INTO video_income_table (video_id, video_income,users_name) VALUES (?,?,?)",
    ('1', '40', 'test3'))
cur.execute(
    "INSERT INTO video_income_table (video_id, video_income,users_name) VALUES (?,?,?)",
    ('2', '30', 'test3'))
cur.execute(
    "INSERT INTO video_income_table (video_id, video_income,users_name) VALUES (?,?,?)",
    ('3', '22', 'test3'))

connection.commit()
connection.close()
