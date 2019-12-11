from module.tool import *

def booting():
    if not os.path.isdir(data_dir) :
        os.makedirs(data_dir)
    if not os.path.isdir(note_dir) :
        os.makedirs(note_dir)
    if not os.path.isdir(star_dir) :
        os.makedirs(star_dir)
    if not os.path.isdir(work_dir) :
        os.makedirs(work_dir)

    if not os.path.isfile(star_dir+"/STAR.txt") :
        star = open("data/star/STAR.txt","w",encoding="UTF-8")
        star.close()
    if not os.path.isfile(star_dir+"/NOTELIST.txt") :
        notelist = open("data/star/NOTELIST.txt","w",encoding="UTF-8")
        notes = os.listdir(note_dir)
        for now_note in notes :
            if checkLast(now_note,".wordnote.txt") :
                notelist.write(now_note.split(".wordnote.txt")[0]+"\n")
        notelist.close()