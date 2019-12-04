from module.note import *

def check_addnote(note_name):
    os.chdir(note_dir)
    if os.path.isfile(note_dir+"/"+note_name+".txt") :
        okay = get_yes_or_no("이미 같은 이름의 단어장이 존재합니다. 지우고 새로 만들까요?")
        if okay :
            addnote(note_name)
        else :
            print("단어장을 새로 만들지 못했습니다.")
    else :
        addnote(note_name)
    os.chdir(module_dir)

def check_removenote(note_name):
    os.chdir(note_dir)
    if os.path.isfile(note_dir+"/"+note_name+".txt") :
        if get_yes_or_no("정말 단어장을 삭제할까요?") :
            removenote(note_name)
        else :
            print("단어장을 삭제하지 않았습니다.")
    else :
        print("존재하지 않는 단어장을 삭제할 수 없습니다.")
    os.chdir(module_dir)

def check_noteform(note_name,note_line):
    if note_line[0].find("THIS IS THE START OF WORDNOTE. WORDNOTE NAME : "+note_name) == -1 :
        return False
    if note_line[len(note_line)-1].find("THIS IS THE END OF WORDNOTE. TOTAL NUMBER OF WORDS : "+str(len(note_line)-2)) == -1 :
        return False
    return True 

def check_connectnote(note_name):
    os.chdir(note_dir)
    if getNNN(note_dir) == "" :
        if os.path.isfile(note_dir+"/"+note_name+".txt") :
            print(os.getcwd())
            now_note = open(note_name+".txt","r",encoding="UTF-8")
            note_line = now_note.readlines()
            now_note.close()
            if check_noteform(note_name,note_line) :
                connectnote(note_name)
            else :
                print("단어장의 형식이 올바르지 않아 접근할 수 없습니다.")
        else :
            print("존재하지 않는 단어장에 접근할 수 없습니다.")
    else :
        print("이미 접근 중인 단어장이 존재합니다. 단어장 이름 : "+getNNN(note_dir))
    os.chdir(module_dir)

def check_disconnectnote():
    if getNNN(module_dir) != "" :
        disconnectnote()
    else :
        print("접근한 단어장이 없습니다.")