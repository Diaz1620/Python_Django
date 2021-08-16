from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("index.html")

@app.route('/play/<int:number>')
def boxes(number):
    return render_template('boxes.html', num = number)

@app.route('/play/<color>/<int:number>')
def colorBoxes(color, number):
    return render_template('colorBoxes.html', color=color, num=number)



if __name__=="__main__":
    app.run(debug=True)