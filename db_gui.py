import tkinter as tk
from tkinter import ttk
import db_client
from PIL import Image, ImageTk
from tkinter import filedialog


def create_blood_type(letter, rh):
    output = "{}{}".format(letter, rh)
    return output


def upload_data_to_server(patient_name, patient_id, patient_blood_letter,
                          patient_rh_factor):
    blood_type = create_blood_type(patient_blood_letter, patient_rh_factor)
    msg, code = db_client.upload_patient_info(
        patient_name, int(patient_id), blood_type)
    return msg


def main_window():

    def ok_cmd():
        # Get data from interface
        if rh_button.get() == "":
            print("Choose a Rh factor")
            return
        patient_name = patient_name_entry.get()
        patient_id = patient_id_entry.get()
        patient_blood_letter = blood_letter_selection.get()
        patient_rh_factor = rh_button.get()

        # Call other testable functinos to do all the work
        msg = upload_data_to_server(patient_name, patient_id,
                                    patient_blood_letter, patient_rh_factor)

        # Update GUI based on results of other functions
        status_label.configure(text=msg)

    def cancel_cmd():
        root.destroy()

    def picture_button_cmd():
        # Will only test with JPG images
        new_file = "Images/blue_devil.jpg"
        new_file = filedialog.askopenfilename()
        print("Filename: {}".format(new_file))
        pil_image = Image.open(new_file)
        x_size, y_size = pil_image.size
        new_y = 100
        new_x = new_y * (x_size/y_size)
        pil_image = pil_image.resize((round(new_x), round(new_y)))
        tk_image = ImageTk.PhotoImage(pil_image)
        image_label.configure(image=tk_image)
        # Anytime an image is added to a label, always create the '.image'
        # attribute so Python doesn't discard the 'tk_image' defined within
        # this function locally
        # Adding new attribute to the class ttk label
        image_label.image = tk_image

    root = tk.Tk()
    root.title("Blood Donor Database")
    # root.geometry("600x300")

    # sticky is based on "n", "s", "e", "w", and even northwest and other
    # directions ("nw"). Can also use tk version (tk.W)
    ttk.Label(root, text="Blood Donor Database").grid(column=0, row=0,
                                                      columnspan=2, sticky=tk.W)
    ttk.Label(root, text="Name:").grid(column=0, row=1)

    # This special variable can be connected to a GUI widget to get information
    # in and out of a widget
    patient_name_entry = tk.StringVar()

    # Default size of 30 characters
    ttk.Entry(root, width=50, textvariable=patient_name_entry).grid(
        column=1, row=1, sticky=tk.W)

    ttk.Label(root, text="ID:").grid(column=0, row=2, sticky=tk.E)
    patient_id_entry = tk.StringVar()
    ttk.Entry(root, textvariable=patient_id_entry).grid(
        column=1, row=2, sticky=tk.W)

    blood_letter_selection = tk.StringVar()
    ttk.Radiobutton(root, text="A", variable=blood_letter_selection,
                    value="A").grid(column=0, row=3, sticky=tk.W)
    ttk.Radiobutton(root, text="B", variable=blood_letter_selection,
                    value="B").grid(column=0, row=4, sticky=tk.W)
    ttk.Radiobutton(root, text="AB", variable=blood_letter_selection,
                    value="AB").grid(column=0, row=5, sticky=tk.W)
    ttk.Radiobutton(root, text="O", variable=blood_letter_selection,
                    value="O").grid(column=0, row=6, sticky=tk.W)

    rh_button = tk.StringVar()
    ttk.Checkbutton(root, text="Rh Positive?", variable=rh_button,
                    onvalue='+', offvalue='-').grid(column=1, row=4)

    ttk.Label(root, text="Closest Donation Center").grid(column=2, row=0)
    donor_center = tk.StringVar()
    donor_center_combo = ttk.Combobox(root, textvariable=donor_center)
    donor_center_combo.grid(column=2, row=1)
    donor_center_combo["values"] = ["Durham", "Cary", "Raleigh"]
    donor_center_combo.state(["readonly"])

    ttk.Button(root, text="Ok", command=ok_cmd).grid(column=1, row=7)
    ttk.Button(root, text="Cancel", command=cancel_cmd).grid(
        column=2, row=6, sticky=tk.E)

    other_button = ttk.Button(root, text="Other", state=tk.DISABLED)
    other_button.grid(column=2, row=7, sticky=tk.E)

    picture_button = ttk.Button(
        root, text="Load Picture", command=picture_button_cmd)
    picture_button.grid(column=2, row=8)

    status_label = ttk.Label(root, text="Status")
    status_label.grid(column=0, row=8)

    pil_image = Image.open("Images/blank_pic.jpg")
    pil_image = pil_image.resize((100, 100))
    tk_image = ImageTk.PhotoImage(pil_image)
    image_label = ttk.Label(root, image=tk_image)
    image_label.image = tk_image
    image_label.grid(column=1, row=8)

    root.mainloop()


if __name__ == "__main__":
    main_window()
