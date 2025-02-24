from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    print("testing")
    return 'Hello world!'

@app.route('/time')
def get_current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')



app.run(host='0.0.0.0',
        port=8080,
        debug=True)
