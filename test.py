from ultralytics import YOLO

model = YOLO(r"C:\Users\User\Desktop\Phones\runs\detect\train-2\weights\best.pt")

results = model(r"C:\Users\User\Desktop\Phones\IMG_2943.jpg")

results[0].show()