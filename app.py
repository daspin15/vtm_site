from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/estimate', methods=['GET'])
def estimate():
    return render_template('estimate.html')

@app.route('/add',methods = ['POST'])
def add():
    if request.method == 'POST':
        radius= int(request.form['radius'])
        height = int(request.form['height'])
        topArea = 3.14 * radius**2
        sideArea = 2*(3.14*(radius* height))
        totalArea_in = topArea + sideArea
        totalArea_sq = totalArea_in / 144
        materialCost = totalArea_sq * 25
        laborCost = totalArea_sq * 15
        mySum = materialCost + laborCost
        print(mySum)
    return render_template('estimate.html', myValue = mySum)
    
if __name__ == '__main__':
    app.run(debug=True)