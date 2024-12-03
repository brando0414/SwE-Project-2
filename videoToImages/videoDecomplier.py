import cv2
import os

def video_to_images(video_path, output_dir, quality=0.5):
    # NOTE: desired image quality is from 0-1, will affect process time

    # load input mp4 file
    cap = cv2.VideoCapture(video_path)

    # create directory to store decompiled images
    os.makedirs(output_dir, exist_ok=True)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Optional: resize frame to fixed size
        # frame = cv2.resize(frame, (640, 480))

        # Encode frame as JPEG image
        frame_num = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        img_path = os.path.join(output_dir, f'frame_' + f'{frame_num:07d}.jpg')
        cv2.imwrite(img_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), int(quality * 100)])

    cap.release()

# example usage
video_to_images('input.mp4', 'output_images', 0.5)