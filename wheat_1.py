import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# import useful tools
from glob import glob
from PIL import Image
import cv2

# import data visualization
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns

# from bokeh.plotting import figure
# from bokeh.io import output_notebook, show, output_file
# from bokeh.models import ColumnDataSource, HoverTool, Panel
# from bokeh.models.widgets import Tabs

# import data augmentation
import albumentations as albu

#
# Setup the paths to train and test images
TRAIN_DIR = '../input/global-wheat-detection/train/'
TEST_DIR = '../input/global-wheat-detection/test/'
TRAIN_CSV_PATH = '../input/global-wheat-detection/train.csv'

# Glob the directories and get the lists of train and test images
train_fns = glob(TRAIN_DIR + '*')
test_fns = glob(TEST_DIR + '*')
