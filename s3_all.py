from src.skull import SkullStripper
from src import helpers as utils
import os
import time
import torch
import glob
import numpy as np
def get_file_names(path_images):
    img_names = []
    files = glob.glob(os.path.join(path_images, '*.nii'))
                
    return files

if __name__ == '__main__':

    from sys import argv

    myargs = utils.getopts(argv)

    want_tissues = False
    want_atlas = False

    if '-i' in myargs:
        input_path = myargs['-i']
        output_path = os.path.dirname(os.path.abspath(input_path))

    if '-o' in myargs:
        output_path = myargs['-o']
        output_path = os.path.abspath(output_path)

    if '-t' in myargs:
        want_tissues = True

    if '-a' in myargs:
        want_atlas = True

    if not os.path.exists(output_path):
        print("The selected output folder doesn't exist, so I am making it \n")
        os.makedirs(output_path)
    os.makedirs(os.path.join(output_path, 'main_result'),exist_ok=True)
    
    img_names=get_file_names(input_path)
#     print(img_names)
    done_images=[]
    
    with open('processed_images.npy', 'rb') as f:
        done_images = np.load(f)
    print(len(done_images))
    done_images=done_images.tolist()
    img_names_2=[]
    
    for el in img_names:
        if el not in done_images:
            img_names_2.append(el)
    img_names=img_names_2
    
    for el in img_names:
        start = time.time()
        skull_stripper = SkullStripper(el, output_path, want_tissues, want_atlas)
        skull_stripper.strip_skull()
        done_images.append(el)
        print('Done (' + str((time.time() - start) / 60.) + ' min)')
        with open('processed_images.npy', 'wb') as f:
            np.save(f,done_images)
            
