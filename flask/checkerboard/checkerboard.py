from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def preBuilt():
    return render_template('index.html')

@app.route('/<int:number>')
def oneInp(number):
    return render_template('index.html', numx = number)

@app.route('/<int:x>/<int:y>')
def twoInp(x,y):
    return render_template('index.html', numx = x, numy = y)





if __name__=="__main__":
    app.run(debug=True)