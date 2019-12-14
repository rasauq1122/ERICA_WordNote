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

def check_word(word):
    if abc_rex.match(word).group() != word or word == "" :
        print("영단어는 다음과 같은 정규표현식을 지켜야 합니다 : [a-zA-Z` -]*")
        return False
    if word in ["n","v","a","ad","prep","conj","pron","int","tag","MEANING","NULL"] :
        print("예약어를 영단어로 등록할 수 없습니다.")
        return False
    return True

def check_newword(command):
    splited = command.split(" -")
    if not check_word(splited[0]) :
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
    if not check_word(splited[0]) :
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
    if not check_word(splited[0]) :
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
            print("접속중인 단어장이 없습니다.")
            return
        decode_viewword(setting)

def check_pullword(setting): # STAR에 없는 뜻 번호에 대한 예외처리 필요 (0,2,3) 이런식으로 있을 때
    splited = setting.split(" -")
    
    mod = 0
    if not check_word(splited[0]) :
        return
    star_index = findAtStar(splited[0])
    if star_index == -1 :
        print("등록되지 않는 영단어입니다 : "+splited[0])
        print("해당 영단어를 등록하고 싶다면 newword 명령어를 사용하세요.")
        return
    if getNNN() == "":
        print("접속중인 단어장이 없습니다.")
        return
    
    mod_option = ["all","opt"]
    length = len(splited)
    max_meaning = len(getStarLine(star_index).split("MEANING;"))
    for i in range(1,length) :
        now = splited[i].split(" ")[0].strip()
        if not now in mod_option :
            print("알 수 없는 옵션입니다 : "+splited[i].split(" ")[0].strip())
            return
        if mod != 0 :
            print("이 명령어에서 모드 옵션은 동시에 하나만 적용할 수 있습니다.")
            return
        if now == "all" :
            if len(splited[i].split(" ")) > 1:
                print("all 옵션은 인수를 갖지 않습니다.")
                return
            mod = 1
        if now == "opt" :
            if len(splited[i].split(" ")) == 1:
                    print("opt 옵션은 정수를 인수로 갖어야 합니다.")
                    return
            detail_list = normalSplit(splited[i]," ")[1].split(",")
            for now_detail in detail_list :
                if not now_detail.strip().isdecimal() :
                    print("opt 옵션은 정수를 인수로 갖어야 합니다 : "+now_detail.strip())
                    return
                if int(now_detail.strip()) >= max_meaning :
                    print("영단어 "+splited[0]+"의 최대 뜻 번호는 "+str(max_meaning-1)+" 입니다.")
                    return
                if getStarLine(star_index).split("MEANING;")[int(now_detail.strip())+1] == "NULL" :
                    print("영단어 "+splited[0]+"의 "+now_detail.strip()+"번째 뜻은 null 값으로 지정할 수 없습니다.")
                    return
                mod = 2
    
    if mod == 0 :
        viewword(splited[0],[True])
        sub_command = input("STAR에서 가져오고자 하는 단어의 뜻을 입력해주세요 : ")
        detail_list = sub_command.split(",")
        for now_detail in detail_list :
            if not now_detail.strip().isdecimal() :
                print("opt 옵션은 정수를 인수로 갖어야 합니다 : "+now_detail.strip())
                return
            if int(now_detail.strip()) >= max_meaning :
                print("영단어 "+splited[0]+"의 최대 뜻 번호는 "+str(max_meaning-1)+" 입니다.")
                return
            if getStarLine(star_index).split("MEANING;")[int(now_detail.strip())+1] == "NULL" :
                print("영단어 "+splited[0]+"의 "+now_detail.strip()+"번째 뜻은 null 값으로 지정할 수 없습니다.")
                return
        mod = 2
        setting = setting + " -opt " + sub_command
    elif mod == 1 :
        sub_command = ""
        meaninglist = getStarLine(star_index).split("MEANING;")
        length2 = len(meaninglist)
        for i in range(1,length2) :
            if meaninglist[i] != "NULL" :
                sub_command = sub_command + str(i-1) + ", "
        setting = setting + " -opt " + sub_command

    decode_pullword(setting)