from PIL import Image
import os

dir_path=r'E:\AI精英2001\代码\day14\images'
cut_path = r'E:\AI精英2001\代码\day14\cut_images'
for file in os.listdir(dir_path):
    img = Image.open(os.path.join(dir_path,file))
    x,y=img.size
    img1 = img.crop(box=(0.5*x,0.5*y,0.5*x+100,0.5*y+100))
    img1.save(os.path.join(cut_path,file))