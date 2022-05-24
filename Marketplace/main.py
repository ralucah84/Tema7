from users.functions import *

def print_menu_options():
    print(f"Available options: {list(menu_options.keys())}")

def exit_message():
    print('Have a nice day!')

menu_options = {
    "create_user": create_user,
    "delete_user": delete_user,
    "list_users": list_users,
    "list_user": list_user,
    "update_user": update_user,
    "help": print_menu_options,
    "exit": exit_message
}


def main():
    option = ''
    while option != "exit":
        option = input("Choose an option (type help for menu options, exit to leave): ")
        function_to_call = menu_options.get(option)
        if function_to_call:
            function_to_call()
        else:
            print("You did not input a valid option")
            print_menu_options()


if __name__ == '__main__':
    main()

import json

from users.functions import *

from flask import Flask, request, Response


app = Flask("Marketplace API")

@app.route('/list_users', methods=["GET"])
def list_users():
    status_code, users_returned = list_users_flask()
    return Response(status=status_code, response=json.dumps(users_returned))

@app.route('/get_user/<user_id>', methods=["GET"])
def get_user(user_id):
    status_code, users_returned = get_user_flask(user_id)
    return Response(status=status_code, response=json.dumps(users_returned))

@app.route('/add_user',methods=["POST"])
def add_user():
    post_data=json.loads(request.data)
    name = post_data['name']
    email = post_data["email"]
    status_code, user_returned = create_user_flask(name,email)
    return Response(status=status_code, response=json.dumps(user_returned))


# TODO: implement the missing APIs for users, products and orders

if __name__ == '__main__':
    app.run()