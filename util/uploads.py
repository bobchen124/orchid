'''
Created on 2013-1-21
@author: Bob
'''

import os
from orchid import settings
import uuid
import ImageFile
import Image

def do_upload(temp_file):
    try:
        if temp_file:
            file_dir = os.path.join(settings.STATIC_ROOT,"upload/temp")
            file_name = str(uuid.uuid1()) + '.' + str(temp_file.name).split('.')[-1]
            file_path = os.path.join(file_dir, file_name)
            
            parser = ImageFile.Parser()
            for chunk in temp_file.chunks():
                #pass
                parser.feed(chunk)
            temp_img = parser.close()
            #try:
            temp_img.thumbnail((400,300))
            temp_img.save(file_path)
                
            return file_name
            #except Exception, e:
                #return "" + e
    except Exception, e:
        return "" + e

def compressImage(imagepath):
    image_file = Image.open(imagepath)
    image_file.thumbnail()

def image_cut(file_name,x,y,width,height):
    try:
        file_dir = os.path.join(settings.STATIC_ROOT,"upload/temp")
        file_path = os.path.join(file_dir, file_name)
        file_image = Image.open(file_path);
    
        box = (int(x),int(y),int(width),int(height))
        region = file_image.crop(box)
    
        save_path =  os.path.join(settings.STATIC_ROOT,"upload/live")
        file_path = os.path.join(save_path, file_name)
        region.save(file_path)
    except:
        pass
#print str(uuid.uuid1())
#print str(uuid.uuid4())    