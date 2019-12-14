from module.execute_word import *

# n : 명사
# v : 동사
# a : 형용사
# ad : 부사
# prep : 전치사
# conj : 접속사
# pron : 대명사
# int : 감탄사

# : apple -n 사과 -v 사과하다 -a 사과가 먹고 싶은 -ad 사과처럼 -prep 사과에 의한 -conj 그러나 -pron 사과 -int 빵상

def minus2max(given_int, max_len):
    if given_int < 0 :
        return max_len
    else :
        return given_int

def superSplit(given_string):
    len_over = len(given_string) + 1
    all_meaning_list = []
    now_meaning_list = []
    while True:
        if minus2max(given_string.find(";"),len_over) < minus2max(given_string.find(","),len_over) :
            splited = normalSplit(given_string,";")
            if splited[0].strip() != "" :
                now_meaning_list = now_meaning_list + [splited[0].strip()]
            if now_meaning_list != [] :
                all_meaning_list = all_meaning_list + [now_meaning_list]
            now_meaning_list = []
            if len(splited) == 1:
                break
            else :
                given_string = splited[1][:]
        else :
            splited = normalSplit(given_string,",")
            if splited[0].strip() != "" :
                now_meaning_list = now_meaning_list + [splited[0].strip()]
            if len(splited) == 1:
                break
            else :
                given_string = splited[1][:]
    if now_meaning_list != [] :
        all_meaning_list = all_meaning_list + [now_meaning_list]
    return all_meaning_list

def decode_meaningoption(splited):
    class_dictionary = {"n":1, "v":2, "a":3, "ad":4, "prep":5, "conj":6, "pron": 7, "int": 8, "tag":9} # 레벨도 있으면 좋긴 할텐데
    part_of_class = [splited[0].strip(), [], [], [], [], [], [], [], []]
    tags = [{}, {}, {}, {}, {}, {}, {}, {}]
    counts = [0, 0, 0, 0, 0, 0, 0, 0]
    splited.remove(splited[0])

    log = [0, 0, 0]
    for details in splited :
        now_class = class_dictionary[normalSplit(details," ")[0]]
        if now_class == 9 :
            now_tag = normalSplit(details," ")[1].split(",")
            length = len(now_tag)
            for i in range(length) :
                now_tag[i] = now_tag[i].strip()
            while "" in now_tag :
                now_tag.remove("")
            if now_tag != [] :
                for i in range(log[1],log[2]+1) :
                    tags[log[0]-1][i] = list(set(now_tag))
        elif len(normalSplit(details," ")) == 2 :
            now_meaning = superSplit(normalSplit(details," ")[1])
            now_count = counts[now_class-1]
            part_of_class[now_class] = part_of_class[now_class] + now_meaning
            log = [now_class, now_count, now_count + len(now_meaning)-1]
            counts[now_class-1] = now_count + len(now_meaning)
        
    return part_of_class + [tags]

def decode_newword(setting):
    splited = setting.split(" -")
    newword(decode_meaningoption(splited))

def decode_appendword(setting):
    splited = setting.split(" -")
    decoding = decode_meaningoption(splited)
    if decoding[0].isdecimal() :
        decoding[0] = int(decoding[0])
    else :
        decoding[0] = findAtStar(decoding[0])
    appendword(decoding)

def decode_viewword(setting):
    star_mod = False
    splited = setting.split(" -")
    for now in splited :
        if now.strip() == "star" :
            star_mod = True
    viewword(setting.split(" -")[0],[star_mod])

def decode_pullword(setting):
    word = setting.split(" -opt")[0].strip()
    options = setting.split(" -opt")[1].split(",")
    star_index = findAtStar(word)
    working_note = open("data/work/"+getNNN()+".working-on.txt","r",encoding="UTF-8")
    working_lines = working_note.readlines()
    working_note.close()
    length = len(working_lines)
    log = []
    
    cnt = -1
    for i in range(length) :
        if working_lines[i].find("WordAt"+str(star_index)) != -1 :
            cnt = i
            break
    if cnt == -1 :
        cnt = length

    length = len(options)
    for i in range(length) :
        options[i] = options[i].strip()
    
    while "" in options:
        options.remove("")

    length = len(options)
    for i in range(length) :
        if not options[i] in log :
            log = log + [options[i]]
    
    pullword(cnt,star_index,log)

def decode_eraseword(setting):
    word = setting.split(" -opt")[0].strip()
    options = setting.split(" -opt")[1].split(",")
    star_index = findAtStar(word)
    note_index = findAtNote(star_index)
    james = normalSplit(getNoteLine(note_index),";WordAt")[1].split(";")[1:]
    length = len(options)
    for i in range(length) :
        options[i] = options[i].strip()
    log = []
    for now in james :
        if not (now in options or now == "\n"):
            log = log + [now]
    return eraseword(note_index,star_index,log)