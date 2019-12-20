from module.decode_word import *

global abc_rex, kor_rex
abc_rex = re.compile("[a-zA-Z` -]*")
kor_rex = re.compile("[ㄱ-ㅎ가-힣()ㅏ-ㅣ 0-9]*")

def check_meaningoption(splited):
    meaning_list = []
    meansomething = False
    meaning_option = ["n","v","a","ad","prep","conj","pron","int"]
    tag_option = []
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
                if kor_rex.match(now_detail.strip()).group() != now_detail.strip() or now_detail.strip() == "" :
                    print("단어는 다음과 같은 정규표현식을 지켜야 합니다 : [ㄱ-ㅎ가-힣()ㅏ-ㅣ 0-9]*")
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
    if word in ["n","v","a","ad","prep","conj","pron","int","tag","MEANING","NULL",";"] :
        print("예약어를 영단어로 등록할 수 없습니다.")
        return False
    if word.strip() != word :
        print("영단어의 양 끝에 공백이 있습니다.")
        return False
    return True

def check_overlay(star_index,word,exception):
    meaning_and_tag = getStarLine(star_index).split("MEANING;")[1:]
    if exception > -1 :
        meaning_and_tag.remove(meaning_and_tag[exception])
    meanings = []
    for now in meaning_and_tag :
        meanings = meanings + now.split(";tag")[0].split(";")[1:]
    return word in meanings 

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

    star_index = findAtStar(splited[0])
    if check_meaningoption(splited) :
        splited.remove(splited[0])
        for now in splited :
            k = doublesplit(normalSplit(now," ")[1],",",";")
            for now2 in k :
                if check_overlay(star_index,now2,-1) :
                    print("기존 단어의 뜻과 중복되는 뜻이 있습니다 : "+now2.strip())
                    return
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
            if working_note.read().find("WordAt"+str(index_star)) == -1 and not star_mod :
                working_note.close()
                print("현재 단어장("+getNNN()+")에서 찾을 수 없는 단어입니다 : "+splited[0].strip())
                return
            working_note.close()
        elif not star_mod :
            print("접속중인 단어장이 없습니다.")
            return
        decode_viewword(setting)

def check_canpull(str_list,max_meaning,star_index,word):
    for now_detail in str_list :
        if not now_detail.strip().isdecimal() :
            print("opt 옵션은 정수를 인수로 갖어야 합니다 : "+now_detail.strip())
            return False
        if int(now_detail.strip()) >= max_meaning :
            print("영단어 "+word+"의 최대 뜻 번호는 "+str(max_meaning-1)+" 입니다.")
            return False
        if getStarLine(star_index).split("MEANING;")[int(now_detail.strip())+1] == "NULL" :
            print("영단어 "+word+"의 "+now_detail.strip()+"번째 뜻은 null 값으로 지정할 수 없습니다.")
            return False
    return True

def check_pullword(setting): 
    splited = setting.split(" -")
    
    mod = 0
    if getNNN() == "":
        print("접속중인 단어장이 없습니다.")
        return
    if not check_word(splited[0]) :
        return
    star_index = findAtStar(splited[0])
    if star_index == -1 :
        print("등록되지 않는 영단어입니다 : "+splited[0])
        print("해당 영단어를 등록하고 싶다면 newword 명령어를 사용하세요.")
        return
    
    mod_option = ["all","opt"]
    length = len(splited)
    max_meaning = len(getStarLine(star_index).split("MEANING;"))-1
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
            if not check_canpull(detail_list,max_meaning,star_index,splited[0]) :
                return
            mod = 2
    
    if mod == 0 :
        viewword(splited[0],[True])
        sub_command = input("STAR에서 가져오고자 하는 단어의 뜻 번호를 입력해주세요 : ")
        detail_list = sub_command.split(",")
        if not check_canpull(detail_list,max_meaning,star_index,splited[0]) :
            return
        setting = setting + " -opt " + sub_command
    elif mod == 1 :
        sub_command = ""
        meaninglist = getStarLine(star_index).split("MEANING;")
        length2 = len(meaninglist)
        for i in range(1,length2) :
            if meaninglist[i] != "NULL" :
                sub_command = sub_command + str(i-1) + ", "
        setting = splited[0] + " -opt " + sub_command

    decode_pullword(setting)

def check_canerase(str_list, james):
    for now_detail in str_list :
        if not now_detail.strip().isdecimal() :
            print("opt 옵션은 정수를 인수로 갖어야 합니다 : "+now_detail.strip())
            return False
        if not now_detail.strip() in james :
            print("접속중인 단어장에 참조되지 않은 단어의 뜻은 지울 수 없습니다.")
            return False
    return True

