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
                    tags[log[0]-1][i] = now_tag
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