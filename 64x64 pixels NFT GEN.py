from PIL import Image

# Define image size
width = 64
height = 64

# Create a new image with the specified size and white background
img = Image.new("RGB", (width, height), color="white")

# Set the pixel colors in a checkerboard pattern
for x in range(width):
    for y in range(height):
        if (x + y) % 2 == 0:
            img.putpixel((x, y), (0, 0, 0))

# Save the image to a file
img.save("checkerboard.png")
