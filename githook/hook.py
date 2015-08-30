import os,subprocess,re, warnings, time
def hookOnCommit():
    output_f = open('commit.txt', 'w')
    content=subprocess.Popen(["git", "log", "-1"], stdout=output_f,stderr=output_f)
    output_f.close()
    time.sleep(1)
    cmt_line=open('commit.txt').readlines()[0].strip()
    hash_value=str(cmt_line.split(' ')[1])
    time.sleep(1)
    output_f = open('content.txt', 'w')
    content=subprocess.Popen(['git', 'show', hash_value], stdout=output_f,stderr=output_f)
    output_f.close()
    time.sleep(1)
    cnt =[]
    with open('content.txt') as f:
        lines = f.readlines()
        for line in lines:
                line=line.rstrip('\n')
                cnt.append(line)
        data = ''.join(cnt)
    #res=subprocess.Popen(["grep", "-w", "def", data])
    #if res:
     #   result=subprocess.Popen(["grep", "-w", "security declared", data])
        #if result:
         #   exit()
        #else:
            #exit()
         #   warnings.warn("<<<<<<<<<<<<<< missing security declaration >>>>>>>>>>>>>>>")
    #else:
     #   exit() 
        if re.match("(.*)def(.*)", data):
            if "security.declareProtected" not in data:
                warnings.warn("<<<<<<<<<<<<<< missing security declaration >>>>>>>>>>>>>>>")
            else:
                exit()
        else:
            exit()


hookOnCommit()