# Art Images By ASCII Text

In this code we’ll art an image by ASCII characters with Python

If you are a Junior developer looking for a new challenge, this might be a good exercise!

## Code explanation

We will declare variable with string value is consist of all ASCII characters


```batch
  ASCII_CHARACTERS_BY_SURFACE = '`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
```
<hr>

Then, we will calculate maximum brightness value (each pixel in image consists of (r, g, b) values) and calculate brightness weight

```batch
  MAX_BRIGHTNESS = 255 * 3
  BRIGHTNESS_WEIGHT = len(ASCII_CHARACTERS_BY_SURFACE) / MAX_BRIGHTNESS
```
<hr>
Then, import Image from PIL module to open any image you want convert it and pass the variable as argument to our function


```batch
  from PIL import Image # to download this module in terminal type this command -> pip3 install PIL

  def main():
    image = Image.open('your-image.jpeg')
    art_image_with_ascii(image)
```
<hr>
Now, we’ll iterate through all the pixels and read them one by one and pass it as argument to convert function and add the ASCII code we get it to ascii_art array


```batch
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
```
<hr>
For a given pixel we can find its corresponding index from the ASCII characters string


```batch
  def convert_pixel_to_character(pixel):
    (r, g, b) = pixel
    pixel_brightness = r + g + b
    index = int(BRIGHTNESS_WEIGHT * pixel_brightness) - 1

    return ASCII_CHARACTERS_BY_SURFACE[index]
```
<hr>
Finally, we’ll write everything into a text file


```batch
  def save_ascii_text_in_file(ascii_text):
    with open('your-image.txt', 'w') as file:
        for line in ascii_text:
            file.write(line)
            file.write('\n')
        file.close
```
