# server.py

from flask import Flask, request, jsonify  # request sub-module

# Call Flask through the variable app; call all Flask commands through the
# 'app' variable
app = Flask(__name__)

# If a request comes in with just a slash ("/"), the following function
# should run assuming we have a "GET" request
@app.route("/", methods=["GET"])
def server_status():
    return "Server is on."


# Note that to access a new server route, we need to shut down the server
# and rerun the server to update the available routes
@app.route("/info", methods=["GET"])
def information():
    x = "This website will calculate blood cholesterol levels.\n"
    x += "It is written by Nikhil Gadiraju."
    return x


@app.route("/hdl_check", methods=["POST"])
def hdl_check_from_internet():
    """
        incoming_json = {"name": <name_str>,
                         "hdl_value": <hdl_value_int>}
    """
    from blood_calculator import check_HDL
    in_data = request.get_json()
    hdl_value = in_data["hdl_value"]
    print("The received value was {}".format(hdl_value))
    answer = check_HDL(hdl_value)
    return answer


@app.route("/add_numbers", methods=["POST"])
def numsum():
    """
    incoming_json = {"a": <float value>,
                     "b": <float value?=>}
    """
    json_inp = request.get_json()
    answer = json_inp['a'] + json_inp['b']
    return jsonify(answer)


@app.route("/add/<a>/<b>", methods=["GET"])
def add_variable_url(a, b):
    answer = int(a) + int(b)
    return jsonify(answer)


if __name__ == "__main__":
    app.run()

# %% Notes
# - A server should never return a '500 Internal Server Error' since there should be
#   data validation processes in place that can take bad inputs and notify the user
#   of this
# - Unfortunately, we can't use pytest to test these functions since they only work
#   within the context of Flask, and when they're called outside of Flask, they will fail
#   Thus, we must design flask handler functions to outsource all processes to non-Flask
#   functions that can be tested by pytest. Thus flask handler functions must:
#       1) Receive data form the route request
#       2) Call other functions which validate inputs and complete tasks
#       3) Return information to requestor
# - Server code is "event-driven code" meaning th user defines how a given script runs;
#   Thus, server code needs to be designed so that it can handle various different server inputs
#   and numerous server requests.