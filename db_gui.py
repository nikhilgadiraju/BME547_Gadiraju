import tkinter as tk
from tkinter import ttk


def main_window():

    def ok_cmd():
        other_button.configure(state=tk.NORMAL)
        if rh_button.get() == "":
            print("Choose a Rh factor")
            return
        print("Patient name: {}".format(patient_name_entry.get()))
        print("Patient ID: {}".format(patient_id_entry.get()))
        print("Blood type: {}{}".format(
            blood_letter_selection.get(), rh_button.get()))
        print("Donation Center: {}".format(donor_center.get()))
        print("Clicked Ok button")

    def cancel_cmd():
        root.destroy()

    root = tk.Tk()
    root.title("Blood Donor Database")
    # root.geometry("600x300")

    ttk.Label(root, text="Blood Donor Database").grid(column=0, row=0,
                                                      columnspan=2)
    ttk.Label(root, text="Name:").grid(column=0, row=1)

    # This special variable can be connected to a GUI widget to get information
    # in and out of a widget
    patient_name_entry = tk.StringVar()

    # Default size of 30 characters
    ttk.Entry(root, width=50, textvariable=patient_name_entry).grid(
        column=1, row=1)

    ttk.Label(root, text="ID:").grid(column=0, row=2)
    patient_id_entry = tk.StringVar()
    ttk.Entry(root, textvariable=patient_id_entry).grid(
        column=1, row=2)

    blood_letter_selection = tk.StringVar()
    ttk.Radiobutton(root, text="A", variable=blood_letter_selection,
                    value="A").grid(column=0, row=3)
    ttk.Radiobutton(root, text="B", variable=blood_letter_selection,
                    value="B").grid(column=0, row=4)
    ttk.Radiobutton(root, text="AB", variable=blood_letter_selection,
                    value="AB").grid(column=0, row=5)
    ttk.Radiobutton(root, text="O", variable=blood_letter_selection,
                    value="O").grid(column=0, row=6)

    rh_button = tk.StringVar()
    ttk.Checkbutton(root, text="Rh Positive?", variable=rh_button,
                    onvalue='+', offvalue='-').grid(column=1, row=4)

    ttk.Label(root, text="Closest Donation Center").grid(column=2, row=0)
    donor_center = tk.StringVar()
    donor_center_combo = ttk.Combobox(root, textvariable=donor_center)
    donor_center_combo.grid(column=2, row=1)
    donor_center_combo["values"] = ["Durham", "Cary", "Raleigh"]
    donor_center_combo.state(["readonly"])

    ttk.Button(root, text="Ok", command=ok_cmd).grid(column=1, row=6)
    ttk.Button(root, text="Cancel", command=cancel_cmd).grid(column=2, row=6)

    other_button = ttk.Button(root, text="Other", state=tk.DISABLED)
    other_button.grid(column=2, row=7)

    root.mainloop()


if __name__ == "__main__":
    main_window()
