from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.train(
    data=r"C:\Users\User\Desktop\Phones\YOLODataset\dataset.yaml",
    epochs=100,
    imgsz=640
)