import os

module_dir = os.getcwd()
main_dir = os.getcwd().split("/module")[0]
note_dir = main_dir+"/note"

if not(os.path.isdir(note_dir)) :
    os.makedirs(note_dir)

def check_yes_or_no(notice):
    check = input(notice+" [y/n] ")
    while not check in ["y","yes","n","no"] :
        check = input("다음 중 하나를 입력해주세요. [y, yes, n, no] ")
        if check.strip().isalpha() :
            check = check.strip().lower()
        else :
            continue
    return check in ["y","yes"]

def addnote(note_name):
    os.chdir(note_dir)
    
    if not os.path.isfile(note_dir+"/"+note_name+".txt"):
        note = open(note_name+".txt","w",encoding="UTF-8")
        note.write("THIS IS THE START OF WORDNOTE. WORDNOTE NAME : "+note_name+"\nTHIS IS THE END OF WORDNOTE. TOTAL NUMBER OF WORDS : 0")
        print("성공적으로 단어장를 만들었습니다. 단어장 이름 : "+note_name)
        note.close()
    else :
        check = check_yes_or_no("이미 같은 이름의 단어장이 있습니다. 지우고 새로 만듭니까?")
        if check :
            note = open(note_name+".txt","w",encoding="UTF-8")
            note.write("THIS IS THE START OF WORDNOTE. WORDNOTE NAME : "+note_name+"\nTHIS IS THE END OF WORDNOTE. TOTAL NUMBER OF WORDS : 0")
            print("성공적으로 단어장를 만들었습니다. 단어장 이름 : "+note_name)
            note.close()
        else :
            print("단어장을 새로 만들지 못했습니다.")

    os.chdir(module_dir)

def removenote(note_name):
    os.chdir(note_dir)

    if os.path.isfile(note_dir+"/"+note_name+".txt") :
        check = check_yes_or_no("정말 단어장을 삭제하시겠습니까?")
        if check :
            os.remove(note_dir+"/"+note_name+".txt")
            print("단어장을 삭제하였습니다. 단어장 이름 : "+note_name)
        else :
            print("단어장을 삭제하지 않았습니다.")
    else :
        print("존재하지 않은 단어장입니다.")

    os.chdir(module_dir)