import MySQLdb
import string

def connect_db():
    conn = MySQLdb.connect("localhost","root","root","tweets")
    return conn

def build(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE tweets
                     (id int, time text, content text, category text, sentiment text)''')
    conn.commit()

def cclose(conn):
    conn.commit()
    conn.close()

def get(conn, text, category, emotion):
    c = conn.cursor()
    result = []
    for row in c.execute('SELECT * FROM tweets').fetchall():
        if((text.lower() in row[2].lower()) and
          (category.lower() in row[3].lower() and
           emotion.lower() in row[4].lower())):
            result.append(row)
    print len(result)
    #sql = "SELECT * FROM tweets WHERE content like '%product%' and category='kind'"
    #c.execute("SELECT * FROM tweets WHERE content LIKE %s and category = %s and sentiment = %s", ("%" + text + "%",category, emotion))
    return len(result)

def filter(conn, text1, text2):
    results = []
    results[0] = get(conn, text1, text2, 'positive') #postive
    results[1] = get(conn, text1, text2, 'neutral')
    results[2] = get(conn, text1, text2, 'negative') #negative
    return results

