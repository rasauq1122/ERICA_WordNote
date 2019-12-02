import os

module_dir = os.getcwd()
main_dir = os.getcwd().split("/module")[0]
note_dir = main_dir+"/note"

if not(os.path.isdir(note_dir)) :
    os.makedirs(note_dir)

now_note_name = ""
word_count = -1

def connectnote(note_name):
    os.chdir(note_dir)
    global now_note_name, word_count
    now_note_name = note_name

    if os.path.isfile(note_dir+"/"+note_name+".txt") :
        connected_note = open(note_name+"_working-on.txt","w",encoding="UTF-8")
        origin_note = open(note_name+".txt","r",encoding="UTF-8")
        origin_string = origin_note.readlines()
        origin_note.close()
        for now_string in origin_string :
            if now_string.find("THIS IS THE END OF WORDNOTE.") != -1 :
                total = now_string.split(" TOTAL NUMBER OF WORDS : ")[1]
                if total.isdigit() :
                    word_count = int(total)
                break
            else :
                connected_note.write(now_string)
        if (word_count == -1) :
            print("올바른 단어장의 형식이 아닙니다. 접근하지 못했습니다.")
        else :
            print("성공적으로 단어장에 접근했습니다. 단어장 이름 : "+note_name)
        connected_note.close()
    else :
        print("존재하지 않는 단어장입니다. 접근하지 못했습니다.")
        
    os.chdir(module_dir)

def disconnectnote():
    os.chdir(note_dir)
    global word_count, now_note_name

    if word_count == -1 :
        print("접근한 단어장이 없습니다.")
    else :
        now_note = open(now_note_name+".txt","w",encoding="UTF-8")
        connected_note = open(now_note_name+"_working-on.txt","r",encoding="UTF-8") # 예외처리 : 있는 지 확인해야 함
        connected_string = connected_note.readlines()
        connected_note.close()
        for now_string in connected_string :
            now_note.write(now_string)
        now_note.write("THIS IS THE END OF WORDNOTE. TOTAL NUMBER OF WORDS : "+str(word_count))
        now_note.close()
        os.remove(note_dir+"/"+now_note_name+"_working-on.txt")
        print("접근한 단어장에서 벗어납니다. 단어장 이름 : "+now_note_name)
        now_note_name = ""
        word_count = -1