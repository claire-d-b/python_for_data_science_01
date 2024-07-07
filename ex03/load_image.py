from PIL import Image

def ft_load(path: str) -> bytearray:
    try:
        assert Image.open(path), "Error: failed to open file"
        image = Image.open(path)
        barray = []

        width, height = image.size

        for x in range(width):
            for y in range(height):
                r, g, b = image.getpixel((x, y))
                barray.append([r, g, b])
        barray.append([r, g, b])
        
        string = "The shape of image is: "
        items = image.getpixel((0,0))
        i = 0
        for item in items:
            i += 1
        print(string, (height, width, i))
        print([barray])
    except AssertionError as e:
        print(f"AssertionError: {e}")

    # In Python, the // operator is used for integer (floor) division.
    # This means it divides the number on its left by the number on its right and then rounds down to the nearest integer.
    # Example: Simple integer division
    # result = 7 // 2 Output: 3

    output_image_path = "zoom.jpeg"
    
    # Specify the zoom factor (adjust as needed)
    # Zoom factor > 1 zooms in, < 1 zooms out
    factor = 1.5

    nwidth, nheight = 400, 400

    # Calculate the cropping box
    center_x, center_y = width // 2, height // 2

    if width < height:
        right, bottom = width / factor, width / factor
    else:
        right, bottom = height / factor, height / factor
    
    # Crop the image to the calculated box
    cropped_image = image.crop((0, 0, right, bottom))
    
    # Resize the cropped image back to the original dimensions
    zoomed_image = cropped_image.resize((nwidth, nheight), Image.LANCZOS)
    
    # Save the zoomed image
    zoomed_image.save(output_image_path)

    npath = output_image_path

    try:
        assert Image.open(npath), "Error: failed to open file"
        nimage = Image.open(npath)
        nbarray = []
        
        for x in range(nwidth):
            for y in range(nheight):
                r, g, b = nimage.getpixel((x, y))
                nbarray.extend([r, g, b])
        nbarray.extend([r, g, b])

    except AssertionError as e:
        print(f"AssertionError: {e}")
    string = "New shape after slicing: "

    print(string, (nheight, nwidth, 1), " or ", (nheight, nwidth))

    return nbarray