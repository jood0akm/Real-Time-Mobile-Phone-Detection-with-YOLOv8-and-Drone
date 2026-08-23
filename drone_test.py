from ultralytics import YOLO
from djitellopy import Tello
import cv2
import time

model = YOLO(r"C:\Users\User\Desktop\Phones\runs\detect\train-3\weights\best.pt")

drone = Tello()
drone.connect()
print(f"البطارية: {drone.get_battery()}%")

drone.streamon()

frame = drone.get_frame_read().frame
cv2.imshow("Tello Camera", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
cv2.waitKey(1)

drone.takeoff()
drone.move_up(80)

last_keepalive = time.time()

while True:
    frame = drone.get_frame_read().frame
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    results = model.predict(frame, conf=0.5, verbose=False)
    annotated = results[0].plot()
    cv2.imshow("Tello Camera", annotated)

    # يرسل أمر كل 5 ثواني عشان يخلي الاتصال حي ومايفكر الدرون انقطع
    if time.time() - last_keepalive > 5:
        drone.send_rc_control(0, 0, 0, 0)
        last_keepalive = time.time()

    if cv2.waitKey(1) & 0xFF == 32:
        break

drone.land()
drone.streamoff()
cv2.destroyAllWindows()
