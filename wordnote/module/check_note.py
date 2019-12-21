from module.execute_note import *

abc_rex = re.compile("[a-zA-Z` -]*")
kor_rex = re.compile("[ㄱ-ㅎ가-힣()ㅏ-ㅣ 0-9]*")
note_rex = re.compile("[a-zA-Z ㄱ-ㅎ가-힣()ㅏ-ㅣ0-9_.-]*")

def check_notename(note_name):
    if note_name.strip() != note_name :
        print("단어장의 이름 양 끝에 공백이 있습니다.")
        return False
    if note_rex.match(note_name).group() != note_name or note_name == "" :
        print("단어장은 다음과 같은 정규표현식을 지켜야 합니다 : [a-zA-Z ㄱ-ㅎ가-힣()ㅏ-ㅣ0-9_.-]*")
        return False
    if len(note_name) > 100 :
        print("최대 100자까지만 사용할 수 있습니다.")
        return False
    return True

def check_addnote(note_name):
    if note_name == "" :
        print("단어장의 이름은 최소 한 글자 이상이어야 합니다.")
        return
    if not check_notename(note_name) :
        return
    notelist = open("data/star/NOTELIST.txt","r",encoding="UTF-8")
    notelist_reading = notelist.read()
    notelist.close()
    if notelist_reading.find(note_name+"\n") != -1 :
        okay = get_yes_or_no("이미 같은 이름의 단어장이 존재합니다. 지우고 새로 만들까요?")
        if okay :
            addnote(note_name)
        else :
            print("단어장을 새로 만들지 못했습니다.")
            return
    else :
        addnote(note_name)

def check_removenote(note_name):
    notelist = open("data/star/NOTELIST.txt","r",encoding="UTF-8")
    notelist_reading = notelist.read()
    notelist.close()
    if getNNN() != "":
        print("접속 중인 단어장이 있으면 사용할 수 없는 명령어입니다.")
        return
    if notelist_reading.find(note_name+"\n") != -1 and os.path.isfile(note_dir+"/"+note_name+".wordnote.txt") :
        if get_yes_or_no("정말 단어장을 삭제할까요?") :
            removenote(note_name)
        else :
            print("단어장을 삭제하지 않았습니다.")
    else :
        print("존재하지 않는 단어장을 삭제할 수 없습니다.")

def check_noteform(note_name,note_line):
    return True 

def check_connectnote(note_name):
    if getNNN() == "" :
        if os.path.isfile(note_dir+"/"+note_name+".wordnote.txt") :
            now_note = open("data/note/"+note_name+".wordnote.txt","r",encoding="UTF-8")
            note_line = now_note.readlines()
            now_note.close()
            if check_noteform(note_name,note_line) :
                connectnote(note_name)
            else :
                print("단어장의 형식이 올바르지 않아 접근할 수 없습니다.")
        else :
            print("존재하지 않는 단어장에 접근할 수 없습니다.")
    else :
        print("이미 접근 중인 단어장이 존재합니다. 단어장 이름 : "+getNNN())

def check_disconnectnote(string):
    if string != "":
        print("해당 명령어는 어떤 옵션도 넣을 수 없습니다.")
        return
    if getNNN() != "" :
        disconnectnote()
    else :
        print("접근한 단어장이 없습니다.")

def check_end(setting):
    if setting == "" :
        check_disconnectnote("")
        end()
    else :
        print("해당 명령어는 어떤 옵션도 넣을 수 없습니다.")
        return

def check_mergenote(setting): # asd, asdd, addd -name merged
    splited = setting.split(" -")
    mergelist = splited[0].split(",")
    log = []
    notelist = getNoteList()
    if getNNN() != "" :
        print("접속 중인 단어장이 있으면 사용할 수 없는 명령어입니다.")
        return
    for now in mergelist :
        if not now.strip() in notelist :
            print("알 수 없는 단어장입니다 : "+now.strip())
            return
        if not now.strip() in log :
            log.append(now.strip())
    
    if len(log) <= 1 :
        print("합병하고자 하는 단어장의 갯수가 최소 2개 이상이어야 합니다.")
        return

    mod = 0

    mod_option = ["name"]
    length = len(splited)
    for i in range(1,length) :
        now = splited[i].split(" ")[0].strip()
        if not now in mod_option :
            print("알 수 없는 옵션입니다 : "+splited[i].split(" ")[0].strip())
            return
        if mod != 0 :
            print("이 명령어에서 모드 옵션은 동시에 하나만 적용할 수 있습니다.")
            return
        if now == "name" :
            k = splited[i].split(" ")
            if len(k) != 2:
                print("name 옵션은 하나의 문자열을 인수로 받습니다.")
                return
            if not check_notename(k[1]) :
                return
            mod = k[1]
    
    if mod == 0 :
        sub_command = input("합병된 단어장의 새 이름을 입력해주세요. ")
        make_log(sub_command)
        if not check_notename(sub_command) :
            return
        mod = sub_command

    mergenote(log,mod)

def check_notelist(setting):
    if setting != "":
        print("해당 명령어는 어떤 옵션도 넣을 수 없습니다.")
        return
    notelist()

def check_viewnote(setting):
    if getNNN() == "":
        print("접근한 단어장이 없습니다.")
        return
    if setting != "-print" and setting != "" :
        print("해당 명령어는 -print 만을 옵션으로 넣을 수 있습니다.")
        return
    
    mod = False
    if setting == "-print":    
        mod = True
    
    viewnote(mod)

def check_breaker(setting):
    if setting != "":
        print("해당 명령어는 어떤 옵션도 넣을 수 없습니다.")
        return
    if getNNN() != "" :
        print("접근한 단어장에서 강제로 벗어납니다. 단어장 이름 : "+getNNN())
        breaker()
    else :
        print("접근한 단어장이 없습니다.")