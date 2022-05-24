# partile componente ale unui request:
# 1. request URL
# 2. verb (GET/POST/DELETE/....)
# 3. headers: detalii despre mesaj (de ex: ce fel de mesaj e JSON, XML, HTML, ....) (cookie sunt tot un header)
# 4. body: in cazul requesturilor POST de ex asa se trimit datele (ex: cream un user nou, nume, email, register_date se trimit in body)

import json
from flask import Flask, request

app = Flask("My first web api")

@app.route('/')
def hello_world():
    return "Hello World!!"


@app.route('/home_page', methods=["GET"])
def home_page():
    return "Hello, Welcome to our home page!"


@app.route('/display_message_text', methods=["POST"])
def display_message_text():
    requested_message = request.data.decode("UTF-8")  # decode transforma mesajul din bytes in str
    return f"Hello, your text display message is: {requested_message}"


@app.route('/display_message', methods=["POST"])
def display_message():
    requested_message = json.loads(request.data)  # decode transforma mesajul din bytes in str
    return f"Hello, your json display message is: {requested_message['message']}"


@app.route('/get_user/<user_id>', methods=["GET"])
def get_user(user_id):
    return f"Hello, the user has id = {user_id}"


@app.route('/delete_user/<user_id>', methods=["DELETE"])
def delete_user(user_id):
    return f"Hello, User with id = {user_id} has been deleted"



if __name__ == '__main__':
    app.run()
