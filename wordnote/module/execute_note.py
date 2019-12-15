from module.tool import *

def addnote(note_name):
    note = open("data/note/"+note_name+".wordnote.txt","w",encoding="UTF-8")
    note.close()
    notelist = open("data/star/NOTELIST.txt","r",encoding="UTF-8")
    notelist_lines = notelist.read().split("\n")
    notelist.close()
    length = len(notelist_lines)
    for i in range(length) :
        if notelist_lines[i] == "" :
            notelist_lines[i] = note_name
            break
    notelist = open("data/star/NOTELIST.txt","w",encoding="UTF-8")
    notelist.write(glue(notelist_lines,"\n"))
    if not "" in notelist_lines :
        notelist.write("\n")
    notelist.close()
    print("성공적으로 단어장를 만들었습니다. 단어장 이름 : "+note_name)

def removenote(note_name):
    notelist = open("data/star/NOTELIST.txt","r",encoding="UTF-8")
    notelist_lines = notelist.read().split("\n")
    notelist.close()
    length = len(notelist_lines)
    for i in range(length) :
        if notelist_lines[i] == note_name :
            notelist_lines[i] = ""
            break
    if notelist_lines[length-1] == "" :
        notelist_lines = notelist_lines[:length-1]
    notelist = open("data/star/NOTELIST.txt","w",encoding="UTF-8")
    notelist.write(glue(notelist_lines,"\n")+"\n")
    notelist.close()
    os.remove(note_dir+"/"+note_name+".wordnote.txt")
    print("성공적으로 단어장을 삭제하였습니다. 단어장 이름 : "+note_name)

def connectnote(note_name):
    working_note = open("data/work/"+note_name+".working-on.txt","w",encoding="UTF-8")
    origin_note = open("data/note/"+note_name+".wordnote.txt","r",encoding="UTF-8")
    origin_note_line = origin_note.readlines()
    origin_note.close()
    length = len(origin_note_line)
    for i in range(length) :
        working_note.write(origin_note_line[i])
    working_note.close()
    setNNN(note_name)
    print("성공적으로 단어장에 접근했습니다. 단어장 이름 : "+getNNN())

def disconnectnote():
    working_note = open("data/work/"+getNNN()+".working-on.txt","r",encoding="UTF-8")
    origin_note = open("data/note/"+getNNN()+".wordnote.txt","w",encoding="UTF-8")
    working_note_line = working_note.readlines()
    working_note.close()
    for now_line in working_note_line :
        origin_note.write(now_line)
    origin_note.close()
    os.remove(work_dir+"/"+getNNN()+".working-on.txt")
    print("접근한 단어장에서 벗어납니다. 단어장 이름 : "+getNNN())
    resetNNN()

def end():
    import sys
    print("프로그램을 종료합니다.")
    sys.exit()

def mergenote(notelist,notename) :
    merged = {}
    for now in notelist :
        now_note = open("data/note/"+now+".wordnote.txt","r",encoding="UTF-8")
        notelines = now_note.read().split("\n")
        now_note.close()
        for nowline in notelines :
            if nowline != "":
                james = nowline.split(";WordAt")[1].split(";")
                james.remove("")
                length = len(james)

                for i in range(length) :
                    james[i] = int(james[i])

                if not james[0] in merged.keys() :
                    merged[james[0]] = set()
                merged[james[0]].update(james[1:])
    
    merged_key = list(merged.keys())
    merged_key.sort()
    merged_note = open("data/note/"+notename+".wordnote.txt","w",encoding="UTF-8")
    length = len(merged_key)

    for i in range(length) :
        line = str(i) + ";WordAt" + str(merged_key[i]) + ";" + glue(list(merged[merged_key[i]]),";") + ";\n"
        merged_note.write(line)
    
    notelist = open("data/star/NOTELIST.txt","r",encoding="UTF-8")
    notelist_lines = notelist.read().split("\n")
    notelist.close()
    length = len(notelist_lines)
    for i in range(length) :
        if notelist_lines[i] == "" :
            notelist_lines[i] = note_name
            break
    notelist = open("data/star/NOTELIST.txt","w",encoding="UTF-8")
    notelist.write(glue(notelist_lines,"\n"))
    if not "" in notelist_lines :
        notelist.write("\n")
    notelist.close()

    merged_note.close()
    print("성공적으로 단어장를 합병했습니다. 단어장 이름 : "+notename)

def notelist():
    print("단어장 목록 : "+glue(getNoteList(),", "))