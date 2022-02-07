#Ref: https://flask.palletsprojects.com/en/2.0.x/quickstart/
#Ref: https://hackersandslackers.com/flask-routes/
#Import the Flask class and related functions used in this app
from flask import Flask, request, redirect, url_for, render_template, Response

#Create an instance of the Flask class and call it as the name 'app'
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def respond():
  print(request.json);
  return Response(status=200)


#app.route("/") is call to the root URL and will execute the codes in the 'home' view function
@app.route("/")
def home():
  #Redirect(url_for ......) is to redirect the user to the path specified in this case /printMessage and pass the variable 'message' over
  return redirect(url_for('printMessage', message='Hello its me!!'))

#Call to the /printMessage URL. It also accepts a second argument which is a list of accepted HTTP methods in this case GET and POST
#and will execute the codes in the 'printMessage' view function which will accept an argument 'message'
@app.route("/printMessage/<message>", methods=['GET','POST'])
def printMessage(message):
  #Execute if the HTML returns back a POST method
  if request.method == 'POST':
    #return render_template will call an HTML page to the user in this case 'post.html' which by default located in the 'templates' directory
    return render_template('post.html',message='This page is called through a POST method')
  #'index.html' will be called first in this view function, only when there is a POST, then 'post.html' will be called
  return render_template('index.html',message=message)

  
