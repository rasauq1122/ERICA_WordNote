from module.tool import *

if not(os.path.isdir(note_dir)) : # 추후 부팅 과정으로 넘길 것
    os.makedirs(note_dir)

def addnote(note_name):
    os.chdir(note_dir)
    note = open(note_name+".txt","w",encoding="UTF-8")
    note.write("THIS IS THE START OF WORDNOTE. WORDNOTE NAME : "+note_name+"\nTHIS IS THE END OF WORDNOTE. TOTAL NUMBER OF WORDS : 0\n")
    note.close()
    print("성공적으로 단어장를 만들었습니다. 단어장 이름 : "+note_name)
    os.chdir(module_dir)

def removenote(note_name):
    os.chdir(note_dir)
    os.remove(note_dir+"/"+note_name+".txt")
    print("성공적으로 단어장을 삭제하였습니다. 단어장 이름 : "+note_name)
    os.chdir(module_dir)

def connectnote(note_name):
    os.chdir(note_dir)
    working_note = open(note_name+".working-on.txt","w",encoding="UTF-8")
    origin_note = open(note_name+".txt","r",encoding="UTF-8")
    origin_note_line = origin_note.readlines()
    origin_note.close()
    length = len(origin_note_line) - 1
    for i in range(length) :
        working_note.write(origin_note_line[i])
    working_note.close()
    setNNN(note_name,note_dir)
    print("성공적으로 단어장에 접근했습니다. 단어장 이름 : "+getNNN(note_dir))
    os.chdir(module_dir)

def disconnectnote():
    os.chdir(note_dir)
    working_note = open(getNNN(note_dir)+".working-on.txt","r",encoding="UTF-8")
    origin_note = open(getNNN(note_dir)+".txt","w",encoding="UTF-8")
    working_note_line = working_note.readlines()
    working_note.close()
    for now_line in working_note_line :
        origin_note.write(now_line)
    origin_note.write("THIS IS THE END OF WORDNOTE. TOTAL NUMBER OF WORDS : "+str(len(working_note_line)-1)+"\n")
    origin_note.close()
    os.remove(note_dir+"/"+getNNN(note_dir)+".working-on.txt")
    print("접근한 단어장에서 벗어납니다. 단어장 이름 : "+getNNN(note_dir))
    resetNNN(note_dir)
    os.chdir(module_dir)