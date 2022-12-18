import cv2
import glob

# Create a list of all the images in the folder
image_list = glob.glob('*.jpg')

for image_path in image_list:
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find the non-zero min and max y-coordinates
    ys = np.where(gray != 0)[0]
    y_min, y_max = ys[0], ys[-1]

    # Find the non-zero min and max x-coordinates
    xs = np.where(gray != 0)[1]
    x_min, x_max = xs[0], xs[-1]

    # Crop the image
    cropped_image = image[y_min:y_max+1, x_min:x_max+1]

    # Save the cropped image
    cv2.imwrite(image_path, cropped_image)
