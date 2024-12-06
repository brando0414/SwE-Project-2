from roboflow import Roboflow
from PIL import Image, ImageDraw, ImageFont
import os
from videoToImages.videoDecomplier import video_to_images
from imagesToVideo.videoCompiler import images_to_video
from ultralytics import YOLO
import torch

# # Initialize Roboflow
# rf = Roboflow(api_key="3Blxz6aswzjyShfdBHjk")
# project = rf.workspace().project("swe-project-2")
# model = project.version(5).model
model = YOLO("../runs/detect/train4/weights/best.pt")

def predict(input_image, output_image, con=0.40, ovl=30):
    # Make predictions
    predictions = model.predict(input_image, conf=con, save=True)

    # Load the image
    image = Image.open(input_image)
    # draw = ImageDraw.Draw(image)

    # # Define font for annotation (adjust size if necessary)
    # try:
    #     font = ImageFont.truetype("arial.ttf", 20)  # Adjust font size here
    # except IOError:
    #     # Fallback font if the specified one is unavailable
    #     font = ImageFont.load_default()

    # # Draw bounding boxes and add confidence scores
    # for prediction in predictions['predictions']:
    #     x, y, width, height = prediction['x'], prediction['y'], prediction['width'], prediction['height']
    #     confidence = prediction['confidence']
    #     label = prediction['class']

    #     # Calculate bounding box coordinates
    #     x0 = int(x - width / 2)
    #     y0 = int(y - height / 2)
    #     x1 = int(x + width / 2)
    #     y1 = int(y + height / 2)

    #     # Draw rectangle
    #     draw.rectangle([x0, y0, x1, y1], outline="red", width=2)

    #     # Add label and confidence outside the box (slightly above or below)
    #     text = f"({confidence:.2f}) {label}"
    #     text_width, text_height = font.getbbox(text)[2:4]  # Updated method for text size calculation

    #     # Position the text above the box if there's enough space; otherwise, below
    #     if y0 - text_height - 5 > 0:
    #         text_position = (x0, y0 - text_height + 20)  # Above the box
    #     else:
    #         text_position = (x0, y1 - 20)  # Below the box

    #     # Draw text background to enhance readability
    #     draw.rectangle(
    #         [
    #             (text_position[0], text_position[1]),
    #             (text_position[0] + text_width, text_position[1] + text_height),
    #         ],
    #         fill="white",
    #     )

    #     # Add text
    #     draw.text(text_position, text, fill="red", font=font)

    # Convert image to RGB mode to save as JPEG
    image = image.convert("RGB")

    # Save the annotated image
    image.save(output_image)

    # print("Annotated image saved as 'annotated_prediction.jpg'")

# convert pikachu mp4 into individual images in the pikachu_vid_images directory
folder_path = "pikachu_vid_images"
video_to_images("../demoVideos/pikachu_vid.mp4", folder_path, 1)

# run a prediction on every frame/image and put them in the predicted_output_images directory
file_num = 0
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):  # Check if it's a file
        file_num += 1
        predict(folder_path + "/" + file_name,
                "predicted_output_images/" + f'prediction_' + f'{file_num:05d}.jpg', 0.40, 30)

# convert those predicted images in the predicted_output_images directory back into a video (mp4)
images_to_video("runs/detect/predict", "predicted_output_video.mp4", 30)

# predict("pika.jpg", "predicted_output_images/annotated_prediction.jpg", 40, 30)