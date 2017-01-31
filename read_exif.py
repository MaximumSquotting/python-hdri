#!/usr/bin/env python3

import argparse
import os
import pyexiv2

def get_exposure(photo):
    metadata = pyexiv2.ImageMetadata(photo)
    metadata.read()
    try:
        exposure_fraction = metadata['Exif.Photo.ExposureTime'].value
        return round(float(exposure_fraction), 10)
    except KeyError:
        print("%{0} lacks ExposureTime EXIF tag. Skipping.".format(photo))
        pass

parser = argparse.ArgumentParser()
parser.add_argument("images", nargs="+", help="images to get the values from")
args = parser.parse_args()

for filename in args.images:
    exposure = get_exposure(filename)
    filename_split = os.path.splitext(filename)
    new_filename = "t{0}{1}".format(exposure, filename_split[1].lower())
    print("Renaming {0} to {1}".format(filename, new_filename))
    os.rename(filename, "input/" + new_filename)
