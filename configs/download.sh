#!bin/sh
git clone "https://github.com/pythonlessons/TensorFlow-2.x-YOLOv3"
# mode to code directory
cd "./TensorFlow-2.x-YOLOv3"
# yolov3
wget -P model_data https://pjreddie.com/media/files/yolov3.weights
# yolov3-tiny
wget -P model_data https://pjreddie.com/media/files/yolov3-tiny.weights
# yolov4
wget -P model_data https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights
# yolov4-tiny

#Conda installation
#https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf
