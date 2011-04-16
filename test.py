import time, os
r = open('C:/users/Domas/Music/iTunes/backup/d.xml', 'r')
#potential temp file
w = open('C:/users/Domas/Music/iTunes/backup/that.xml', 'w')

info = []

def parseloc (inloc):
    

def parsedate (indate):
    indate = indate.lstrip()
    

def dump(info):
    count = 0
    for i in info:
        if i.lstrip()[0:13] == '<key>Location':
            i = parseloc(i)
        elif:
            i++
    for i in info:
        if i.lstrip()[0:15] == '<key>Date Added':
            i = parsedate(i)
            
    for i in info:
        w.write(i)



for line in r:
    info.append(line)
    if info[-1].lstrip() == </dict>:
        dump(info)
    



r.close()
w.close()

print 
