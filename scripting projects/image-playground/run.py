'''Create an image converter'''
# import sys
# import os
# from PIL import Image

# # grab first 'Pokemon' and second 'new' argument from terminal
# input_folder = sys.argv[1]
# output_folder = sys.argv[2]

# # check if 'new' exits, if not create it
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)


# # loop through Pokemon
# # convert images to png
# # save to the new folder 'new'
# for imagefile in os.listdir(input_folder):
#     img = Image.open(f'{input_folder}\\{imagefile}')
#     split_file = os.path.splitext(imagefile)[0]
#     img.save(f'{output_folder}\\{split_file}.png')
