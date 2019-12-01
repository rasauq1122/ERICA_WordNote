import os

module_dir = os.getcwd()
main_dir = os.getcwd().split("/module")[0]
note_dir = main_dir+"/note"

def addnote(note_name):
    os.chdir(note_dir)
    
    if not(os.path.isfile(note_dir+"/"+note_name+".txt")):
        note = open(note_name+".txt","w",encoding="UTF-8")
        print("성공적으로 단어장를 만들었습니다. 단어장 이름 : "+note_name)
    else :
        check = "init"
        while not(check in ["y","yes","n","no"]):
            check = input("이미 같은 이름의 단어장이 있습니다. 지우고 새로 만듭니까? [y/n] ")
            if check.strip().isalpha():
                check = check.strip().lower()
            else :
                continue
        if check in ["y","yes"]:
            note = open(note_name+".txt","w",encoding="UTF-8")
            print("성공적으로 단어장를 만들었습니다. 단어장 이름 : "+note_name)
        else :
            print("단어장을 새로 만들지 못했습니다.")

    os.chdir(module_dir)
