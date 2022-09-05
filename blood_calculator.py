#%% Function Definitions
# Define interface functino
def interface():
    print("Blood Calculator")
    print("Options:")
    print("1 - Analyze HDL")
    print("2 - Analyze LDL")
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

# Create HDL functions
def input_HDL():
    HDL_input = input("Enter the HDL value: ")
    return int(HDL_input)

def check_HDL(param):
    if param >= 60:
        return "Normal"
    elif 40 <= param < 60: # Technically we don't need to specify "<60"
        return "Borderline Low"
    else:
        return "Low"

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
        return "Very High"
    elif 160 <= param < 190:
        return "High"
    elif 130 <= param < 160:
        return "Borderline High"
    else:
        return "Normal"

def output_LDL_result(ldl_value, charac):
    print("The results for an LDL value of {} is {}".format(ldl_value, charac))

def LDL_driver(): # Driver functions essentially call other functions
    ldl_value = input_LDL()
    answer = check_LDL(ldl_value)
    output_LDL_result(ldl_value, answer)

#%% Function Calls
interface()