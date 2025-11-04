from images import Image

def grayscale(image):
    """Converts the argument image to grayscale."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            gray = int((r + g + b) / 3)
            image.setPixel(x, y, (gray, gray, gray))

def sepia(image):
    """Converts the argument image to sepia."""

    grayscale(image)

    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)

            if r < 63:
                r = int(r * 1.1)
                b = int(b * 0.9)
            elif r < 192:
                r = int(r * 1.15)
                b = int(b * 0.85)
            else:
                r = int(min(r * 1.08, 255))
                b = int(b * 0.93)

                image.setPixel(x, y, (r, g, b))

def main():
    image = Image("smokey.gif")
    sepia(image)
    image.draw()

if __name__ == "__main__":
    main()
