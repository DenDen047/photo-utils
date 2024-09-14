import os
import sys
import glob
from tqdm import tqdm
from pprint import pprint


if __name__ == "__main__":
    parent_dir = '/Volumes/Untitled/DCIM/100MSDCF'

    jpeg_files = sorted(glob.glob(os.path.join(parent_dir, '*.JPG')))
    arw_files = sorted(glob.glob(os.path.join(parent_dir, '*.ARW')))

    # Remove the ARW file names based on the JPEG list
    # Extract only the base name (without extension) to compare
    jpeg_basenames = {os.path.basename(fj)[:-4] for fj in jpeg_files}

    # Find ARW files not in the JPEG list
    arw_to_remove = [f for f in arw_files if os.path.basename(f)[:-4] not in jpeg_basenames]

    # make trash dir
    trash_dir = os.path.join(parent_dir, 'trash')
    os.makedirs(trash_dir, exist_ok=True)

    # move to trash
    for arw_file in tqdm(arw_to_remove):
        os.rename(
            arw_file,
            os.path.join(trash_dir, os.path.basename(arw_file))
        )
