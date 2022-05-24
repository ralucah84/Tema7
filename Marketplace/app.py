import json

from users.functions import list_users_flask

from flask import Flask, request, Response


app = Flask("Marketplace API")

@app.route('/list_users', methods=["GET"])
def list_users():
    status_code, users_returned = list_users_flask()
    return Response(status=status_code, response=json.dumps(users_returned))


# TODO: implement the missing APIs for users, products and orders

if __name__ == '__main__':
    app.run()
