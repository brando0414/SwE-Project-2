
# from roboflow import Roboflow

# ROBOFLOW_API_KEY ='3Blxz6aswzjyShfdBHjk'
# rf = Roboflow(api_key=ROBOFLOW_API_KEY)

# workspace = rf.workspace("swe-project-2")
# project = workspace.project("swe-project-2")
# version = project.version(7)
# dataset = version.download("yolov11")
# !yolo task=detect mode=train model=yolo11s.pt data= "C:\Users\brand\Documents\GitHub\SwE-Project-2\SwE-Project-2-5\data.yaml" epochs=100 imgsz=640 plots=True

from ultralytics import YOLO
import torch
print(torch.cuda.is_available())
model = YOLO("../runs/detect/train/weights/best.pt")

# force to run on CPU by using device flag
#results = model.predict(source="0", show=True, stream=True, classes=0, device='gpu')
# train on GPU 1
if __name__ == "__main__":
    model.train(data="../datasets/SwE-Project-2-7/data.yaml", epochs=250, imgsz=640, device=0)