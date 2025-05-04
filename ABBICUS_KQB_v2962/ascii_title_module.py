
# ascii_title_module.py

from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def scale_image(image, new_width=80):
    width, height = image.size
    aspect_ratio = height / float(width)
    new_height = int(aspect_ratio * new_width * 0.55)
    return image.resize((new_width, new_height))

def convert_to_grayscale(image):
    return image.convert("L")

def map_pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ''.join(ASCII_CHARS[pixel // 25] for pixel in pixels)
    return ascii_str

def convert_image_to_ascii(image_path, width=80):
    try:
        image = Image.open(image_path)
        image = scale_image(image, width)
        image = convert_to_grayscale(image)
        ascii_str = map_pixels_to_ascii(image)
        pixel_count = len(ascii_str)
        ascii_image = "\n".join(
            ascii_str[index:(index + width)] for index in range(0, pixel_count, width)
        )
        return ascii_image
    except Exception as e:
        return f"[ERROR] Could not generate ASCII art: {e}"

def display_ascii_title():
    path = "Media/Images/ABBICUS Title Image.png"
    print("[ABBI] Generating visual entropy...")
    ascii_art = convert_image_to_ascii(path, width=80)
    print(ascii_art)
    print("\n[OSO UNIT NOTICE] Ostriches initialized. If you see feathers in the logs, don't worry about it.")
