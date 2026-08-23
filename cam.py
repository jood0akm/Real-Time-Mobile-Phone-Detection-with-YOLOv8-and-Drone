print("بدأ التشغيل...")

from ultralytics import YOLO

print("تم استيراد YOLO")

model = YOLO(r"C:\Users\User\Desktop\Phones\runs\detect\train-3\weights\best.pt")

print("تم تحميل الموديل، جاري فتح الكاميرا...")

model.predict(source=0, show=True, conf=0.5)

print("انتهى")
