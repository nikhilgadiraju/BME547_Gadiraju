def create_patient_entry(patient_first_name,
                         patient_last_name,
                         patient_id, patient_age):
    new_patient = {"First Name": patient_first_name,
                   "Last Name": patient_last_name,
                   "Id": patient_id,
                   "Age": patient_age,
                   "Tests": []}
    return new_patient

def data_print(db):
    for patients in db:
        print("{:15}{:<5}{:<5}".format(get_full_name(db[patients]),
                                       db[patients]["Id"],
                                       db[patients]["Age"]))

def get_full_name(patient):
    full_name = "{} {}".format(patient["First Name"], patient["Last Name"])
    return full_name

def find_patient(db, id_no):
    patient = db[id_no]
    return patient

def tests(db, id_no, test_name, test_val):
    patient = find_patient(db, id_no)
    patient['Tests'].append((test_name, test_val))

def adult_or_minor(patient):
    if patient["Age"] >= 18:
        return 'adult'
    else:
        return 'minor'

def main():
    db = {}
    db[11] = create_patient_entry("Ann", "Ables", 1, 30)
    db[22] = create_patient_entry("Bob", "Boyles", 2, 34)
    db[3] = create_patient_entry("Chris", "Chou", 3, 25)
    data_print(db)
    tests(db, 3, "HDL", 100)
    print(find_patient(db, 3))
    #print("Patient {} is a {}".format(get_full_name(db[2]),
    #                                  adult_or_minor(db[2])))

if __name__ == "__main__":
    main()