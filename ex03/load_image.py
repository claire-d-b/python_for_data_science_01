from PIL import Image
import io

def ft_load(path: str) -> bytearray:
    image = None
    width, height = 0, 0
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

        # In Python, the // operator is used for integer (floor) division.
        # This means it divides the number on its left by the number on its right and then rounds down to the nearest integer.
        # Example: Simple integer division
        # result = 7 // 2 Output: 3

        # output_image_path = "zoom.jpg"
        
        # Specify the zoom factor (adjust as needed)
        # scale = 2.0  # Zoom factor > 1 zooms in, < 1 zooms out

        # Calculate the cropping box
        # center_x, center_y = width // 2, height // 2
        # crop_width, crop_height = int(width // scale), int(height // scale)
        
        # left = max(center_x - crop_width // 2, 0)
        # top = max(center_y - crop_height // 2, 0)
        # right = min(center_x + crop_width // 2, width)
        # bottom = min(center_y + crop_height // 2, height)
        
        # Crop the image to the calculated box
        # cropped_image = image.crop((left, top, right, bottom))

        # nwidth, nheight = 400, 400
        
        # Resize the cropped image back to the original dimensions
        # zoomed_image = cropped_image.resize((nwidth, nheight), Image.LANCZOS)

        # image.thumbnail((nwidth, nheight), Image.LANCZOS)

        # nwidth, nheight = image.size
        
        # Save the zoomed image
        # image.save(output_image_path)
        npath = "zoom.jpeg"
        nsize = (400, 400)
        nwidth, nheight = 400, 400
        assert Image.open(path), "Unable to open image"
        nimage = Image.open(path)
        print("IMAGE :", nimage)
        # assert Image.open(path), "Error: failed to open file"
        # nimage = Image.open(path)

        coeff_1 = float(nwidth / width)
        coeff_2 = float(nheight / height)

        print("coeff : ", coeff_1)
        print("coeff : ", coeff_2)

        crop_box = (0, 0, width * coeff_1, height * coeff_2)
        cropped_region = nimage.crop(crop_box)
        print("IMAGE CROP :", cropped_region)
        print("SIZE", cropped_region.size)

        # Calculate new dimensions after zooming
        # cropped_width, cropped_height = cropped_region.size
        # nwidth = int(cropped_width * zoom_factor)
        # nheight = int(cropped_height * zoom_factor)
        # Zoom (resize) the cropped region

        zoomed_region = cropped_region.resize(nsize, Image.LANCZOS)
        print("IMAGE ZOOM :", zoomed_region)

        # Save or display the zoomed and cropped image
        zoomed_region.save(npath)

        nwidth, nheight = zoomed_region.size

        nimage = Image.open(npath)
        nbarray = []

        for x in range(nwidth):
            for y in range(nheight):
                r, g, b = nimage.getpixel((x, y))
                nbarray.extend([[r], [g], [b]])
        nbarray.extend([[r], [g], [b]])

        string = "New shape after slicing: "

        print(string, (nheight, nwidth, 1), " or ", (nheight, nwidth))
    except AssertionError as e:
        print(f"AssertionError: {e}")

    return nbarray