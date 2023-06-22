# imports ##############################################################################################################
import cv2

# preprocess the sky image #############################################################################################
def image_preprocess(image_path):
    image = cv2.imread(image_path)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image, image_gray

# Load the sky image, You can also use live image ######################################################################
image_path = "Images/image2.jpg"
image, image_gray = image_preprocess(image_path)

# apply grayscale on the loaded image,and detact edges #################################################################
def image_detect_edges(gray_img):
    edges = cv2.Canny(gray_img, 30, 150)
    return edges

edges = image_detect_edges(image_gray)

# Perform contour detection on the edges ###############################################################################
def image_detect_contours(edges):
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

contours = image_detect_contours(edges)

# Find the sky condition based on the number of edge contours ##########################################################
def detect_sky_condition(contours):
    
    if len(contours) < 10:
        condition = "Clear sky"
    elif len(contours) < 63:
        condition = "Partly cloudy"
    elif len(contours) < 90:
        condition = "Cloudy"
    else:
        condition = "Rainy"
    return condition


# Run ##################################################################################################################
if __name__ == "__main__":
    condition = detect_sky_condition(contours)
    print("Sky condition is:", condition)
