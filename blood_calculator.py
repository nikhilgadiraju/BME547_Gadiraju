#%% Function Definitions
# Define interface function
def interface():
    print("Blood Calculator")
    print("Options:")
    print("1 - Analyze HDL")
    print("2 - Analyze LDL")
    print("3 - Total Cholesterol Check")
    print("9 - Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter choice: ")
        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            totchol_driver()

# Create HDL functions
def input_val(label):
    input_val = input("Enter the {} value: ".format(label))
    return int(input_val)

def check_HDL(param):
    if param >= 60:
        return "normal"
    elif 40 <= param < 60: # Technically we don't need to specify "<60"
        return "borderline low"
    else:
        return "low"

def output_result(label, value, charac):
    print("The results for {} value of {} is {}".format(label, value, charac))

def HDL_driver(): # Driver functions essentially call other functions
    hdl_value = input_val("HDL")
    answer = check_HDL(hdl_value)
    output_result("an HDL",hdl_value, answer)

# Create LDL functions
def check_LDL(param):
    if param >= 190:
        return "very high"
    elif 160 <= param < 190:
        return "high"
    elif 130 <= param < 160:
        return "borderline high"
    else:
        return "normal"


def LDL_driver(): # Driver functions essentially call other functions
    ldl_value = input_val("LDL")
    answer = check_LDL(ldl_value)
    output_result("an LDL",ldl_value, answer)

# Create Total Cholesterol Check
def check_totchol(param):
    if param >= 240:
        return "high"
    elif 200 <= param < 240:
        return "borderline high"
    else:
        return "normal"

def totchol_driver(): # Driver functions essentially call other functions
    totchol_value = input_val("Total Cholesterol")
    answer = check_totchol(totchol_value)
    output_result("a total cholesterol", totchol_value, answer)

#%% Function Calls
interface()