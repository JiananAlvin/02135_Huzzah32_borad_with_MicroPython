import os

os.chdir()
path = "D:/development/development_lib/VirtualMachine/hole_detection_yolov5.v1i.yolov5pytorch/test/labels"

for file in os.listdir(path):
    print(file)
