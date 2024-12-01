import cv2
import os

# load input mp4 file
cap = cv2.VideoCapture('input.mp4')

fps = 30  # frame rate of input video
quality = 0.5  # desired image quality (0-1, will affect process time)

# create directory to store decompiled images
img_dir = 'output_images'
os.makedirs(img_dir, exist_ok=True)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame to fixed size (optional)
    # frame = cv2.resize(frame, (640, 480))

    # Encode frame as JPEG image
    frameNum = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
    img_path = os.path.join(img_dir, f'frame_' + f'{frameNum:07d}.jpg')
    cv2.imwrite(img_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), int(quality * 100)])

cap.release()
