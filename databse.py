def create_patient_entry(patient_name, patient_id, patient_age):
    new_patient = [patient_name, patient_id, patient_age, []]
    return new_patient

def data_print(db):
    print("{:15}{:5}{:5}".format("Name", "ID", "Age"))
    for patients in db:
        print("{:15}{:<5}{:<5}".format(patients[0], patients[1], patients[2]))

def find_patient(db, id_no):
    for patient in db:
        if patient[1] == id_no:
            return patient
    return False

def tests(db, id_no, test_name, test_val):
    patient = find_patient(db, id_no)
    patient[3].append((test_name, test_val))

def main():
    db = []
    db.append(create_patient_entry("Ann Ables", 1, 30))
    db.append(create_patient_entry("Bob Boyles", 2, 34))
    db.append(create_patient_entry("Chris Chou", 3, 25))
    tests(db, 3, "HDL", 100)
    print(find_patient(db, 3))

    room_list = ["Room 1", "Room 2", "Room 3"]
    for i, patient in enumerate(db):
        print("Name = {}, Room = {}".format(patient[0], room_list[i]))

    # Alternatively
    for patient, room in zip(db, room_list):
        print("Name = {}, Room = {}".format(patient[0], room))

if __name__ == "__main__":
    main()