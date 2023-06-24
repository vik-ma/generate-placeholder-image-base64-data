import base64
from io import BytesIO
from PIL import Image

# CUSTOMIZE THESE VALUES
OUTPUT_WIDTH = 8
OUTPUT_HEIGHT = 5
OUTPUT_QUALITY = 100

file_name = r"test.png"

img_name = file_name.rsplit(".", 1)[0]

img = Image.open(file_name)

resized_img = img.resize((OUTPUT_WIDTH, OUTPUT_HEIGHT), Image.LANCZOS)

# resized_img.save("output.jpg", optimize=True, quality=OUTPUT_QUALITY)

buffered = BytesIO()
resized_img.save(buffered, optimize=True, quality=OUTPUT_QUALITY, format="JPEG")
base64_data = base64.b64encode(buffered.getvalue())

image_data_uri = "data:image/jpeg;base64," + str(base64_data)[2:-1]

output_text = [img_name, image_data_uri]

with open("output.txt", "w") as file:
    file.write('\n'.join(output_text))
    file.write('\n')