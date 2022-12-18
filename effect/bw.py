import os
from PIL import Image

# Get a list of all the image files in the current directory
image_files = [f for f in os.listdir('.') if f.endswith('.jpg') or f.endswith('.png')]

# Print the list of image files
print("Image files in the current directory:")
for i, f in enumerate(image_files):
    print(f"{i+1}. {f}")

# Prompt the user to choose an image file
choice = input("Enter the number of the image file you want to convert to grayscale (or press enter to exit): ")

# Check if the user wants to exit
if choice == "":
    exit()

# Convert the choice to an integer
choice = int(choice)

# Get the selected image file
filename = image_files[choice-1]

# Open the image file
image = Image.open(filename)

# Convert the image to grayscale
image = image.convert('L')

# Save the grayscale image
image.save("bw_"+filename)
