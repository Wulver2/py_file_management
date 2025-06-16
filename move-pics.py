import os
from pathlib import Path
import re
import datetime
import platform


# should allow anyone to use on their computer without having to change paths
source = Path.home() / "Downloads"
target = Path.home() / "Documents/Photos"
EXTS = ("jpg", "png", "jpeg", "mov", "mp4", "mp3")
# year/month/day
DATE_PATTERN = r".*(20\d\d)-?([01]\d)-?([0123]\d).*"

files = os.listdir(source)

# includes videos as well, may create one for to organize .pdf and .txt files
# add option for screenshots
def is_photo(file):
    if (file.lower().endswith(tuple(EXTS))) :
            return True
    return False

def get_date(folder, file):
    matchObj = re.match(DATE_PATTERN, file)
    if (matchObj):
         year = matchObj.group(1)
         month = matchObj.group(2)
         print(year)
         print(month)
    else: 
         dateCreated = creation_date(str(folder) + "/" + file)
         matchObj = re.match(DATE_PATTERN, dateCreated)
         year = matchObj.group(1)
         month = matchObj.group(2)
         print(year)
         print(month)
    return {"year": year, "month": month}
         
    
def creation_date(path_to_file):
    if platform.system() == 'Windows':
        timestamp = os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            timestamp = stat.st_birthtime
        except AttributeError:
            timestamp = stat.st_mtime
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def move_photos():
    for file in files:
         if(is_photo(file)):
              date = get_date(source, file)
              year = date["year"]
              month = date["month"]
              
              

def main():
    move_photos()

if __name__=="__main__":
    main()