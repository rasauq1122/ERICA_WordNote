from module.decode_word import *

def check_addword(command):
    splited = command.split(" -")
    if splited[0] == "" :
        print("영단어가 감지되지 않았습니다.")
        return
    splited.remove(splited[0])
    length = len(splited)
    if length == 0:
        print("태그가 아닌 하나의 옵션은 포함되어야 합니다.")
        return
    alltag = True
    meansomething = False
    for i in range(length) :
        if not splited[i].split(" ")[0] in {"n","v","a","ad","prep","conj","pron","int","tag"} :
            print("다음은 올바르지 않은 옵션입니다 : "+splited[i].split(" ")[0])
            return
        elif not splited[i].split(" ")[0] in {"tag"} :
            alltag = False
            if len(normalSplit(splited[i]," ")) == 2 and len(superSplit(normalSplit(splited[i]," ")[1])) != 0 :
                meansomething = True
    if alltag :
        print("태그만 입력하실 수 없습니다.")
        return
    if not meansomething :
        print("단어는 최소 하나의 의미를 가져야 합니다.")
        return
    decode_addword(command)