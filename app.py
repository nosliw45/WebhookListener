from flask import Flask, render_template, jsonify, request, session, logging, Response

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    app.logger.info("[index]")
    return render_template('index.html', **locals())



@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():
    # app.logger.setLevel(logging.DEBUG)
    app.logger.info("[chatbotResponse]")
    
    if request.method == 'GET':
        return "You sent a GET request"
    
    if request.method == 'POST':
        the_question = request.form['question']
        #[response, tempName] = processor.chatbot_response(the_question, sessionName)

    # return jsonify({"response": "this is a hard-coded response from Wilson" })
    return Response(status=200)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
