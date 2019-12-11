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

def setNNN(note_name):
    now_note_name = open("data/work/NowNoteName.txt","w",encoding="UTF-8")
    now_note_name.write(note_name)
    now_note_name.close()

def getNNN():
    if os.path.isfile(work_dir+"/NowNoteName.txt") :
        now_note_name = open("data/work/NowNoteName.txt","r",encoding="UTF-8")
        note_name = now_note_name.readline()
        return note_name
    else :
        return "" 

def resetNNN():
    if os.path.isfile(work_dir+"/NowNoteName.txt") :
        os.remove(work_dir+"/NowNoteName.txt")

def doublesplit(given_string, para1, para2):
    splited = given_string.split(para1)
    for now in splited:
        splited = splited + now.split(para2)
        splited.remove(now)
    return splited

def findAtStar(word):
    star = open("data/star/STAR.txt","r",encoding="UTF-8")
    star_lines = star.readlines()
    for now_line in star_lines :
        now = now_line.split("MEANING;")[0].split(";")
        if len(now) != 1 and now[1] == word :
            star.close()
            return int(now_line.split("MEANING;")[0].split(";")[0])
    star.close()
    return -1

def findAtStar_index(index):    
    star = open("data/star/STAR.txt","r",encoding="UTF-8")
    star_lines = star.readlines()
    return index < len(star_lines) and star_lines[index] != ""

def glue(str_list,insert):
    string = str_list[0]
    length = len(str_list)
    for i in range(1,length) :
        string = string + insert + str_list[i]
    return string    