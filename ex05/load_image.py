from PIL import Image, ImageOps

def ft_load(path: str) -> bytearray:
    input_image_path = "animal.jpeg"
    output_image_path = "rotate.jpeg"
    barray = []
    try:
        assert Image.open(input_image_path)
        # Open the image
        image = Image.open(input_image_path)
        
        # Invert the image
        inverted_image = ImageOps.invert(image)
        
        # Save the inverted image
        inverted_image.save(output_image_path)

        width, height = image.size

        for x in range(width):
            for y in range(height):
                r, g, b = image.getpixel((x, y))
                barray.append([r, g, b])
        barray.append([r, g, b])

    except AssertionError as e:
        print(f"AssertionError: {e}")

    return barray
    
