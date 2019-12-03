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

def normalSplit(given_string, clue):
    where = given_string.find(clue)
    if where == -1 :
        return [given_string]
    else :
        return [given_string[:where],given_string[where+len(clue):]]

def superSplit(given_string):
    len_over = len(given_string) + 1
    meaning_list = []
    now_meaning_list = []
    while True:
        if minus2max(given_string.find(";"),len_over) < minus2max(given_string.find(","),len_over) :
            splited = normalSplit(given_string,";")
            if splited[0].strip() != "" :
                now_meaning_list = now_meaning_list + [splited[0].strip()]
            if now_meaning_list != [] :
                meaning_list = meaning_list + [now_meaning_list]
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
        meaning_list = meaning_list + [now_meaning_list]
    return meaning_list


def addDecoding(setting): # setting은 올바른 입력이라는 것이 보장될 예정
    word_name = setting.split(" -")[0]
    part_of_class = [word_name, [], [], [], [], [], [], [], [], []]
    class_dictionary = {"n":1, "v":2, "a":3, "ad":4, "prep":5, "conj":6, "pron": 7, "int": 8, "tag":9}

    now_string = setting[:]
    while now_string.find(" -") != -1 :
        working_string = now_string.split(" -")[0]
        now_class = class_dictionary[working_string.split(" ")[0]]
        # superSplit 을 이용하여 단어 추가 및 tag 예외 처리 필요 