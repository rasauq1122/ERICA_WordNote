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
                    word = word + ";"
            word = word + ";"
            if j in wordlist[9][i].keys() :
                word = word + "tag" + ";"
                tag = wordlist[9][i][j]
                tag_count = len(tag)
                for k in range(tag_count) :
                    word = word + tag[k]
                    if k < tag_count-1 :
                        word = word + ";"
                word = word + ";"
    return word

def newword(wordlist):
    star = open("data/star/STAR.txt","r",encoding="UTF-8")
    star_linelist = star.read().split("\n")
    star.close()
    count = 0
    while star_linelist[count] != "" :
        count = count + 1
    star_linelist[count] = str(count)+";"+wordlist[0]+";"+giveword(wordlist)
    star = open("data/star/STAR.txt","w",encoding="UTF-8")
    star.write(glue(star_linelist,"\n")+"\n")
    star.close()
    print("새로운 단어를 등록했습니다 : "+wordlist[0])
    index_list = list(range(len(star_linelist[count].split("MEANING;"))-1))

    if getNNN() != "" :
        working_note = open("data/work/"+getNNN()+".working-on.txt","r",encoding="UTF-8")
        working_note_lines = working_note.read().split("\n")
        working_note.close()
        word_index = 0
        while working_note_lines[word_index] != "" :
            word_index = word_index + 1
        working_note_lines[word_index] = str(word_index)+";WordAt"+str(count)+";"+glue(index_list,";")+";"
        working_note = open("data/work/"+getNNN()+".working-on.txt","w",encoding="UTF-8")
        working_note.write(glue(working_note_lines,"\n")+"\n")
        working_note.close()
        print("단어장("+getNNN()+")에 새로운 단어를 등록했습니다.")

def appendword(wordlist):
    star = open("data/star/STAR.txt","r",encoding="UTF-8")
    meanings = star.read().split("\n")
    star.close()
    splited = meanings[wordlist[0]].split("MEANING;")
    james = giveword(wordlist).split("MEANING;")
    wordname = meanings[wordlist[0]].split("MEANING;")[0].split(";")[1]
    while "" in james :
        james.remove("")
    index_list = []
    
    length1 = len(splited)
    for i in range(1,length1-1) :
        if splited[i] == "NULL;" :
            index_list = index_list + [i-1]
            splited[i] = james[0]
            james.remove(james[0])
            if james == [] :
                break
    meanings[wordlist[0]] = glue(splited,"MEANING;")
    if james != [] :
        meanings[wordlist[0]] = meanings[wordlist[0]] + "MEANING;" + glue(james,"MEANING;")
        index_list = index_list + list(range(length1-1,length1+len(james)-1))

    star = open("data/star/STAR.txt","w",encoding="UTF-8")
    star.write(glue(meanings,"\n"))
    star.close()

    if getNNN() != "" :
        if findAtNote(wordlist[0]) == -1 :
            working_note = open("data/work/"+getNNN()+".working-on.txt","r",encoding="UTF-8")
            working_note_lines = working_note.read().split("\n")
            working_note.close()
            word_index = 0
            while working_note_lines[word_index] != "" :
                word_index = word_index + 1
            working_note_lines[word_index] = str(word_index)+";WordAt"+str(wordlist[0])+";"+glue(index_list,";")+";"
        else :
            working_note = open("data/work/"+getNNN()+".working-on.txt","r",encoding="UTF-8")
            working_note_lines = working_note.read().split("\n")
            working_note.close()
            index = findAtNote(wordlist[0])
            working_note_lines[index] = working_note_lines[index] + glue(index_list,";") + ";" 
        working_note = open("data/work/"+getNNN()+".working-on.txt","w",encoding="UTF-8")
        working_note.write(glue(working_note_lines,"\n"))
        working_note.close()        
        print("단어장("+getNNN()+")에 새로운 뜻을 추가했습니다 : "+wordname)
        return
    print("단어장에 새로운 뜻을 추가했습니다 :"+wordname)

def viewword(word,modlist):
    nowword = word
    star_index = findAtStar(nowword)
    print(start_view)
    if modlist[0] :
        view_format("",[nowword+" (STAR : "+str(star_index)+")"])
        print(middle_view)
        view_list = makeview(getStarLine(star_index))
        class_list = ["n", "v", "a", "ad", "prep", "conj", "pron", "int"]
        for i in range(8) :
            splited = view_list[i].split(";")
            james = []
            for now in splited :
                james = james + kor_cut(now,149-len(class_list[i])-2)
            view_format(class_list[i]+". ",james)
    else :
        note_index = findAtNote(star_index)
        view_format("",[nowword+" ("+getNNN()+" : "+str(note_index)+", "+"STAR : "+str(star_index)+")"])
        print(middle_view)
        view_list = makeview(mergeNoteLine(getNoteLine(note_index)))
        class_list = ["n", "v", "a", "ad", "prep", "conj", "pron", "int"]
        for i in range(8) :
            splited = view_list[i].split(";")
            james = []
            for now in splited :
                james = james + kor_cut(now,149-len(class_list[i])-2)
            view_format(class_list[i]+". ",james)
    print(end_view)

