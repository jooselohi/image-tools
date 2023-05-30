import sys
from PIL import Image

def square_image(image):
    width, height = image.size
    max_dim = max(width, height)
    new_image = Image.new('RGBA', (max_dim, max_dim), (0, 0, 0, 0))
    offset = ((max_dim - width) // 2, (max_dim - height) // 2)
    new_image.paste(image, offset)
    return new_image

def resize_image(image, size):
    return image.resize(size)

if len(sys.argv) != 2:
    print("Usage: python3 favicon.py <image_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = "favicon.png"
output_size = (32, 32)

try:
    # Open the input image
    with Image.open(input_file) as image:
        # Convert image to square
        square = square_image(image)

        # Resize the square image
        resized = resize_image(square, output_size)

        # Save the resized image
        resized.save(output_file)
        print(f"Saved favicon as {output_file}")

except IOError:
    print(f"Unable to open or process {input_file}")
