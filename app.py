from flask import Flask, render_template, jsonify, request, session, logging, Response

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    app.logger.info("[index]")
    return render_template('index.html', **locals())



@app.route('/webhook', methods=["GET", "POST"])
def chatbotResponse():
        
    '''
    if request.method == 'GET':
        return "You sent a GET request"
    elif request.method == 'POST':
        return "You sent a POST request"
    else:
        return "You sent an unknown request type"
    '''
    
    #if request.method == 'POST':
        #the_question = request.form['question']
        #[response, tempName] = processor.chatbot_response(the_question, sessionName)
    
    print(f"Json data = {request.json}")
    
    with open("data.txt", "w") as fp:
        fp.write("abcd")
    
    # return jsonify({"response": "this is a hard-coded response from Wilson" })
    # return Response(status=200)
   return request.json



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
