from os.path import *
import os

paths = {
    "input_path": "input",
    "output_path": "output",
}

for path in paths:
    if not exists(paths[path]):
        os.makedirs(paths[path])