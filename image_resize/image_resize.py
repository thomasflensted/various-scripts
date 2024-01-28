'''
This program resizes multiple images to a size specified by the user.

'''

from PIL import Image
import os, os.path, sys

extensions = ("jpg", "jpeg", "png", "tiff", "tif")

def main():

    if sys.argv == 1:

        sys.exit("Usage: image_resize.py [path to folder with images]")

    else:

        folder = sys.argv[1]

    response = intro()
    skipped_images = image_resize(response, folder)
    outro(skipped_images)

#user specifies how they want to resize their images. They choose between width, length, short edge and long edge.
def intro():

    print("\nThis program resizes multiple images to a desired size.\nImages smaller than the specified size will not be processed.")
    response = input("The aspect ratio of the images will be maintained.\n\nTo adjust image by height type 'h', to adjust by width, type 'w', to adjust by long edge type 'l', and to adjust by short edge type 's': ")

    while True:
        if response == 'h' or response == 'w' or response == 'l' or response == 's':
            break
        else:
            response = input("Please type h, w, l or s: ")

    return response

#the user specifies the size in pixels they want their images to have.
def image_resize(response, folder):

    if response == 'h':
        new_size = input("\nType the height (in pixels) you want your image(s) to have: ")
    elif response == 'w':
        new_size = input("\nType the width (in pixels) you want your image(s) to have: ")
    elif response == 'l':
        new_size = input("\nType the length (in pixels) you want the long edge of your image(s) to have: ")
    else:
        new_size = input("\nType the length (in pixels) you want the short edge of your image(s) to have: ")

    while True:
        if new_size.isdigit():
            break
        else:
            new_size = input("Please type a number: ")
    
    if response == 'h':
        skipped_images = height_resize(new_size, folder)
    elif response == 'w':
        skipped_images = width_resize(new_size, folder)
    elif response == 'l':
        skipped_images = long_resize(new_size, folder)
    else:
        skipped_images = short_resize(new_size, folder)
    
    return skipped_images

#this function resizes by width and returns the number of skipped images,
#i.e. images that are smaller than the size specified by the user 
def width_resize(new_size, folder):

    skipped_images = 0

    for file in os.listdir(folder):

        if file.endswith(extensions):
            f_img = folder + "/" + file
            img = Image.open(f_img)
            width, height = img.size

            if width > int(new_size):
                IMAGE_RATIO = (int(new_size) / width)
                img = img.resize((int(new_size), int(height*IMAGE_RATIO)))
                img.save(f_img)
            else:
                skipped_images += 1

    return skipped_images

#this function resizes by height and returns the number of skipped images,
#i.e. images that are smaller than the size specified by the user
def height_resize(new_size, folder):

    skipped_images = 0

    for file in os.listdir(folder):

        if file.endswith(extensions):
            f_img = folder + "/" + file
            img = Image.open(f_img)
            width, height = img.size

            if height > int(new_size):
                IMAGE_RATIO = (int(new_size) / height)
                img = img.resize((int(width*IMAGE_RATIO), int(new_size)))
                img.save(f_img)
            else:
                skipped_images += 1

    return skipped_images

#this function resizes by long edge and returns the number of skipped images,
#i.e. images that are smaller than the size specified by the user
def long_resize(new_size, folder):

    skipped_images = 0

    for file in os.listdir(folder):

        if file.endswith(extensions):
            f_img = folder + "/" + file
            img = Image.open(f_img)
            width, height = img.size

            if width > height:
                if width > int(new_size):
                    IMAGE_RATIO = (int(new_size) / width)
                    img = img.resize((int(new_size), int(height*IMAGE_RATIO)))
                    img.save(f_img)
                else:
                    skipped_images += 1
            else:
                if height > int(new_size):
                    IMAGE_RATIO = (int(new_size) / height)
                    img = img.resize((int(width*IMAGE_RATIO), int(new_size)))
                    img.save(f_img)
                else:
                    skipped_images += 1

    return skipped_images

#this function resizes by short edge and returns the number of skipped images,
#i.e. images that are smaller than the size specified by the user
def short_resize(new_size, folder):

    skipped_images = 0

    for file in os.listdir(folder):

        if file.endswith(extensions):
            f_img = folder + "/" + file
            img = Image.open(f_img)
            width, height = img.size

            if width > height:
                if height > int(new_size):
                    IMAGE_RATIO = (int(new_size) / height)
                    img = img.resize((int(width*IMAGE_RATIO), int(new_size)))
                    img.save(f_img)
                else:
                    skipped_images += 1
            else:
                if width > int(new_size):
                    IMAGE_RATIO = (int(new_size) / width)
                    img = img.resize((int(new_size), int(height*IMAGE_RATIO)))
                    img.save(f_img)
                else:
                    skipped_images += 1

    return skipped_images

#finally the program prints that all images have been processed. If any of the images
#were smaller than the specified size the program prints the number of skipped images.       
def outro(skipped_images):
    
    if skipped_images == 0:
        print("All images have been processed.")
    else
        print(str(skipped_images), "images were smaller than the specified size. All remaining images have been processed.")

if __name__ == '__main__':
    main()
