def image_to_ascii(image):
    img = image.convert("L")
    img = img.resize((200, 100))
    WIDTH, HEIGHT = img.size
    chars = "-%#*+=@:."

    pixels = img.getdata()
    ascii_str = "".join([chars[(pixel * (len(chars) - 1)) // 255] for pixel in pixels])
    ascii_picture = ""
    for i in range(0, len(ascii_str), WIDTH):
        line = ascii_str[i:i+WIDTH]
        ascii_picture += line + "\n"

    print(ascii_picture)