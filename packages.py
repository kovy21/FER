# Packages necessary:
#import sys
#pip install tensorflow
#pip install FER

import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tensorflow']) # tensorflow for keras models 
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'FER']) # facial recognition
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'opencv-python']) # facial recognition