def check_eraseword(setting):
    splited = setting.split(" -")
    
    mod = 0
    if getNNN() == "":
        print("접속중인 단어장이 없습니다.")
        return
    if not check_word(splited[0]) :
        return
    star_index = findAtStar(splited[0])
    if star_index == -1 :
        print("등록되지 않는 영단어입니다 : "+splited[0])
        print("해당 영단어를 등록하고 싶다면 newword 명령어를 사용하세요.")
        return
    note_index = findAtNote(star_index)
    if note_index == -1 :
        print("접속중인 단어장에 없는 영단어입니다.")
        return
    james = normalSplit(getNoteLine(note_index),";WordAt")[1].split(";")[1:]

    mod_option = ["all","opt"]
    length = len(splited)
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
            if not check_canerase(detail_list,james) :
                return
            mod = 2

    if mod == 0 :
        viewword(splited[0],[False])
        sub_command = input("지우고자 하는 단어의 뜻 번호를 입력해주세요 : ")
        detail_list = sub_command.split(",")
        if not check_canerase(detail_list,james) :
            return
        setting = setting + " -opt " + sub_command
    elif mod == 1 :
        sub_command = ""
        for now in james :
            sub_command = sub_command + now + ", "
        setting = splited[0] + " -opt " + sub_command
    
    decode_eraseword(setting)

def check_candelete(str_list,max_meaning,star_index,word):
    for now_detail in str_list :
        if not now_detail.strip().isdecimal() :
            print("opt 옵션은 정수를 인수로 갖어야 합니다 : "+now_detail.strip())
            return False
        if int(now_detail.strip()) >= max_meaning :
            print("영단어 "+word+"의 최대 뜻 번호는 "+str(max_meaning-1)+" 입니다.")
            return False
    return True

def check_deleteword(setting):
    splited = setting.split(" -")
    
    if getNNN() != "" :
        print("접속 중인 단어장이 있으면 사용할 수 없는 명령어입니다.")
        return
    if not check_word(splited[0]) :
        return
    star_index = findAtStar(splited[0])
    if star_index == -1 :
        print("STAR에 등록되지 않는 단어는 삭제할 수 없습니다.")
        return
    mod = 0

    mod_option = ["all","opt"]
    length = len(splited)
    max_meaning = len(getStarLine(star_index).split("MEANING;"))-1
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
            if not check_candelete(detail_list,max_meaning,star_index,splited[0]) :
                return
            mod = 2
    
    if mod == 0 :
        viewword(splited[0],[True])
        sub_command = input("STAR에서 지우고자 하는 단어의 뜻 번호를 입력해주세요 : ")
        detail_list = sub_command.split(",")
        if not check_candelete(detail_list,max_meaning,star_index,splited[0]) :
            return
        setting = setting + " -opt " + sub_command
    elif mod == 1 :
        sub_command = ""
        meaninglist = getStarLine(star_index).split("MEANING;")
        length2 = len(meaninglist)
        for i in range(1,length2) :
            if meaninglist[i] != "NULL" :
                sub_command = sub_command + str(i-1) + ", "
        setting = splited[0] + " -opt " + sub_command

    notelist = getNoteList()
    
    options = setting.split("-opt")[1].split(",")
    log = []
    for now in options :
        if not now.strip() in log and now.strip() != "":
            log = log + [int(now.strip())]
    log.sort()
    affected = {}
    for now in notelist :
        havings = isNoteHaving(now,star_index)
        for now_log in log :
            if str(now_log) in havings :
                if not now in affected.keys() :
                    affected[now] = [str(now_log)]
                else :
                    affected[now] = affected[now] + [str(now_log)]

    if mod != 0 :
        viewword(splited[0],[True])

    affected_note = list(affected.keys())
    if affected_note != [] :
        print("다음 단어장들이 참조하고 있는 단어의 뜻도 함께 삭제됩니다 :")
    for now in affected_note :
        print(" "+now+" : "+glue(affected[now],", "))

    if not get_yes_or_no("정말 삭제하시겠습니까?") :
        return

    deleteword(star_index,log,affected)