def pullword(index,star_index,pointers):
    working_note = open("data/work/"+getNNN()+".working-on.txt","r",encoding="UTF-8")
    working_lines = working_note.readlines()
    working_note.close()
    if index == len(working_lines) :
        working_lines.append(str(index)+";WordAt"+str(star_index)+";")
    james = normalSplit(working_lines[index],";WordAt")[1].split(";")[1:]
    
    for now in james :
        if now.strip() != "" and not now.strip() in pointers:
            pointers = pointers + [now.strip()]
    
    pointers = sortbynumber(pointers)

    working_lines[index] = str(index)+";WordAt"+str(star_index)+";"
    for now in pointers :
        working_lines[index] = working_lines[index] + now + ";"
    working_lines[index] = working_lines[index] + "\n"
    working_note = open("data/work/"+getNNN()+".working-on.txt","w",encoding="UTF-8")
    working_note.writelines(working_lines)
    working_note.close()
    print("성공적으로 단어의 뜻을 불러왔습니다.")

def eraseword(index,star_index,pointers):
    working_note = open("data/work/"+getNNN()+".working-on.txt","r",encoding="UTF-8")
    working_lines = working_note.readlines()
    working_note.close()

    pointers = sortbynumber(pointers)

    if pointers == [] :
        working_lines[index] = ""
        print("해당 영단어가 접속중인 단어장에서 완전히 지워집니다.")
    else :
        working_lines[index] = str(index) +";WordAt" + str(star_index) + ";"
        for now in pointers :
            working_lines[index] = working_lines[index] + now + ";"
    working_lines[index] = working_lines[index] + "\n"
    working_note = open("data/work/"+getNNN()+".working-on.txt","w",encoding="UTF-8")
    working_note.writelines(working_lines)
    working_note.close()
    print("성공적으로 단어의 뜻을 삭제하였습니다.")

def minidelete(star_index,note_name,pointers):
    havings = isNoteHaving(note_name,star_index)
    for now in pointers :
        havings.remove(now)
    havings = sortbynumber(havings)
    
    note = open("data/note/"+note_name+".wordnote.txt","r",encoding="UTF-8")
    note_lines = note.read().split("\n")
    note.close()
    index = -1
    for now in note_lines :
        if now.find("WordAt"+str(star_index)) != -1 :
            index = int(now.split(";")[0])
            break
    if havings == [] :
        note_lines[index] = ""
    else :
        note_lines[index] = str(index) +";WordAt" + str(star_index) + ";"
        for now in havings :
            note_lines[index] = note_lines[index] + now + ";"
    note = open("data/note/"+note_name+".wordnote.txt","w",encoding="UTF-8")
    note.write(glue(note_lines,"\n"))
    note.close()

def deleteword(star_index,star_pointers,pointers_dictionary):
    star = open("data/star/STAR.txt","r",encoding="UTF-8")
    star_lines = star.read().split("\n")
    star.close()
    star_now = star_lines[star_index].split("MEANING;")
    length = len(star_now)

    for now in star_pointers :
        star_now[now+1] = "NULL;"

    all_null = True
    for i in range(1,length) :
        if star_now[i] != "NULL;" :
            all_null = False
            break
    
    if all_null :
        star_lines[star_index] = ""
    else :
        star_lines[star_index] = glue(star_now,"MEANING;")
    
    star = open("data/star/STAR.txt","w",encoding="UTF-8")
    star_lines = star.write(glue(star_lines,"\n"))
    star.close()

    pointers_key = list(pointers_dictionary.keys())
    for now in pointers_key :
        minidelete(star_index,now,pointers_dictionary[now])
    
    print("성공적으로 단어를 삭제했습니다.")

def decode_modifyword(next_command, star_index, modi_index, overlay):
    now_line = getStarLine(star_index).split("MEANING;")[1:][modi_index]
    log = []
    mod = 0
    if overlay > -1 :
        mod = 1
    elif overlay < -1 :
        mod = 2

    splited = next_command.split(",")
    for now in splited :
        log.append(now.strip())

    if mod == 0 :
        return now_line.split("tag;")[0].split(";")[0] + ";" + glue(log,";")+";"
    elif mod == 1 :
        return now_line.split("tag;")[0]+glue(log,";")+";"
    
    now_line = now_line.split(";tag")[0].split(";")
    for now in log :
        now_line.remove(now)
    if len(now_line) <= 2 :
        return "NULL;"
    return glue(now_line,";")

def modifyword(next_command, star_index, modi_index, overlay):
    star = open("data/star/STAR.txt","r",encoding="UTF-8")
    star_lines = star.read().split("\n")
    star.close()
    meanings = star_lines[star_index].split("MEANING;")
    now_meaning = meanings[modi_index+1].split(";tag")
    now_meaning[0] = decode_modifyword(next_command,star_index,modi_index,overlay)

    if now_meaning[0] == "NULL;":
        now_meaning = ["NULL;"]
    meanings[modi_index+1] = glue(now_meaning,";tag")
    star_lines[star_index] = glue(meanings,"MEANING;")

    star = open("data/star/STAR.txt","r",encoding="UTF-8")
    star_check = star.read().split("\n")
    star.close()
    checker = star_check[star_index].split("MEANING")[1:]
    allnull = True
    for now in checker :
        if checker != "NULL" :
            allnull = False
            break
    
    if allnull :
        star_lines = []
        print("남아 있는 단어의 뜻이 없으므로 해당 영단어가 삭제됩니다.")
    star = open("data/star/STAR.txt","w",encoding="UTF-8") 
    star.write(glue(star_lines,"\n"))
    star.close()

    print("성공적으로 단어의 뜻을 수정했습니다.")

def checkword(setting):
    notelist = getNoteList()
    star_index = findAtStar(setting)
    boot = False
    for now in notelist :
        if isNoteHaving(now,star_index) != [] :
            if boot :
                print(", ",end="")
            else :
                print("참조하고 있는 단어장 목록 : ",end="")
            print(now,end="")
            boot = True
    if not boot :
        print("참조하고 있는 단어장이 없습니다.")
    else :
        print("")