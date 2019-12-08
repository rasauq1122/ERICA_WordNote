from module.tool import *

def addword(wordlist): # 기존에 없는 단어라면 여기로
    os.chdir(star_dir)
    star = open("STAR.txt","r+",encoding="UTF-8")
    star_linelist = star.readlines()
    count = 0
    for now_line in star_linelist :
        count = count + 1
        star.readline()
    word = str(count)+";"+wordlist[0]+";"
    class_list = ["n", "v", "a", "ad", "prep", "conj", "pron", "int"] # 예약어 처리할 것
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
    star.write(word)
    star.close()
    os.chdir(work_dir)
    working_note = open(getNNN(work_dir)+".working-on.txt","r+",encoding="UTF-8")
    working_note_lines = working_note.readlines()
    wn_count = 0
    for now_line in working_note_lines :
        wn_count = wn_count + 1
        working_note.readline()
    pointer = str(wn_count) + ";" + str(count) + ";"
    word_count = len(word.split(";MEANING;")) - 1
    for i in range(word_count) :
        pointer = pointer + str(i) + ";"
    pointer = pointer + "\n"
    working_note.write(pointer)
    working_note.close()