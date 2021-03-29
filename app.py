from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/estimate')
def vtm_site():
    return render_template('estimate.html')

@app.route('/add')
def add():
    if request.method == 'POST':
        radius = request.form['radius']
        height = request.form['height']
        
    return render_template('estimate.html')

if __name__ == '__main__':
    app.run(debug=True)