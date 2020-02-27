# Smear-Detection 

1  Chirag Khandar
2. AKSHAY KULKARNI

## Aproach

1. Implement Single Image Transformation on the sequence of input images by applying grayscale, threshold, dilating the image and use Canny Edge detector for edge detection of the object.
2. Implement Image Accumulation on the resultant images of the previous step.
3. Repeat the same accumulation process for every N=500 images for the example taken.
4. The next step is to post process the accumulated images to clean the pictures from the artifacts by opening, blurring, applying threshold and contours to the image.
5. The next step is Selecting + Normalizing the retained contours.
6. The final step is to clean up the final result by finding the maximum retained pixel value and applying threshold using this maximum value- tolerance.


## How to Run

* This script works with Python 3.8 or above.
* Install the following packages
  * `numpy`
  * `cv2`
  * `glob`
* We've used Anaconda IDE (Spyder).
* Run the `main.py` by pressing run button or if you are using Command Prompt use `python main.py`
* The script makes use of 5 folders named `cam_0`, `cam_1`, `cam_2`, `cam_3`, `cam_5` which contains aprroximately 4000 images per folder (folder name = sample_drive).
* So we are giving the path of `sample_drive` as input path when prompted and same path for output path when prompted.
* That's all, now just wait for the processing to be done.
* *PS. My PC with i5 6th Gen Processor, 8 Gigs RAM took 49.81 mins!*
