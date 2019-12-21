import os
import re
import datetime

def checkLast(main_string,clue):
    clue_length = len(clue)
    main_length = len(main_string)
    return main_string[main_length-clue_length:] == clue

now_dir = os.getcwd()
directoies = ["/data","/module","/data/note","/data/star","/data/work","/data/view"]
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
view_dir = main_dir+directoies[5]

start_view = "┌"+"─"*149+"┐"
middle_view = "├"+"─"*149+"┤"
end_view = "└"+"─"*149+"┘"

def get_yes_or_no(notice):
    check = input(notice+" [y/n] ")
    log = open("data/log.txt","a",encoding="UTF-8")
    log.write(str(datetime.datetime.now())+" : "+check+"\n")
    log.close()
    while not check in ["y","yes","n","no"] :
        check = input("다음 중 하나를 입력해주세요. [y, yes, n, no] ")
        log = open("data/log.txt","a",encoding="UTF-8")
        log.write(str(datetime.datetime.now())+" : "+check+"\n")
        log.close()
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
    if len(str_list) == 0:
        return ""
    string = str(str_list[0])
    length = len(str_list)
    for i in range(1,length) :
        string = string + insert + str(str_list[i])
    return string    

def len_kor(string):
    kor_char = re.compile("[ㄱ-ㅎ가-힣ㅏ-ㅣ]")
    length = 0
    for char in string:
        if kor_char.match(char) :
            length = length + 2
        else :
            length = length + 1
    return length

def count_kor(string,limit):
    kor_char = re.compile("[ㄱ-ㅎ가-힣ㅏ-ㅣ]")
    length = len(string)
    count = 0
    for index in range(length) :
        now = 0
        if kor_char.match(string[index]) :
            now = 2
        else :
            now = 1
        if count + now > limit :
            return index
        else :
            count = count + now
    return length - 1

def kor_cut(string,length):
    if length < 2:
        return []
    if len_kor(string) == 0:
        return []
    elif len_kor(string) <= length:
        return [string]
    else :
        return [string[:count_kor(string,length)]] + kor_cut(string[count_kor(string,length):],length)

def view_format(pre,str_list):
    good_len = 149-len_kor(pre)
    printer = []
    def invis(string, mod):
        if mod == 0 :
            return string
        else :
            return " "*len_kor(string)
    
    length = len(str_list)
    for i in range(length) :
        printer.append("│"+invis(pre,i)+str_list[i]+" "*(good_len-len_kor(str_list[i]))+"│")
        print(printer[i])
    return printer

def make_format(pre,str_list):
    good_len = 149-len_kor(pre)
    printer = []
    def invis(string, mod):
        if mod == 0 :
            return string
        else :
            return " "*len_kor(string)
    
    length = len(str_list)
    for i in range(length) :
        printer.append("│"+invis(pre,i)+str_list[i]+" "*(good_len-len_kor(str_list[i]))+"│")
    return printer

def getStarLine(index):
    star = open("data/star/STAR.txt","r",encoding="UTF-8")
    star_lines = star.readlines()
    star.close()
    if len(star_lines) > index :
        return star_lines[index]
    else :
        return ""

def makeview(string): # STAR 형식만 받음
    class_dictionary = {"n":1, "v":2, "a":3, "ad":4, "prep":5, "conj":6, "pron": 7, "int": 8, "NULL" : 9} 
    splited = string.split("MEANING;")
    length = len(splited)
    view = ["","","","","","","",""]
    
    for i in range(1,length) :
        parts = splited[i].split("tag;")
        meaning_part = parts[0]
        meaning_split = meaning_part.split(";")
        now_class = class_dictionary[meaning_split[0]]-1
        if now_class == 8 :
            continue
        view[now_class] = view[now_class] + "(" + str(i-1) + ") " + meaning_split[1]
        
        length2 = len(meaning_split)
        for j in range(2,length2-1) :
            view[now_class] = view[now_class] + ", " + meaning_split[j]

        if len(parts) == 2 :
            tag_split = parts[1].split(";")
            view[now_class] = view[now_class] + " # tag : " + tag_split[0]
            
            length2 = len(tag_split)
            for j in range(1,length2-1) :
                view[now_class] = view[now_class] + ", " + tag_split[j]
        view[now_class] = view[now_class] + ";"

    return view

