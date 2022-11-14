# Nikhil Gadiraju
# Oct. 24, 2022 Class project

"""
Database format

[{
"name": <string>,
"id": <integer>
"blood_type": <string>
"test_name": [<string1>, <string2>, ...]
"test_result": [<string1>, <string2>, ...]
}]

OR

[{
"name": <string>,
"id": <integer>
"blood_type": <string>
"tests": {"test_name1": [result1, result2, ...],
          "test_name2: [result1, result2, ...]}
}]

"""

from pymodm import connect, MongoModel, fields
from flask import Flask, request, jsonify
from database_definition import Patient

app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_on():
    return "DB Server is on"


def add_patient(patient_name, patient_id, blood_type):
    new_patient = Patient(name=patient_name,
                          id=patient_id,
                          blood_type=blood_type)
    added_patient = new_patient.save()
    return added_patient


def init_server():
    connect("mongodb+srv://nikhilgadiraju:547nik0314@bme547.yzyab75.mongodb.net/"
            "db_server?retryWrites=true&w=majority")
    add_patient("Ann Ables", 1, "A+")
    add_patient("Bob Boyles", 2, "B+")
    # initialize logging


@app.route("/new_patient", methods=["POST"])
def add_new_patient_to_server():
    """
    Recieve data from POST request
    Call other functions to do all the work
    """
    in_data = request.get_json()
    message, status_code = add_new_patient_worker(in_data)
    return message, status_code


def add_new_patient_worker(in_data):
    result = validate_new_patient_info(in_data)
    if result is not True:
        # Specify 400 status code (tells user request is not valid)
        return result, 400
    add_patient(in_data["name"],
                in_data["id"],
                in_data["blood_type"])
    return "Patient successfully added", 200


def validate_new_patient_info(in_data):
    if type(in_data) is not dict:
        return "POST data was not a dictionary"
    expected_keys = ["name", "id", "blood_type"]
    for key in expected_keys:
        if key not in in_data:
            return "Key {} is missing from POST data".format(key)
    expected_types = [str, int, str]
    for key, ex_type in zip(expected_keys, expected_types):
        if type(in_data[key]) is not ex_type:
            return "Key {} has the wrong data type".format(key)
    return True


@app.route("/add_test", methods=["POST"])
def add_test():
    in_data = request.get_json()
    message, status_code = add_test_worker(in_data)
    return message, status_code


def add_test_worker(in_data):
    result = validate_test_info(in_data)
    if result is not True:
        return result, 400
    # for dict in db:
    #     if in_data['id'] == dict['id']:
    #         dict["test_name"] = in_data["test_name"]
    #         dict["test_result"] = in_data["test_result"]
    #         return "Tests successfully added", 200
    return "invalid patient ID", 400


def validate_test_info(in_data):
    if type(in_data) is not dict:
        return "POST data was not a dictionary"
    expected_keys = ["id", "test_name", "test_result"]
    for key in expected_keys:
        if key not in in_data:
            return "Key {} is missing from POST data".format(key)
    expected_types = [int, str, int]
    for key, ex_type in zip(expected_keys, expected_types):
        if type(in_data[key]) is not ex_type:
            return "Key {} has the wrong data type".format(key)
    return True


if __name__ == "__main__":
    init_server()
    app.run()
