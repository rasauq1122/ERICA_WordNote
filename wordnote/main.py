from module.module import *

booting()
breaker()
log = open("data/log.txt","a",encoding="UTF-8")
log.write(str(datetime.datetime.now())+" : "+"boot\n")
log.close()

commands = {"addnote":check_addnote,"removenote":check_removenote,"connectnote":check_connectnote,
            "disconnectnote":check_disconnectnote,"mergenote":check_mergenote,"notelist":check_notelist,
            "viewnote":check_viewnote,
            "newword":check_newword,"appendword":check_appendword,"viewword":check_viewword,"pullword":check_pullword,
            "erasewword":check_eraseword,"deleteword":check_deleteword,"modifyword":check_modifyword,"checkword":check_checkword,

            "an":check_addnote,"rn":check_removenote,"cn":check_connectnote,"dn":check_disconnectnote,"mn":check_mergenote,
            "nl":check_notelist,"vn":check_viewnote,
            "nw":check_newword,"aw":check_appendword,"vw":check_viewword,"pw":check_pullword,"ew":check_eraseword,
            "dw":check_deleteword,"mw":check_modifyword,"cw":check_checkword,

            "exit":check_end,"break":check_breaker}

while True :
    command = input("> ")
    log = open("data/log.txt","a",encoding="UTF-8")
    log.write(str(datetime.datetime.now())+" : "+command+"\n")
    log.close()
    splited = normalSplit(command," ")
    if splited[0] in commands.keys() :
        if len(splited) == 1 :
            commands[splited[0]]("")
        else :
            commands[splited[0]](splited[1].strip())
    else :
        print("알 수 없는 명령어입니다.")