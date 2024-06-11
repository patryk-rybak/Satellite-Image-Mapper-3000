import os
import re
import imageio

# Ścieżka do folderu 
folder_path = 

def extract_epoch_number(filename):
    match = re.search(r'epoch_(\d+)_last_batch', filename) #doktryna nazewnictwa
    return int(match.group(1)) if match else -1

image_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]

image_files.sort(key=extract_epoch_number)

images = []
for filename in image_files:
    img_path = os.path.join(folder_path, filename)
    images.append(imageio.imread(img_path))

output_path = 'ZAJEBISTYGIF.gif'
imageio.mimsave(output_path, images, duration=0.01) #czas jednej klatki 0.01 wydaje mi sie optymalne 
