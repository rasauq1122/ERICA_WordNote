from module.tool import *

def addnote(note_name):
    note = open("data/note/"+note_name+".wordnote.txt","w",encoding="UTF-8")
    note.close()
    notelist = open("data/star/NOTELIST.txt","r",encoding="UTF-8")
    okay_append = notelist.read().find(note_name+"\n") == -1
    notelist.close()
    if okay_append :
        notelist = open("data/star/NOTELIST.txt","a",encoding="UTF-8")
        notelist.write(note_name+"\n")
        notelist.close()
    print("성공적으로 단어장를 만들었습니다. 단어장 이름 : "+note_name)

def removenote(note_name):
    notelist = open("data/star/NOTELIST.txt","r",encoding="UTF-8")
    notelist_reading = notelist.read()
    notelist.close()
    notelist_writing = normalSplit(notelist_reading,note_name+"\n")[0]
    if len(normalSplit(notelist_reading,note_name+"\n")) == 2 :
        notelist_writing = notelist_writing + normalSplit(notelist_reading,note_name+"\n")[1]
    notelist = open("data/star/NOTELIST.txt","w",encoding="UTF-8")
    notelist.write(notelist_writing)
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