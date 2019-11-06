import csv
import requests
import os
import glob
from PIL import Image

def get_images():

    if not os.path.exists('images'):
        os.mkdir("images")



    with open('data/multimedia.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV) # skip the header line

        for row in readCSV:
            url = row[2]
            local_name = "images/"+url.split("/")[-1]
            if os.path.exists(local_name):
                continue

            print('downloading', url)
        
            #download and save to file
            results = requests.get(url)
    
            open(local_name, 'wb').write(results.content)


def resize_images(file, folder):
    os.getcwd()
    if not os.path.exists(folder):
        os.mkdir(folder)

    im = Image.open(file)
    print(im.size)
    thumbpath = thumbs + "/" + os.path.basename(file)
    thumbpath = thumbpath.replace(".tif", ".jpg")
    #im.save(thumbs+'/'++"_thumb.jpg", quality=50)
    im.save(thumbpath, quality=50)


def resize():
    path = os.getcwd()
    images_dir = path+"/images/"
    print(images_dir)
    for item in images_dir:
        if os.path.isfile(images_dir+item):
            im = Image.open(images_dir+item)
            f, e = os.images_dir.splitext(images_dir+item)
            imResize = im.resize((200,200), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=50)

def crop_image(file, folder):
    print("Resizing images")
    # thumbs="/Users/tegabrain/Documents/PROJECTS/Current/2019-Vienna/sat-tiles/"+location+"-thumbs"
    thumbs=folder+"-thumbs"

    print(thumbs)
    if not os.path.exists(thumbs):
        os.mkdir(thumbs)
    im = Image.open(file)
    print(im.size)
    #thumbpath = os.path.dirname(file) + location+"thumbs" + os.path.basename(file)
    thumbpath = thumbs + "/" + os.path.basename(file)
    thumbpath = thumbpath.replace(".tif", ".jpg")
    #im.save(thumbs+'/'++"_thumb.jpg", quality=50)
    im.save(thumbpath, quality=50)

if __name__ == "__main__":
    resize()
    path = os.getcwd()
    #images_dir = path+"/images/"
    for image_file in glob.iglob(path+'images/*.jpg'):
        crop_image(image_file, folder)

            

