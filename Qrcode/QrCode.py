import os
from natsort import natsorted, ns
from qrtools import QR

path = "/home/n3rd/Downloads/ctf/unz"
os.chdir(path)

def decodz(file_path):
    QRz=QR(filename=file_path)
    QRz.decode()
    res = QRz.data
    res2 = " ".join(res.splitlines())
    print(res2)

#file_list = []
file_list = os.listdir()
file_list = natsorted(file_list, alg=ns.PATH | ns.IGNORECASE)
for file in file_list:
    if file.endswith(".gif"):
        file_path = f"{path}/{file}"
        decodz(file_path)