from PIL import Image

def ft_load(path: str) -> bytearray:
    image = Image.open(path)
    barray = []

    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            barray.append([r, g, b])
    
    barray.append([r, g, b])
    string = "The shape of image is: "
    try:
        assert len(barray) % 3 == 0, "Error: file is not in correct format"
        print(string, (height, width, 3))
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return None
    return barray

