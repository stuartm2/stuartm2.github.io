#!/usr/bin/python

from os import listdir, system
from os.path import isdir, isfile, join
from sys import argv


VALID_EXTS = ['.jpg', '.png', '.gif']


def valid_ext(filename):
    filename = filename.lower()

    for ext in VALID_EXTS:
        if filename.endswith(ext) and not (filename.endswith('.tn' + ext) or
                filename.endswith('_' + ext)):
            return True

    return False


dirpath = argv[1]
assert isdir(dirpath)

images = [f for f in listdir(dirpath) if isfile(join(dirpath, f))
            and valid_ext(f)]

for img in images:
    tnimg = img.split('.')
    tnimg.insert(-1, 'tn')
    tnimg = '.'.join(tnimg)

    if not tnimg.startswith('cover.') and not isfile(join(dirpath, tnimg)):
        system('cp %s %s' % (join(dirpath, img), join(dirpath, tnimg)))
        system('sips -Z 600 %s' % join(dirpath, tnimg))

        print "%s > %s\n" % (img, tnimg)
