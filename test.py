from ultralytics import YOLO

model = YOLO("runs/detect/train2/weights/best.pt")
model.predict("WIN_20241203_22_28_06_Pro.jpg", conf=0.4, save=True)