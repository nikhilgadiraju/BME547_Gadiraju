# BME 547: Medical Software Design
# Blood Matching Mini Project
# Author: Nikhil Gadiraju

# Module Imports
import requests
import json

# Get Recipient and Donor's ID's and Blood Types
r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/nvg6")
r_dict = json.loads(r.text)
recipient_id = r_dict["Recipient"]
donor_id = r_dict["Donor"]

r = requests.get(
    "http://vcm-7631.vm.duke.edu:5002/get_blood_type/{}".format(recipient_id))
recipient_btype = r.text

r = requests.get(
    "http://vcm-7631.vm.duke.edu:5002/get_blood_type/{}".format(donor_id))
donor_btype = r.text

# Create Blood matching function:


def blood_match(recipient, donor):
    blood_dict = {
        "A+": ["A+", "A-", "O+", "O-"],
        "A-": ["A-", "O-"],
        "B+": ["B+", "B-", "O+", "O-"],
        "B-": ["B-", "O-"],
        "AB+": ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
        "AB-": ["AB-", "A-", "B-", "O-"],
        "O+": ["O+", "O-"],
        "O-": ["O-"]
    }
    return "Yes" if donor in blood_dict[recipient] else "No"


# Check blood match
btype_match = blood_match(recipient_btype, donor_btype)
match_dict = {"Name": "nvg6", "Match": btype_match}
r = requests.post(
    "http://vcm-7631.vm.duke.edu:5002/match_check", json=match_dict)

# Printing
print("Recipeint ID: {}".format(recipient_id))
print("Recipient Blood Type: {}\n".format(recipient_btype))
print("Donor ID: {}".format(donor_id))
print("Donor Blood Type: {}\n".format(donor_btype))
print("Match? {}".format(btype_match))
print("Check Match with Servier: {}".format(r.text))
