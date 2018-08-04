#!/usr/bin/env python
##################################################
# Copyright (C) 2017, All rights reserved.
##################################################

from __future__ import print_function
import argparse
import exifread
import os
import sys

from pyprelude.file_system import make_path

from exifscan import __description__, __project_name__, __version__

_EXTENSIONS = map(lambda x: x.lower(), [".jpg", ".jpeg", ".png", ".avi"])

def _exif_dump(scan_dir):
    for f in os.listdir(scan_dir):
        if os.path.splitext(f)[1].lower() in _EXTENSIONS:
            path = make_path(scan_dir, f)
            with open(path, "rb") as f:
                tags = exifread.process_file(f)
                if len(tags.keys()) > 0:
                    print("{}:".format(path))
                    for key in tags.keys():
                        print("  {}".format(key))
                else:
                    print("No tags found in {}".format(path))

def _main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument("--version", action="version", version="{} version {}".format(__project_name__, __version__))
    parser.add_argument("scan_dir", metavar="SCANDIR", type=make_path)

    args = parser.parse_args(argv)
    _exif_dump(args.scan_dir)

if __name__ == "__main__":
    _main()