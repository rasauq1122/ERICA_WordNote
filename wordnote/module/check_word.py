from module.decode_word import *

def check_newword(command):
    if getNNN(module_dir) == "" :
        print("접속중인 단어장이 있어야 합니다.")
        return
    splited = command.split(" -")
    if splited[0] == "" :
        print("영단어가 감지되지 않았습니다.")
        return
    length = len(splited)
    if length == 1 :
        print("의미 옵션을 추가해주세요.")
        return

    meansomething = False
    
    global meaning_option, tag_option
    meaning_option = ["n","v","a","ad","prep","conj","pron","int"]
    tag_option = ["tag"]

    for i in range(1,length) :
        option_list = meaning_option + tag_option
        option = splited[i]
        option_main = normalSplit(option," ")[0]
        option_sub = ""
        if len(normalSplit(option," ")) == 2 :
            option_sub = normalSplit(option," ")[1]
        if not option_main in option_list :
            print("다음은 올바르지 않은 옵션입니다 : "+option_main)
            return
        if option_main in tag_option :
            if option_sub.find(";") != -1 :
                print("태그에 세미콜론을 포함할 수 없습니다.")
                return
        elif option_main in meaning_option :
            if option_sub != "" :
                meansomething = True

        option_detail = doublesplit(option_sub,",",";")
        for now_detail in option_detail :
            reserved = option_list + ["MEANING"]
            if now_detail.strip() in reserved :
                print("의미나 태그로 예약어를 사용할 수 없습니다 : "+now_detail)
                return
    if not meansomething :
        print("의미 옵션을 추가해주세요.")

    decode_newword(command)