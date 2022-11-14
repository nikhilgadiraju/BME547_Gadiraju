# %% Imports
import requests
from database_definition import Patient

# %% Client Calls


def upload_patient_info(patient_name, patient_id, patient_blood_type):
    out_data = {"name": patient_name, "id": patient_id,
                "blood_type": patient_blood_type}
    try:
        r = requests.post("http://127.0.0.1:5000/new_patient", json=out_data)
    except:
        return "Failed Server Connection", 400
    return r.text, r.status_code

# r = requests.post("http://127.0.0.1:5000/add_test", json=test_data)
# print(r.status_code)
# print(r.text)

# %% Tests


# def test_add_patient():
#     from db_server import add_patient, init_server
#     init_server()
#     patient_name = "Nikhil"
#     patient_id = 555
#     blood_type = "B-"
#     answer = add_patient(patient_name, patient_id, blood_type)
#     find_patient = Patient.objects.raw({"_id": 555}).first()
#     find_patient.delete()
#     assert answer.name == patient_namef
