# FLAC to MP3

A small script to convert FLAC files to MP3 files.

## Dependencies

- [FFmpeg](https://ffmpeg.org/)
- [pydub · PyPI](https://pypi.org/project/pydub/)
- [mutagen · PyPI](https://pypi.org/project/mutagen/)

```
pip install pydub
```
```
pip install mutagen
```

## Usage

Just pass the file and/or folder paths to the script file.

```
convert.py "path/to/some/dir" "path/to/some/file.flac"
```

On Windows, I just drag-and-drop the target files/folders on the script file.

## Output

- If the argument is a file, the new MP3 file is created next to the FLAC file.
- If it's a folder, a new folder with " (mp3)" appended to the original name will be created and the converted files will be in it.
