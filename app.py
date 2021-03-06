from flask import Flask, render_template, jsonify, request, session, logging, Response
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'

# quizResults = None
app.config['quizResults'] = None

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())


@app.route('/webhook', methods=["GET", "POST"])
def chatbotResponse():
    global quizResults
        
    '''
    if request.method == 'GET':
        return "You sent a GET request"
    elif request.method == 'POST':
        return "You sent a POST request"
    else:
        return "You sent an unknown request type"
    '''
    
    # quizResults = None
    # quizResults = request.json
    app.config['quizResults'] = request.json
    
    print(f"Json data = {request.json}")
           
    # return jsonify({"response": "this is a hard-coded response from Wilson" })
    # return Response(status=200)
    return request.json



@app.route('/quizresults', methods=["GET", "POST"])
def getQuizResults():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    if app.config['quizResults'] == None:
        return f"[{dt_string}] No results"
    else:
        return app.config['quizResults']


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
