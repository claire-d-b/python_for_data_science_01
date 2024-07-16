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
        items = image.getpixel((0, 0))
        i = 0
        for item in items:
            i += 1
        print(string, (height, width, i))
    except AssertionError as e:
        print(f"AssertionError: {e}")
    return [barray]
