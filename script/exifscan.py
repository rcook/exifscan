#!/usr/bin/env python
##################################################
# Copyright (C) 2017, All rights reserved.
##################################################

from __future__ import print_function
import exifread
import os

_EXTENSIONS = map(lambda x: x.lower(), [".jpg", ".jpeg", ".png"])

def _exif_dump(dir):
    for f in os.listdir(dir):
        if os.path.splitext(f)[1].lower() in _EXTENSIONS:
            path = os.path.abspath(os.path.join(dir, f))
            with open(path, "rb") as f:
                tags = exifread.process_file(f)
                if len(tags.keys()) > 0:
                    print("{}:".format(path))
                    for key in tags.keys():
                        print("  {}".format(key))
                else:
                    print("No tags found in {}".format(path))

def _main():
    _exif_dump("C:/Users/rcook/Pictures")

if __name__ == "__main__":
    _main()