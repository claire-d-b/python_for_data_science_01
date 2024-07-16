from PIL import Image


def ft_load(path: str) -> bytearray:
    input_image_path = "animal.jpeg"
    output_image_path = "rotate.jpeg"
    try:
        assert Image.open(input_image_path), "Error: failed to open file"
        image = Image.open(input_image_path)
        barray = []

        width, height = image.size

        for x in range(width):
            for y in range(height):
                r, g, b = image.getpixel((x, y))
                barray.extend([r, g, b])
        barray.extend([r, g, b])

        nbarray = barray[::-1]
        # nbarray = barray
        """ Convert the flat list of RGB values to bytes """
        rgb_bytes = bytes(nbarray)

        """ Create an RGB image from bytes """
        img = Image.frombytes('RGB', (height, width), rgb_bytes)

        img.save(output_image_path)

        string = "The shape of image is: "
        items = image.getpixel((0, 0))
        i = 0
        for item in items:
            i += 1
        print(string, (height, width, i))
        print([nbarray])
    except AssertionError as e:
        print(f"AssertionError: {e}")

    except AssertionError as e:
        print(f"AssertionError: {e}")
    string = "New shape after transpose: "

    print(string, (height, width))

    return nbarray
