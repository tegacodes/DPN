import csv
import requests
import os
import glob
from PIL import Image

def get_images(num):

    if not os.path.exists('images'): #make image folder 
        os.mkdir("images")

    with open('data/multimedia.csv') as csvfile: #open csv file
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV) # skip the header line

        for i, row in enumerate(readCSV): 
            if i > num: #download certain number of images
                break
        #for row in readCSV: #uncomment to download entire dataset
            url = row[2]
            local_name = "images/"+url.split("/")[-1]
            if os.path.exists(local_name):
                continue

            print('downloading', url)
        
            #download and save to file
            results = requests.get(url)
    
            open(local_name, 'wb').write(results.content)


def resize_image(file):
    print("Resizing images")
    thumbs="thumbs"

    print(thumbs)
    if not os.path.exists(thumbs):
        os.mkdir(thumbs)
    im = Image.open(file)
    print(im.size)
    im.thumbnail((600,400)) #set image size you want
    thumbpath = thumbs + "/" + os.path.basename(file)

    im.save(thumbpath, quality=50) #set image quality

def rename_image(collection):
    for i, filename in enumerate(os.listdir(collection)):
        os.rename(collection+filename, "image" + str(i) + ".jpg")


if __name__ == "__main__":
    #download images
    get_images(10) 

    #resize images 
    #for image_file in glob.iglob('images/*.JPG'): 
        #resize_image(image_file)
    #for image_file in glob.iglob('thumbs/*.JPG'): #resize .jpgs
        #rename_image('thumbs/')

    #for image_file in glob.iglob('images/*.JPG'): #resize .JPGs
        #resize_image(image_file)

            

