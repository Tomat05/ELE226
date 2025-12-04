import cv2
from facial_recognition import recognize_image, add_faces_from_folder

add_faces_from_folder(r"test_images")

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("[ERROR] Could not open webcam.")
    exit()

print("[INFO] Starting webcam face recognition... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Failed to grab frame.")
        break

    # Run face recognition (don't save output each frame)
    results = recognize_image(frame, save_output=False)

    # Draw results on frame
    for r in results:
        x, y, w, h = r["box"]
        H, W = frame.shape[:2]
        x1, y1 = int(x * W), int(y * H)
        x2, y2 = int((x + w) * W), int((y + h) * H)

        color = (0, 255, 0) if r["name"] != "Unknown" else (0, 0, 255)
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        label = f"{r['name']} ({r['score']:.2f})"
        cv2.putText(frame, label, (x1, max(20, y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    # Show the frame
    cv2.imshow("Webcam Face Recognition", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("[INFO] Webcam recognition stopped.")
