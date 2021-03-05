#https://stackoverflow.com/questions/30227466/combine-several-images-horizontally-with-python
import PIL
from PIL import Image
import numpy as np
from os import listdir
from os.path import isfile, join

def photo_processing(domain):
    onlyfiles = [f"photo/{domain}/"+f for f in listdir(f'photo/{domain}') if isfile(join(f'photo/{domain}', f))]
    print(onlyfiles)


    imgs = [PIL.Image.open(i) for i in onlyfiles ]
    # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
    min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
    imgs_comb = np.hstack(np.asarray(i.resize(min_shape)) for i in imgs)

    # save that beautiful picture
    imgs_comb = PIL.Image.fromarray( imgs_comb)
    imgs_comb.save( 'Trifecta.jpg' )

    # for a vertical stacking it is simple: use vstack
    imgs_comb = np.vstack(np.asarray(i.resize(min_shape)) for i in imgs)
    imgs_comb = PIL.Image.fromarray(imgs_comb)
    imgs_comb.save('Trifecta_vertical.jpg')