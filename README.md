# FER
Facial Emotion Recognition using PySpark.

This is a project exploring the realm of scalable emotion recognition, combining the `FER` and `PySpark` packages.

## Project Description
Emotion recognition and its possible faults, biases and implications are explored throughout two datasets and a variety of means within the notebooks of this project. `fer_code.ipynb` includes the main crux of the project, explains the use of both the `FER` and `PySpark` packages and how they are utilised in the process, as well as going into colour bias and picture resizing in the use of facial recognition.

The results are presented in the form of a confusion matrix, which evaluates the scalable model on the FER dataset from kaggle, accompanied with many more accuracy metrics, such as precision and recall.

The other files go into details, `lime.ipynb` tries to investigate the possible biases of the model, while `resizing.ipynb` explains the role of resizing in improving model accuracy. 

The files are to be used together as laid out in this repository.

Special thanks goes to the team-mates who have worked with me on this project: Denix Hoxha, Mateusz Szewczyk and Sara Ademović.

## Copyright

[1] Vemulapalli R., Agarwala A. (2018). Google facial expression comparison dataset. Retrieved on January 2, 2022, from https://research.google/tools/datasets/google-facial-expression/

[2] Sambare, M. (2020, July 19). FER-2013 Dataset. Retrieved on January 2, 2022, from https://www.kaggle.com/msambare/fer2013

[3] Shenk J., (2018). Facial Expression Recognition. Retrieved January 2, 2022, from https://github.com/justinshenk/fer/blob/master/src/fer/fer.py
