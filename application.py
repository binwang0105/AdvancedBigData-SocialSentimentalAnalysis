from flask import Flask
from flask import request
from flask import render_template
import sql as s


application = Flask(__name__)

@application.route('/', methods=['GET'])
@application.route('/hello', methods=['GET', 'POST'])
@application.route('/hello/<name>', methods=['GET', 'POST'])
def hello(name=None):
    return 'hello world!'


@application.route('/index', methods=['GET', 'POST'])
def index(name=None):
    if request.method == 'POST':
        #c = s.connect_db()
        #res = s.filter(c, text=request.form['product'], category=request.form['category'])
        tweets = []
        #tweets = []
        #for r in res:
        #    if(not str(r[2].encode("ascii", "ignore")) == "None"):
        #    	st = ""
        #    	st = "['" + r[0] + "','" + r[1] + "'," + r[2] + "]"
        #    	tweets.append(st.encode("ascii","ignore"))
                #tweets.append(format_js(r))


        #send = "[" + "], [".join(str(", ".join(str(y) for y in x)) for x in tweets) + "]"
        #send = ", ".join(str(x) for x in tweets)
        #send = "[" + send + "]"
        #js array [a,b,c]
        #populate google map
        return render_template('index.html', tweets=[1,2,3])
    else:
        return render_template('index.html', tweets=[])

if __name__ == '__main__':
    application.debug = False 
    application.run(host='0.0.0.0')
