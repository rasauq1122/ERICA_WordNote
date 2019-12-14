from module.module import *

booting()

commands = {"addnote":check_addnote,"removenote":check_removenote,"connectnote":check_connectnote,
            "disconnectnote":check_disconnectnote,"newword":check_newword,"appendword":check_appendword,"viewword":check_viewword,
            "pullword":check_pullword,

            "an":check_addnote,"rn":check_removenote,"cn":check_connectnote,"dn":check_disconnectnote,
            "nw":check_newword,"aw":check_appendword,"vw":check_viewword,"pw":check_pullword,

            "end":check_end}

while True :
    command = input("> ")
    splited = normalSplit(command," ")
    if splited[0] in commands.keys() :
        if len(splited) == 1 :
            commands[splited[0]]("")
        else :
            commands[splited[0]](splited[1].strip())
    else :
        print("알 수 없는 명령어입니다.")