# Thumbnail Generator
# Created By Liam Moore
# February 19th, 2020

import subprocess
import os
import PIL
from PIL import Image

# find current path
cwd = os.getcwd()

# take initial input
print(".-------------------------------------------------.")
print("|------------ Thumbnail Generator v2.0 -----------|")
print("| MAKE SURE THIS PROGRAM IS IN THE SAME FOLDER AS |")
print("|   THE VIDEOS YOU WISH TO MAKE THUMBNAILS FOR    |")
print("'-------------------------------------------------'")
video_file_name = input("Enter filename or type quit: ")

while video_file_name != "quit":
    # locate file
    video_input_path = cwd + '/' + video_file_name

    # check if file exists
    if not os.path.exists(video_input_path):
        print("The file specified does not exist. Please try again.")
    else:
        # convert video file name into thumbnail file name
        thumbnail_name_list = video_file_name.split(".")
        thumbnail_name = thumbnail_name_list[0]

        # check if thumbnails path exists, make the directory if not
        if not os.path.exists(cwd + '/Thumbnails'):
            print("No thumbnails folder found, creating one now...")
            os.mkdir(cwd + "/Thumbnails")
            print("Folder created.")
        else:
            print("Thumbnails folder found.")
        time = input("Enter thumbnail time: ")

        # output thumbnail
        img_output_path = cwd + '/Thumbnails/' + thumbnail_name + '.jpg'
        subprocess.call(['ffmpeg', '-loglevel', 'quiet', '-i', video_input_path, '-vframes', '1', '-an', '-s', '640x480', '-ss', time, img_output_path])

        # preview thumbnail
        image = Image.open(img_output_path)
        image.show()

        # check if user is okay with thumbnail
        option = input("Is this ok? (y/n): ")
        if (option != "Y" and option != "y"):
            os.remove(img_output_path)
            print("Deleted.")
        else:
            # completion message
            print("Thumbnail created for " + video_input_path)
            print("Complete!")

    # take input to continue loop
    video_file_name = input("Enter filename or type quit: ")

print("Exiting...")
