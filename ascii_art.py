from PIL import Image

ASCII_CHARACTERS_BY_SURFACE = '`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
MAX_BRIGHTNESS = 255 * 3
BRIGHTNESS_WEIGHT = len(ASCII_CHARACTERS_BY_SURFACE) / MAX_BRIGHTNESS

def main():
    image = Image.open('your-image.jpeg')
    art_image_with_ascii(image)

def art_image_with_ascii(image):
    ascii_art = []
    (width, height) = image.size

    for i in range(0, height - 1):
        line = ''
        for j in range(0, width - 1):
            pixel = image.getpixel((j, i))
            line += convert_pixel_to_character(pixel)
        ascii_art.append(line)

    save_ascii_text_in_file(ascii_art)

def convert_pixel_to_character(pixel):
    (r, g, b) = pixel
    pixel_brightness = r + g + b
    index = int(BRIGHTNESS_WEIGHT * pixel_brightness) - 1

    return ASCII_CHARACTERS_BY_SURFACE[index]

def save_ascii_text_in_file(ascii_text):
    with open('your-image.txt', 'w') as file:
        for line in ascii_text:
            file.write(line)
            file.write('\n')
        file.close

if __name__ == '__main__':
    main()