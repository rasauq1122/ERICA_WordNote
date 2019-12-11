from module.tool import *

def giveword(wordlist):
    word = ""
    class_list = ["n", "v", "a", "ad", "prep", "conj", "pron", "int"]
    for i in range(8) :
        group_length = len(wordlist[i+1])
        for j in range(group_length) :
            word = word + "MEANING;" + class_list[i] + ";"
            word_count = len(wordlist[i+1][j])
            for k in range(word_count) :
                word = word + wordlist[i+1][j][k]
                if k < word_count-1 :
                    word = word + ","
            word = word + ";"
            if j in wordlist[9][i].keys() :
                word = word + "tag" + ";"
                tag = wordlist[9][i][j]
                tag_count = len(tag)
                for k in range(tag_count) :
                    word = word + tag[k]
                    if k < tag_count-1 :
                        word = word + ","
                word = word + ";"
    word = word + "\n"
    return word

def newword(wordlist):
    star = open("data/star/STAR.txt","r+",encoding="UTF-8")
    star_linelist = star.readlines()
    count = 0
    for now_line in star_linelist :
        if now_line == "":
            break
        count = count + 1
        star.readline()
    word = str(count)+";"+wordlist[0]+";"+giveword(wordlist)
    star.write(word)
    star.close()
    print("새로운 단어를 등록했습니다 : "+wordlist[0])

    if getNNN() != "" and get_yes_or_no("현재 단어장 ("+getNNN()+") 에 단어를 추가합니까?") :
        working_note = open("data/work/"+getNNN()+".working-on.txt","r+",encoding="UTF-8")
        working_note_lines = working_note.readlines()
        word_index = 0
        for now_line in working_note_lines :
            if now_line == "":
                break
            word_index = word_index + 1
            working_note.readline()
            
        pointer = str(word_index) + ";WordAt" + str(count) + ";"
        word_index = len(word.split("MEANING;")) - 1
        for i in range(word_index) :
            pointer = pointer + str(i) + ";"
        pointer = pointer + "\n"
        working_note.write(pointer)
        working_note.close()
        print("단어장에 새로운 단어를 등록했습니다.")

def appendword(wordlist):
    star = open("data/star/STAR.txt","r",encoding="UTF-8")
    meanings = star.readlines()
    
    start_index = len(meanings[wordlist[0]].split("MEANING;"))
    meanings[wordlist[0]] = meanings[wordlist[0]][:len(meanings[wordlist[0]])-1]
    meanings[wordlist[0]] = meanings[wordlist[0]] + giveword(wordlist)

    wordname = meanings[wordlist[0]].split("MEANING;")[0].split(";")[1]
    end_index = len(meanings[wordlist[0]].split("MEANING;"))
    
    star.close()
    star = open("data/star/STAR.txt","w",encoding="UTF-8")
    star.write(glue(meanings,""))
    star.close()
    print("기존 단어에 새로운 뜻을 등록했습니다 : "+wordname)

    if getNNN() != "":
        working_note = open("data/work/"+getNNN()+".working-on.txt","r",encoding="UTF-8")
        working_lines = working_note.readlines()
        working_note.seek(0)
        if working_note.read().find("WordAt"+str(wordlist[0])+";") != -1 and get_yes_or_no("현재 단어장 ("+getNNN()+") 에 새로 등록한 뜻을 추가합니까?") :
            working_length = len(working_lines)
            for i in range(working_length) :
                if working_lines[i].find("WordAt"+str(wordlist[0])+";") != -1 :
                    working_lines[i] = working_lines[i][:len(working_lines[i])-1]
                    for j in range(start_index,end_index) :
                        working_lines[i] = working_lines[i] + str(j) + ";"
                    working_note.close()
                    working_note = open("data/work/"+getNNN()+".working-on.txt","w",encoding="UTF-8")
                    working_note.write(glue(working_lines,""))
                    break
            print("단어장에 새로운 뜻을 등록했습니다.")
        working_note.close()