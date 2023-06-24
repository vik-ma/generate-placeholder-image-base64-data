# Generate Placeholder Image Base64 Data String

This is a simple Python script to generate multiple base64-encoded image strings to be used as placeholder images that appears before the images on a website are fully loaded.

The script will resize, optimize and generate a base64 string for every image in the 'input' folder and then write the base64 data string for every image in an 'output.txt' file.

The format of the outputted strings will look like this: '**data:image/jpeg;base64,**' followed by the generated base64 string.

## Requirements
The script only requires the Pillow package to run.

## How To Use

1. Create a folder in the same directory as main.py named '**input**'. <br>
   *(The name of the folder can be changed with the **INPUT_FOLDER_DIR** variable inside **'main.py'**)*
2. Place all the images you want to generate base64 data string for inside the '**input**' folder.
3. Edit the '**OUTPUT_IMAGE_WIDTH**', '**OUTPUT_IMAGE_HEIGHT**' and '**OUTPUT_IMAGE_QUALITY**' variables inside **'main.py'** to your liking. <br>
   *(It is recommended to keep the width and height below **10**)* <br> 
   *(Image Quality must range between **1** to **95**, where 1 is the lowest quality and 95 the highest)*
4. Run **'main.py'** and check the generated '**output.txt**' file for every image's base64 string.