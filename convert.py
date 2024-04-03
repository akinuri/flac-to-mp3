from pathlib import Path
import os, sys

from utils import convert_flac_to_mp3, copy_metadata_from_flac_to_mp3, get_flacs_in_dir, prog_exit

if len(sys.argv) != 2:
    prog_exit("This program expects a single directory.")

flac_dir_path = sys.argv[1]

if not os.path.isdir(flac_dir_path):
    prog_exit("The provided path is not a directory or does not exist.")

flac_paths = get_flacs_in_dir(flac_dir_path)

if len(flac_paths) == 0:
    prog_exit("There are no flac files in the provided directory.")

print("%d files are found." % len(flac_paths))

mp3_dir_path = flac_dir_path + " (mp3)"

if not os.path.isdir(mp3_dir_path):
    os.mkdir(mp3_dir_path)

print("Processing ...")

for flac_path in flac_paths:
    flac_name = Path(flac_path).stem
    print(flac_name)
    mp3_path = mp3_dir_path + "\\" + flac_name + ".mp3"
    convert_flac_to_mp3(flac_path, mp3_path)
    copy_metadata_from_flac_to_mp3(flac_path, mp3_path)

print("Done")

prog_exit()