def findAtNote(index):
    if getNNN() != "" :
        working_note = open("data/work/"+getNNN()+".working-on.txt","r",encoding="UTF-8")
        working_lines = working_note.readlines()
        working_note.close()
        
        length = len(working_lines)
        for i in range(length) :
            if working_lines[i].find("WordAt"+str(index)) != -1:
                return i
    return -1

def getNoteLine(index):
    if getNNN() != "" :
        working_note = open("data/work/"+getNNN()+".working-on.txt","r",encoding="UTF-8")
        working_lines = working_note.readlines()
        working_note.close()
        length = len(working_lines)
        
        if index < length :
            return working_lines[index]
    return ""

def mergeNoteLine(string): # note 형식만 받음
    if string == "":
        return ""
    note_splited = string.split(";WordAt")
    james = note_splited[1].split(";")
    star_line = getStarLine(int(james[0]))
    length = len(james)

    star_splited = star_line.split("MEANING;")
    now_line = star_splited[0] 
    
    for i in range(1,length-1) : # 예외처리 필요
        now_line = now_line + "MEANING;" + star_splited[int(james[i])+1]

    return now_line

def getNoteList():
    notelist = open("data/star/NOTELIST.txt","r",encoding="UTF-8")
    splited = notelist.read().split("\n")
    while "" in splited :
        splited.remove("")
    notelist.close()
    return splited

def isNoteHaving(note_name,star_index):
    havings = []
    if os.path.isfile(note_dir+"/"+note_name+".wordnote.txt") :
        note = open("data/note/"+note_name+".wordnote.txt","r",encoding="UTF-8")
        note_lines = note.read().split("\n")
        for now in note_lines :
            if now.find("WordAt"+str(star_index)) != -1 :
                havings = normalSplit(now,"WordAt")[1].split(";")[1:]
                havings.remove("")
                break
    return havings

def sortbynumber(can_int_str_list):
    length = len(can_int_str_list)
    for i in range(length) :
        if not can_int_str_list[i].isdecimal() :
            return []
        can_int_str_list[i] = int(can_int_str_list[i])
    can_int_str_list.sort()
    for i in range(length) :
        can_int_str_list[i] = str(can_int_str_list[i])
    return can_int_str_list

def make_log(string):
    log = open("data/log.txt","a",encoding="UTF-8")
    log.write(str(datetime.datetime.now())+" : "+string+"\n")
    log.close()

def makeview2(noteline):
    starline = mergeNoteLine(noteline)
    class_dictionary = {"n":1, "v":2, "a":3, "ad":4, "prep":5, "conj":6, "pron": 7, "int": 8, "NULL" : 9} 
    note_sp = normalSplit(noteline,";WordAt")[1].split(";")[1:]
    splited = starline.split("MEANING;")
    length = len(splited)
    view = ["","","","","","","",""]
    
    for i in range(1,length) :
        parts = splited[i].split("tag;")
        meaning_part = parts[0]
        meaning_split = meaning_part.split(";")
        now_class = class_dictionary[meaning_split[0]]-1
        if now_class == 8 :
            continue
        view[now_class] = view[now_class] + "(" + note_sp[i-1] + ") " + meaning_split[1]
        
        length2 = len(meaning_split)
        for j in range(2,length2-1) :
            view[now_class] = view[now_class] + ", " + meaning_split[j]

        if len(parts) == 2 :
            tag_split = parts[1].split(";")
            view[now_class] = view[now_class] + " # tag : " + tag_split[0]
            
            length2 = len(tag_split)
            for j in range(1,length2-1) :
                view[now_class] = view[now_class] + ", " + tag_split[j]
        view[now_class] = view[now_class] + ";"

    return view