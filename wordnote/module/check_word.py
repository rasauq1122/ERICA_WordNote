from module.decode_word import *

def check_meaningoption(splited):
    meansomething = False
    
    global meaning_option, tag_option
    meaning_option = ["n","v","a","ad","prep","conj","pron","int"]
    tag_option = ["tag"]
    length = len(splited)

    for i in range(1,length) :
        option_list = meaning_option + tag_option
        option = splited[i]
        option_main = normalSplit(option," ")[0]
        option_sub = ""
        if len(normalSplit(option," ")) == 2 :
            option_sub = normalSplit(option," ")[1]
        if not option_main in option_list :
            print("다음은 올바르지 않은 옵션입니다 : "+option_main)
            return False
        if option_main in tag_option :
            if option_sub.find(";") != -1 :
                print("태그에 세미콜론을 포함할 수 없습니다.")
                return False
        elif option_main in meaning_option :
            if option_sub != "" :
                meansomething = True

        option_detail = doublesplit(option_sub,",",";")
        for now_detail in option_detail :
            reserved = option_list + ["MEANING","NULL"]
            if now_detail.strip() in reserved :
                print("의미나 태그로 예약어를 사용할 수 없습니다 : "+now_detail)
                return False
    if not meansomething :
        print("의미 옵션을 추가해주세요.")
        return False  
    return True

def check_newword(command):
    splited = command.split(" -")
    if splited[0] == "" :
        print("영단어가 감지되지 않았습니다.")
        return
    for number in ["0","1","2","3","4","5","6","7","8","9"] :
        if splited[0].find(number) != -1 :
            print("영단어에 숫자를 포함하실 수 없습니다.")
            return
    if findAtStar(splited[0]) != -1 :
        print("이미 존재하는 영단어입니다. 인덱스 : ",str(findAtStar(splited[0])))
        print("해당 영단어를 단어장에 추가하고 싶다면 pullword 명령어를 사용하세요.")
        return
    length = len(splited)
    if length == 1 :
        print("의미 옵션을 추가해주세요.")
        return

    if check_meaningoption(splited) :
        decode_newword(command)

def check_appendword(command):
    splited = command.split(" -")
    if splited[0].isdecimal() :
        if not findAtStar_index(int(splited[0])) :
            print("해당 인덱스에 등록된 단어가 없습니다.")
            return
    else :
        if findAtStar(splited[0]) == -1 :
            print("등록되지 않는 영단어입니다 : "+splited[0])
            print("해당 영단어를 등록하고 싶다면 newword 명령어를 사용하세요.")
            return

    length = len(splited)
    if length == 1 :
        print("의미 옵션을 추가해주세요.")
        return

    if check_meaningoption(splited) :
        decode_appendword(command)