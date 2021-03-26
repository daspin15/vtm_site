from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mike')
def mike():
    return render_template('mike.html')

@app.route('/vtm_site')
def vtm_site():
    return render_template('vtm_site.html')



if __name__ == '__main__':
    app.run(debug=True)