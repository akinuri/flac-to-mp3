import glob
import os, sys
from pydub import AudioSegment
from mutagen.flac import FLAC, Picture
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TRCK, TYER, APIC
from mutagen.mp3 import MP3

def get_flacs_in_dir(dir_path):
    items = []
    if os.path.isdir(dir_path):
        items = glob.glob(dir_path + "/*.flac")
    return items

def convert_flac_to_mp3(flac_path, mp3_path):
    flac_audio = AudioSegment.from_file(flac_path, "flac")
    flac_audio.export(mp3_path, format="mp3", bitrate="320k")

def copy_metadata_from_flac_to_mp3(flac_path, mp3_path):
    flac_file = FLAC(flac_path)
    mp3_file = MP3(mp3_path, ID3=ID3)
    if flac_file.tags:
        if "title" in flac_file:
            mp3_file.tags.add(TIT2(encoding=3, text=flac_file["title"][0]))
        if "artist" in flac_file:
            mp3_file.tags.add(TPE1(encoding=3, text=flac_file["artist"][0]))
        if "album" in flac_file:
            mp3_file.tags.add(TALB(encoding=3, text=flac_file["album"][0]))
        if "tracknumber" in flac_file:
            mp3_file.tags.add(TRCK(encoding=3, text=flac_file["tracknumber"][0]))
        if "date" in flac_file:
            mp3_file.tags.add(TYER(encoding=3, text=flac_file["date"][0]))
        album_art = None
        for picture in flac_file.pictures:
            if picture.type == 3:
                album_art = picture.data
                break
        if album_art:
            try:
                mp3_file.add_tags()
            except:
                pass
            mp3_file.tags.add(APIC(
                encoding=3,
                mime='image/jpeg',
                type=3,
                desc=u'Cover',
                data=album_art
            ))
        mp3_file.save()

def is_flac_path(path):
    return os.path.isfile(path) and path.lower().endswith('.flac')

def prog_exit(messages=[]):
    if messages:
        if not isinstance(messages, list):
            messages = [messages]
        for message in messages:
            print(message)
    print("")
    print("Program will close.")
    input()
    sys.exit()
    
