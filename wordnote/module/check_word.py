from module.decode_word import *

global abc_rex, kor_rex
abc_rex = re.compile("[a-zA-Z` -]*")
kor_rex = re.compile("[ㄱ-ㅎ가-힣()ㅏ-ㅣ ]*")

def check_meaningoption(splited):
    
    meaning_list = []
    meansomething = False
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
            if option_main in meaning_option :
                if kor_rex.match(now_detail.strip()).group() != now_detail.strip() :
                    print("단어는 다음과 같은 정규표현식을 지켜야 합니다 : [ㄱ-ㅎ가-힣() ]*")
                    return False
                if now_detail.strip() in meaning_list :
                    print("한 영단어가 같은 의미를 두 개이상 갖을 수 없습니다.")
                    return False 
                meaning_list = meaning_list + [now_detail.strip()]
            else :
                reserved = option_list + ["MEANING","NULL"]
                if now_detail.strip() in reserved :
                    print("태그에 예약어를 사용할 수 없습니다 : "+now_detail.strip())
                    return False

    if not meansomething :
        print("의미 옵션을 추가해주세요.")
        return False  
    return True

def check_newword(command):
    splited = command.split(" -")
    if abc_rex.match(splited[0]).group() != splited[0] or splited[0] == "" :
        print("영단어는 다음과 같은 정규표현식을 지켜야 합니다 : [a-zA-Z` -]*")
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
    if abc_rex.match(splited[0]).group() != splited[0] or splited[0] == "" :
        print("영단어는 다음과 같은 정규표현식을 지켜야 합니다 : [a-zA-Z` -]*")
        return
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

def check_viewword(setting):
    splited = setting.split(" -")
    star_mod = False
    if abc_rex.match(splited[0]) == None :
        print("영단어는 다음과 같은 정규표현식을 지켜야 합니다 : [a-zA-Z` -]*")
        return
    index_star = findAtStar(splited[0])
    if index_star == -1 :
        print("등록되지 않는 영단어입니다 : "+splited[0])
        print("해당 영단어를 등록하고 싶다면 newword 명령어를 사용하세요.")
        return
    else :
        mod_option = ['star']
        length = len(splited)
        for i in range(1,length) :
            if not splited[i].strip() in mod_option :
                print("알 수 없는 옵션입니다 : "+splited[i].strip())
                return
            if splited[i].strip() == 'star' :
                star_mod = True
        if getNNN() != "" :
            working_note = open("data/work/"+getNNN()+".working-on.txt","r",encoding="UTF-8")
            if working_note.read().find("WordAt"+str(index_star)) == -1 :
                working_note.close()
                print("현재 단어장("+getNNN()+")에서 찾을 수 없는 단어입니다 : "+splited[0].strip())
                return
            working_note.close()
        elif not star_mod :
            print("접속한 단어장이 없습니다.")
            return
        viewword(setting,star_mod)