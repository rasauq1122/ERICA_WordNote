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
    if not os.path.isdir(view_dir) :
        os.makedirs(view_dir)
    if not os.path.isfile(data_dir+"/log.txt") :
        log = open("data/log.txt","w",encoding="UTF-8")
        log.close()
    if not os.path.isfile(star_dir+"/STAR.txt") :
        star = open("data/star/STAR.txt","w",encoding="UTF-8")
        star.close()
    if not os.path.isfile(star_dir+"/NOTELIST.txt") :
        notelist = open("data/star/NOTELIST.txt","w",encoding="UTF-8")
        notelist.close()