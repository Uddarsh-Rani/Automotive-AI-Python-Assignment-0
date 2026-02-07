import cv2
import random

VIDEO_PATH = r"D:\Educational_space\SIT_Pune\SEM_2\AutomotiveAI\pyhton assigment 0\WhatsApp Video 2026-02-07 at 16.00.48.mp4"
OUTPUT_PATH = r"D:\Educational_space\SIT_Pune\SEM_2\AutomotiveAI\pyhton assigment 0\output_video.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Codec and VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(OUTPUT_PATH, fourcc, fps, (width, height))

frame_count = 0
random_text = "Rani Uddarsh 25070152008"

rand_x, rand_y = 50, 100

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape

    if frame_count % 30 == 0:

        (text_width, text_height), _ = cv2.getTextSize(
            random_text,
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            2
        )

        rand_x = random.randint(0, max(1, width - text_width))
        rand_y = random.randint(text_height, max(text_height + 1, height - 60))

    # Random Text
    cv2.putText(frame,
                random_text,
                (rand_x, rand_y),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (227, 193, 20),
                2,
                cv2.LINE_AA)

    # Bottom Ribbon
    ribbon_text = "python assignment, version 0"
    ribbon_height = 50

    cv2.rectangle(frame,
                  (0, height - ribbon_height),
                  (width, height),
                  (0, 0, 0),
                  -1)

    cv2.putText(frame,
                ribbon_text,
                (20, height - 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2,
                cv2.LINE_AA)

    # ✅ WRITE FRAME TO VIDEO
    out.write(frame)

    cv2.imshow("Video", frame)

    if cv2.waitKey(30) & 0xFF == 27:
        break

    frame_count += 1

cap.release()
out.release()   # VERY IMPORTANT
cv2.destroyAllWindows()

print("Video saved successfully!")
