from module.tool import *

def addword(wordlist):
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
        group_boot = False
        for j in range(group_length) :
            if not group_boot :
                word = word + class_list[i] + ";"
                group_boot = True
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