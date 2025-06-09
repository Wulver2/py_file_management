import os;
from pathlib import Path

# should allow anyone to use on their computer without having to change paths
source = Path.home() / "Downloads"
target = Path.home() / "Documents/Photos"
EXTS = ("jpg", "png", "jpeg", "mov", "mp4", "mp3")

files = os.listdir(source)

# includes videos as well, may create one for to organize .pdf and .txt files
# add option for screenshots
def is_photo(file):
    if (file.lower().endswith(tuple(EXTS))) :
            return True
    return False

def move_photos():
    for file in files:
         if(is_photo(file)):
              print(file)
              

def main():
    move_photos()

if __name__=="__main__":
    main()