def check_modifyword(setting):
    splited = setting.split(" -")
    
    if getNNN() != "" :
        print("접속 중인 단어장이 있으면 사용할 수 없는 명령어입니다.")
        return
    if not check_word(splited[0]) :
        return
    star_index = findAtStar(splited[0])
    if star_index == -1 :
        print("STAR에 등록되지 않는 단어는 수정할 수 없습니다.")
        return
    mod = 0

    mod_option = ["opt"]
    length = len(splited)
    max_meaning = len(getStarLine(star_index).split("MEANING;"))-1
    for i in range(1,length) :
        now = splited[i].split(" ")[0].strip()
        if not now in mod_option :
            print("알 수 없는 옵션입니다 : "+splited[i].split(" ")[0].strip())
            return
        if mod != 0 :
            print("이 명령어에서 모드 옵션은 동시에 하나만 적용할 수 있습니다.")
            return
        if now == "opt" :
            if len(splited[i].split(" ")) == 1:
                    print("opt 옵션은 하나의 정수만을 인수로 갖어야 합니다.")
                    return
            detail_list = normalSplit(splited[i]," ")[1].split(",")
            if not len(detail_list) == 1 :
                print("opt 옵션은 하나의 정수만을 인수로 갖어야 합니다.")
                return
            if not check_candelete(detail_list,max_meaning,star_index,splited[0]) :
                return
            mod = 2
    
    if mod == 0 :
        viewword(splited[0],[True])
        sub_command = input("STAR에서 수정하고자 하는 단어의 뜻 번호 하나를 입력해주세요 : ")
        detail_list = sub_command.split(",")
        if not len(detail_list) == 1 :
            print("opt 옵션은 하나의 정수만을 인수로 갖어야 합니다.")
            return
        if not check_candelete(detail_list,max_meaning,star_index,splited[0]) :
            return
        setting = setting + " -opt " + sub_command

    modi_index = int(setting.split("-opt")[1].strip())

    now_line = getStarLine(star_index).split("MEANING;")[1:][modi_index]
    now_class = now_line.split(";")[0]
    now_meaning = normalSplit(now_line,";")[1]
    good_len = 149-len(now_class)-2

    print(start_view)
    view_format("",[splited[0]+" (STAR : "+str(star_index)+")"])
    print(middle_view)
    view_list = makeview("MEANING;"+now_line)
    class_list = ["n", "v", "a", "ad", "prep", "conj", "pron", "int"]
    for i in range(8) :
        splited = view_list[i].split(";")
        james = []
        for now in splited :
            james = james + kor_cut(now,149-len(class_list[i])-2)
        view_format(class_list[i]+". ",james)
    print(end_view)

    next_command = input("수정할 내용을 입력해주세요. ")
    overlay = -1
    if next_command == "":
        print("주어진 입력이 없습니다.")
        return
    if next_command[0] == "+" :
        next_command = next_command[1:]
        overlay = modi_index
    elif next_command[0] == "-" :
        next_command = next_command[1:]
        overlay = -2
    
    splited = next_command.split(",")
    log = []   
    if overlay != -2 :
        for now in splited :
            if not now.strip() in log :
                log.append(now.strip())
                if kor_rex.match(now.strip()).group() != now.strip() or now.strip() == "":
                    print("단어는 다음과 같은 정규표현식을 지켜야 합니다 : [ㄱ-ㅎ가-힣()ㅏ-ㅣ 0-9]*")
                    return
                if check_overlay(star_index,now.strip(),-1) :
                    print("기존 단어의 뜻과 중복되는 뜻이 있습니다 : "+now.strip())
                    return
            else :
                print("주어진 입력에 중복이 있습니다 : "+now.strip())
                return
    else :
        meaning_list = now_line.split(";tag")[0].split(";")
        for now in splited :
            if not now.strip() in log :
                log.append(now.strip())
                if kor_rex.match(now.strip()).group() != now.strip() or now.strip() == "":
                    print("단어는 다음과 같은 정규표현식을 지켜야 합니다 : [ㄱ-ㅎ가-힣()ㅏ-ㅣ 0-9]*")
                    return
                if not now.strip() in meaning_list :
                    print("기존 단어에 존재하지 않는 뜻이 있습니다 : "+now.strip())
                    return
            else :
                print("주어진 입력에 중복이 있습니다 : "+now.strip())
                return

    modifyword(next_command, star_index, modi_index,overlay)

def check_checkword(setting):
    if setting.find("-") != -1 :
        print("옵션을 넣을 수 없는 명령어입니다.")
        return
    if getNNN() != "" :
        print("접속 중인 단어장이 있으면 사용할 수 없는 명령어입니다.")
        return
    if not check_word(setting) :
        return
    if findAtStar(setting) == -1 :
        print("등록되지 않은 영단어입니다.")
        return
    checkword(setting)