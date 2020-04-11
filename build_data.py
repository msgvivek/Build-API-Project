import sqlite3
import ast

def create_conn():
    conn = sqlite3.connect('example.db', check_same_thread=False)
    conn.cursor().execute('CREATE TABLE IF NOT EXISTS comments (status, like, dislike)')
    conn.commit()
    return conn

def insert_values(conn, data):
    conn.cursor().execute('INSERT into comments VALUES (?, 0, 0)', (data.get("status"),))
    conn.commit()
    return True

def retrieve_values(conn):
    each_list = []
    for each in conn.cursor().execute('SELECT * FROM comments'):
        each_list.append(each)
    return each_list

def update_values(conn, data):
    # data contains key,value pairs
    # status == Text message
    # flag == True (implies like)
    # flag == False (implies dislike)
    status = data.get("status")
    flag = data.get("flag")
    if flag:
        conn.cursor().execute('UPDATE comments SET like = like + 1 WHERE status = (?)', (status,))
    else:
        conn.cursor().execute('UPDATE comments SET dislike = dislike + 1 WHERE status = (?)', (status,))
    conn.commit()
    return True

def delete_values(conn, data):
    status = data.get("status")
    conn.cursor().execute('DELETE FROM comments WHERE status = (?)', (status,))
    conn.commit()
    return True
