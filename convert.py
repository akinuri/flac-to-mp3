from pathlib import Path
import os, sys

from utils import convert_flac_to_mp3, copy_metadata_from_flac_to_mp3, get_flacs_in_dir, is_flac_path, prog_exit

args = sys.argv[1:]
filtered_args = [arg for arg in args if os.path.isdir(arg) or is_flac_path(arg)]

if len(filtered_args) == 0:
    if len(args) != 0:
        prog_exit([
            "Provided arguments are invalid.",
            "An argument must be either a FLAC file path or a folder path that contains FLAC files."
        ])
    else:
        prog_exit([
            "This program expects at least a single argument",
            "that is either a FLAC file path or a folder path that contains FLAC files."
        ])

for arg in filtered_args:
    if os.path.isdir(arg):
        print("Processing the folder: %s" % arg)
        flac_dir_path = sys.argv[1]
        flac_paths = get_flacs_in_dir(flac_dir_path)
        if len(flac_paths) == 0:
            print("There are no flac files in the folder.")
            continue
        print("%d files are found." % len(flac_paths))
        mp3_dir_path = flac_dir_path + " (mp3)"
        if not os.path.isdir(mp3_dir_path):
            os.mkdir(mp3_dir_path)
        print("Processing the files ...")
        for flac_path in flac_paths:
            flac_name = Path(flac_path).stem
            print(flac_name)
            mp3_path = mp3_dir_path + "\\" + flac_name + ".mp3"
            convert_flac_to_mp3(flac_path, mp3_path)
            copy_metadata_from_flac_to_mp3(flac_path, mp3_path)
    else:
        print("Processing the file: %s" % arg)
        flac_path = arg
        flac_name = Path(flac_path).stem
        mp3_path = os.path.join(Path(flac_path).parent, flac_name + ".mp3")
        convert_flac_to_mp3(flac_path, mp3_path)
        copy_metadata_from_flac_to_mp3(flac_path, mp3_path)

print("Done")

prog_exit()

