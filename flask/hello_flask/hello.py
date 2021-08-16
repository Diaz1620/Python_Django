from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return   render_template('index.html')# Return the string 'Hello World!' as a response

# @app.route('/success')
# def success():
#     return "success"

# @app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
# def hello(name):
#     print(name)
#     return "Hello, " + name

# @app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id

@app.route('/nba')
def shownba():
    return "placeholder to show info about NBA"

@app.route('/players')
def players():
    return 'placeholder to show a list of all players'

@app.route('/players/<int:playerId>')
def showAPlayer(playerId):
    return render_template('playerInfo.html', playerIdentification = playerId)

@app.route("/play/<int:number>/<color>")
def playboxes(number,color):
    return render_template('boxes.html', num = number, color = color)




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
    
    
    
    
    
    # if playerId > 15:
    #     return "This player does not exist"
    # else:
    #     return f"placeholder to show player number {playerId}"