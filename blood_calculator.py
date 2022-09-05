#%% Function Definitions
# Define interface functino
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
def input_HDL():
    HDL_input = input("Enter the HDL value: ")
    return int(HDL_input)

def check_HDL(param):
    if param >= 60:
        return "normal"
    elif 40 <= param < 60: # Technically we don't need to specify "<60"
        return "borderline low"
    else:
        return "low"

def output_HDL_result(hdl_value, charac):
    print("The results for an HDL value of {} is {}".format(hdl_value, charac))

def HDL_driver(): # Driver functions essentially call other functions
    hdl_value = input_HDL()
    answer = check_HDL(hdl_value)
    output_HDL_result(hdl_value, answer)

# Create LDL functions
def input_LDL():
    LDL_input = input("Enter the LDL value: ")
    return int(LDL_input)

def check_LDL(param):
    if param >= 190:
        return "very high"
    elif 160 <= param < 190:
        return "high"
    elif 130 <= param < 160:
        return "borderline high"
    else:
        return "normal"

def output_LDL_result(ldl_value, charac):
    print("The results for an LDL value of {} is {}".format(ldl_value, charac))

def LDL_driver(): # Driver functions essentially call other functions
    ldl_value = input_LDL()
    answer = check_LDL(ldl_value)
    output_LDL_result(ldl_value, answer)

# Create Total Cholesterol Check
def input_totchol():
    LDL_input = input("Enter the Total Cholesterol value: ")
    return int(LDL_input)

def check_totchol(param):
    if param >= 240:
        return "high"
    elif 200 <= param < 240:
        return "borderline high"
    else:
        return "normal"

def output_totchol_result(totchol_value, charac):
    print("The results for a Total Cholesterol value of {} is {}".format(totchol_value, charac))

def totchol_driver(): # Driver functions essentially call other functions
    totchol_value = input_totchol()
    answer = check_totchol(totchol_value)
    output_totchol_result(totchol_value, answer)

#%% Function Calls
interface()