import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2
import glob
#from skimage.feature import hog
#from skimage import color, exposure
# images are divided up into vehicles and non-vehicles


# Define a function to return some characteristics of the dataset 
def data_look():
    car_images = glob.glob('../../data/vehicles/KITTI_extracted/*.png')
    not_car_images = glob.glob('../../data/non-vehicles/GTI/*.png')
    not_car_extra_images = glob.glob('../../data/non-vehicles/Extras/*.png')
    cars = []
    notcars = []
    for image in car_images:
        cars.append(image)
    for image in not_car_images:
        notcars.append(image)
    for image in not_car_extra_images:
        notcars.append(image)
    data_dict = {}
    # Define a key in data_dict "n_cars" and store the number of car images
    data_dict["n_cars"] = len(cars)
    # Define a key "n_notcars" and store the number of notcar images
    data_dict["n_notcars"] = len(notcars)
    # Read in a test image, either car or notcar
    # Define a key "image_shape" and store the test image shape 3-tuple
    img = cv2.imread(cars[0])
    data_dict["image_shape"] = img.shape
    # Define a key "data_type" and store the data type of the test image.
    data_dict["data_type"] = img.dtype
    # Return data_dict
    return data_dict, cars, notcars
