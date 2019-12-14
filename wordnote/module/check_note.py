from module.decode_note import *

def check_addnote(note_name):
    if note_name == "" :
        print("단어장의 이름은 최소 한 글자 이상이어야 합니다.")
        return
    if note_name.find(".wordnote.txt") != -1 :
        print("예약어는 단어장의 이름으로 사용할 수 없습니다.")
        return
    notelist = open("data/star/NOTELIST.txt","r",encoding="UTF-8")
    notelist_reading = notelist.read()
    notelist.close()
    if notelist_reading.find(note_name+"\n") != -1 :
        okay = get_yes_or_no("이미 같은 이름의 단어장이 존재합니다. 지우고 새로 만들까요?")
        if okay :
            addnote(note_name)
        else :
            print("단어장을 새로 만들지 못했습니다.")
    else :
        addnote(note_name)

def check_removenote(note_name):
    notelist = open("data/star/NOTELIST.txt","r",encoding="UTF-8")
    notelist_reading = notelist.read()
    notelist.close()
    if getNNN() != "":
        print("접속 중인 단어장이 있으면 사용할 수 없는 명령어입니다.")
        return
    if notelist_reading.find(note_name+"\n") != -1 and os.path.isfile(note_dir+"/"+note_name+".wordnote.txt") :
        if get_yes_or_no("정말 단어장을 삭제할까요?") :
            removenote(note_name)
        else :
            print("단어장을 삭제하지 않았습니다.")
    else :
        print("존재하지 않는 단어장을 삭제할 수 없습니다.")

def check_noteform(note_name,note_line):
    return True 

def check_connectnote(note_name):
    if getNNN() == "" :
        if os.path.isfile(note_dir+"/"+note_name+".wordnote.txt") :
            now_note = open("data/note/"+note_name+".wordnote.txt","r",encoding="UTF-8")
            note_line = now_note.readlines()
            now_note.close()
            if check_noteform(note_name,note_line) :
                connectnote(note_name)
            else :
                print("단어장의 형식이 올바르지 않아 접근할 수 없습니다.")
        else :
            print("존재하지 않는 단어장에 접근할 수 없습니다.")
    else :
        print("이미 접근 중인 단어장이 존재합니다. 단어장 이름 : "+getNNN())

def check_disconnectnote(string):
    if string != "":
        print("해당 명령어는 어떤 옵션도 넣을 수 없습니다.")
        return
    if getNNN() != "" :
        disconnectnote()
    else :
        print("접근한 단어장이 없습니다.")

def check_end(setting):
    if setting == "" :
        check_disconnectnote("")
        end()
    else :
        print("해당 명령어는 어떤 옵션도 넣을 수 없습니다.")
        return