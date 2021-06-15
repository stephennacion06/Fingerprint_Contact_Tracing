from flask import Flask, render_template
from database.db_modules import get_data

app = Flask(__name__)


@app.route('/')
def index():

    lists = get_data()

    return render_template('index.html', lists=lists)


if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=True)
