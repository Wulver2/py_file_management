import os
from pathlib import Path
import re
import datetime
import platform


# should allow anyone to use on their computer without having to change paths
source = Path.home() / "Downloads"
target = Path.home() / "Documents/photos"
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
    else: 
        dateCreated = creation_date(str(folder) + "/" + file)
        matchObj = re.match(DATE_PATTERN, dateCreated)
        if (matchObj):
            year = matchObj.group(1)
            month = matchObj.group(2)
        else:
            year = "0"
            month = "0"
            print("Unble to get date: " + file)
         
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

def getFolder(year, monthNumber):
    if (monthNumber == "01"):
        monthFolder = "01_January"
    elif (monthNumber == "02"):
        monthFolder = "02_February"
    elif (monthNumber == "03"):
        monthFolder = "03_March"
    elif (monthNumber == "04"):
        monthFolder = "04_April"
    elif (monthNumber == "05"):
        monthFolder = "05_May"
    elif (monthNumber == "06"):
        monthFolder = "06_June"
    elif (monthNumber == "07"):
        monthFolder = "07_July"
    elif (monthNumber == "08"):
        monthFolder = "08_August"
    elif (monthNumber == "09"):
        monthFolder = "09_September"
    elif (monthNumber == "10"):
        monthFolder = "10_October"
    elif (monthNumber == "11"):
        monthFolder = "11_November"
    elif (monthNumber == "12"):
        monthFolder = "12_December"
  
    return year + "/" + monthFolder


def move_photos():
    for file in files:
         if (is_photo(file)):
            date = get_date(source, file)
            year = date["year"]
            month = date["month"]

            if (year == "0" or month == "0"):
                continue

            folder = getFolder(year, month)
            targetFolder = str(target) + "/" + folder

            if (not os.path.exists(targetFolder)):
                os.makedirs(targetFolder)

            targetFile = targetFolder + "/" + file
            if(not os.path.exists(targetFile)):
                  print(targetFile)


def main():
    move_photos()

if __name__=="__main__":
    main()