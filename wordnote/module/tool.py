import os

module_dir = os.getcwd()
main_dir = os.getcwd().split("/module")[0]
note_dir = main_dir+"/note"

now_note_name = ""
word_count = -1


def get_yes_or_no(notice):
    check = input(notice+" [y/n] ")
    while not check in ["y","yes","n","no"] :
        check = input("다음 중 하나를 입력해주세요. [y, yes, n, no] ")
        if check.strip().isalpha() :
            check = check.strip().lower()
        else :
            continue
    return check in ["y","yes"]

    
def normalSplit(given_string, clue):
    where = given_string.find(clue)
    if where == -1 :
        return [given_string]
    else :
        return [given_string[:where],given_string[where+len(clue):]]