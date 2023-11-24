import cv2

# Specify the path to your image file
image_path = 'C://Passports/Newzealand.jpg'  # Replace with the actual path to your image

# Read the image
image = cv2.imread(image_path)

# Check if the image is successfully loaded
if image is not None:
    # Display the image
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("done")
    
else:
    print(f"Error: Unable to read the image from {image_path}")
