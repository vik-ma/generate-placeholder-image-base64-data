import base64
from io import BytesIO
from PIL import Image
import os

# CUSTOMIZE THESE VALUES
OUTPUT_IMAGE_WIDTH = 8
OUTPUT_IMAGE_HEIGHT = 5
OUTPUT_IMAGE_QUALITY = 95
INPUT_FOLDER_DIR = "input"


def generate_base64_strings(input_files):
    output_text = []

    for file in input_files:
        if not (file.endswith(".png") or file.endswith(".jpg")\
                or file.endswith(".jpeg") or file.endswith(".gif")):
            print(f"Did not load {file} because it is not a valid type!")
            continue
        
        img_name = file.rsplit(".", 1)[0]

        img = Image.open(f"{INPUT_FOLDER_DIR}/{file}")

        resized_img = img.resize((OUTPUT_IMAGE_WIDTH, OUTPUT_IMAGE_HEIGHT), Image.LANCZOS)

        # resized_img.save(f"{img_name}.jpg", optimize=True, quality=OUTPUT_IMAGE_QUALITY)

        buffered = BytesIO()
        resized_img.save(buffered, optimize=True, quality=OUTPUT_IMAGE_QUALITY, subsampling=0, format="JPEG")
        base64_data = base64.b64encode(buffered.getvalue())

        image_data_uri = "data:image/jpeg;base64," + str(base64_data)[2:-1]

        output_text.extend([img_name, '\n', image_data_uri, '\n', '\n'])

    if output_text != []:
        with open("output.txt", "w") as file:
            file.writelines(output_text)

        print("Finished")
    else:
        print(f"No valid files in '{INPUT_FOLDER_DIR}' folder!")

if __name__ == "__main__":
    if not os.path.exists(INPUT_FOLDER_DIR):
        print(f"No folder named '{INPUT_FOLDER_DIR}'!\nCreate a folder in this directory with the name '{INPUT_FOLDER_DIR}' and put your images inside there.")
    else:
        input_files = os.listdir(INPUT_FOLDER_DIR)

        if len(input_files) > 0:
            generate_base64_strings(input_files)
        else:
            print(f"No files in '{INPUT_FOLDER_DIR}' folder!")