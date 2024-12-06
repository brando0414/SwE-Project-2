This repository contains all of our work for our Software Engineering Project 2
The team members are:
Nathan Johnson
Jacob Riley
Cory Thrutchley
Brandon Collings

This repository houses scripts to:
generate an object prediction model using all datasets contained in the "datasets" folder using model.py, 
validate the model using test images or videos in the root directory via test.py or using a webcam stream via the command "streamlit run testStream.py" in the Scripts directory,
and generate pydoc documentation for all scripts in the "Scripts" folder using pydoc_generation.py in the "documentation" folder.

This repository relies on the following dependencies:
ultralytics
roboflow
torch or pytorch
PIL or pillow

The listed dependecies above can be installed using "pip install <dependency_name>" with the exception of pytorch which will require special installation instructions found here: https://pytorch.org/

Our best runs so far are in "runs/detect/predict14" and our best model is in "runs/detect/train2".
