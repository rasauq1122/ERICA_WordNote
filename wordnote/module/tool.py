import os

def checkLast(main_string,clue):
    clue_length = len(clue)
    main_length = len(main_string)
    return main_string[main_length-clue_length:] == clue

now_dir = os.getcwd()
directoies = ["/data","/module","/data/note","/data/star","/data/work"]
main_dir = ""

for key in directoies:
    if checkLast(now_dir,key) :
        main_dir = now_dir.split(key)[0]
if main_dir == "":
    main_dir = now_dir

data_dir = main_dir+directoies[0]
module_dir = main_dir+directoies[1]
note_dir = main_dir+directoies[2]
star_dir = main_dir+directoies[3]
work_dir = main_dir+directoies[4]

def get_yes_or_no(notice):
    check = input(notice+" [y/n] ")
    while not check in ["y","yes","n","no"] :
        check = input("다음 중 하나를 입력해주세요. [y, yes, n, no] ")
        if check.strip().isalpha() :
            check = check.strip().lower()
        else :
            continue
    return check in ["y","yes"]

    
def normalSplit(given_string, clue):
    where = given_string.find(clue)
    if where == -1 :
        return [given_string]
    else :
        return [given_string[:where],given_string[where+len(clue):]]

def setNNN(note_name,home_dir):
    os.chdir(work_dir)
    now_note_name = open("NowNoteName.txt","w",encoding="UTF-8")
    now_note_name.write(note_name)
    now_note_name.close()
    os.chdir(home_dir)

def getNNN(home_dir):
    os.chdir(work_dir)
    if os.path.isfile(work_dir+"/NowNoteName.txt") :
        now_note_name = open("NowNoteName.txt","r",encoding="UTF-8")
        note_name = now_note_name.readline()
        os.chdir(home_dir) 
        return note_name
    else :
        os.chdir(home_dir)
        return "" 

def resetNNN(home_dir):
    os.chdir(work_dir)
    if os.path.isfile(work_dir+"/NowNoteName.txt") :
        os.remove(work_dir+"/NowNoteName.txt")
    os.chdir(home_dir)
