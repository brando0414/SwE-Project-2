import cv2
import os

inputFPS = 30
image_folder = "input_images"
output_video = "output.mp4"

def images_to_video(image_folder, output_video, fps=inputFPS):
    # Get a list of all JPEG images in the folder
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".jpeg")]
    images.sort()  # Sort images by filename to maintain order

    # Get dimensions of the first image
    first_image_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_image_path)
    height, width, _ = frame.shape

    # Define the video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for mp4
    video_writer = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    # Loop through images and write to video
    for image in images:
        image_path = os.path.join(image_folder, image)
        frame = cv2.imread(image_path)
        video_writer.write(frame)  # Add frame to video

    # Release the video writer
    video_writer.release()
    print(f"Video saved as {output_video}")

images_to_video(image_folder, output_video, inputFPS)
