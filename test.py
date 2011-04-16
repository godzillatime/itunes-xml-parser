import time, os
r = open('C:/users/Domas/Music/iTunes/backup/d.xml', 'r')
#potential temp file
w = open('C:/users/Domas/Music/iTunes/backup/that.xml', 'w')

info = []

def parseloc (inloc):
    '''
    Receive: Location string from iTunes XML file
    Return:  Location string formatted for the filesystem
    '''
    pass
    
def getNewDate(filePath):
    '''
    Receive: Song file location, parsed for special characters
    Return:  Date created as string formatted for iTunes XML file
        Format: yyyy-mm-ddThh:mm:ssZ
    '''
    t = os.path.getctime(filePath) # Float representing seconds since epoch
    newDate = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t)) 

    return newDate

def parsedate (indate):
    '''
    Receive: Date created from iTunes XML file
    Return:  ???
    '''
    indate = indate.lstrip()

def dump(info):
    '''
    Receive: List of information from the iTunes XML file
    '''
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
