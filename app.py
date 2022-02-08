from flask import Flask, render_template, jsonify, request, session, logging, Response

app = Flask(__name__)

app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'

quizResults = None

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())


@app.route('/webhook', methods=["GET", "POST"])
def chatbotResponse():
    global quizResults
        
    if request.method == 'GET':
        return "You sent a GET request"
    elif request.method == 'POST':
        return "You sent a POST request"
    else:
        return "You sent an unknown request type"
    '''
    
    quizResults = request.json
    
    print(f"Json data = {request.json}")
           
    # return jsonify({"response": "this is a hard-coded response from Wilson" })
    # return Response(status=200)
    return request.json



@app.route('/quizresults', methods=["GET", "POST"])
def getQuizResults():
    global quizResults

    print(quizResults)
    return quizResults


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
