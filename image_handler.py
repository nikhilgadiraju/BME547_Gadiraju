from tkinter import filedialog
import base64
import requests
import io
import matplotlib.image as mpimg
from matplotlib import pyplot as plt


def upload_image(net_id, id):
    filename = get_image_file_name()
    b64_string = convert_file_to_b64(filename)
    msg, stat_num = upload_b64_to_server(b64_string, net_id, id)
    if stat_num == 200:
        print("Image Succesfully Uploaded!")
        return True
    else:
        print(stat_num)
        print(msg)
        return False


def return_image(net_id, id):
    msg, stat = get_image_from_server(net_id, id)
    if stat == 200:
        img_arr = b64_to_ndarry(msg)
        plt.imshow(img_arr, interpolation='nearest')
        plt.show()
        return
    else:
        print(stat)
        print(msg)
        return


def get_image_file_name():
    filename = filedialog.askopenfilename()
    return filename


def convert_file_to_b64(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string


def upload_b64_to_server(b64_string, net_id, id):
    img_dict = {
        "image": b64_string,
        "net_id": net_id,
        "id_no": int(id)
    }
    r = requests.post("http://vcm-21170.vm.duke.edu/add_image", json=img_dict)
    return r.text, r.status_code,


def get_image_from_server(net_id, id):
    r = requests.get(
        "http://vcm-21170.vm.duke.edu/get_image/{}/{}".format(net_id, id))
    return r.text, r.status_code


def b64_to_ndarry(b64_string):
    image_bytes = base64.b64decode(b64_string)
    image_buf = io.BytesIO(image_bytes)
    img_ndarray = mpimg.imread(image_buf, format='JPG')
    return img_ndarray


if __name__ == "__main__":
    upload_result = upload_image("nvg6", 2)
    if upload_result:
        return_image("nvg6", 2)
