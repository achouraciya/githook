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

###############################################################################

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
    lines=open('content.txt').readlines()
    #res=subprocess.Popen(["grep", "-EHi", "Anonymous|Authenticated", '/kgeetanjali/new_jiva6/src/jiva.prvportal/Products/ZeProviderPortal/permissions.py'])
    for line in lines:
        line=line.rstrip('\n')
        cnt.append(line)
    data = ''.join(cnt)
    if re.match("(.*)def(.*)", data):
         if "security.declareProtected" in data:
             data=data.split('+')
             for each in data:
                 if "security.declareProtected" in each:
                     perm_word = each
             time.sleep(1)
             if perm_word:
                 perm_word=perm_word.strip()
                 perm_word=perm_word.split('(')[1].split(',')[0]
                 print "The roles aded for the method", perm_word, "are :"
                 res=subprocess.Popen(["grep", "-EHi", perm_word, '/kgeetanjali/new_jiva6/src/jiva.prvportal/Products/ZeProviderPortal/permissions.py'])
         else:
             warnings.warn("<<<<<<<<<<<<<< missing security declaration >>>>>>>>>>>>>>>")
    else:
        exit()


hookOnCommit()



###############################################
import os,subprocess,re, warnings, time
def hookOnCommit():
    output_f = open('commit.txt', 'w')
    commit=subprocess.Popen(["git", "rev-parse", "HEAD"], stdout=output_f,stderr=output_f)
    output_f.close()
    time.sleep(1)
    hash_value=open('commit.txt').readlines()[0].strip()
    time.sleep(1)
    output_f = open('content.txt', 'w')
    content=subprocess.Popen(['git', 'show', hash_value], stdout=output_f,stderr=output_f)
    output_f.close()
    time.sleep(1)
    content_of_cmt =[]
    commit_content=open('content.txt').readlines()
    #res=subprocess.Popen(["grep", "-EHi", "Anonymous|Authenticated", '/kgeetanjali/new_jiva6/src/jiva.prvportal/Products/ZeProviderPortal/permissions.py'])
    for line in commit_content:
        line=line.rstrip('\n')
        content_of_cmt.append(line)
    data = ''.join(content_of_cmt)
    if re.match("(.*)def(.*)", data):
        if re.match("(.*)def(.*)(.__)", data):
            print "no need of permission"
        elif "security.declareProtected" in data:
            data=data.split('+')
            for each in data:
                if "security.declareProtected" in each:
                    permission = each
            time.sleep(1)
            if permission:
                permission=permission.strip().split('(')[1].split(',')[0]
                path = raw_input("please enter a path of permmison file for repository ")
                print "The roles aded for the method", permission, "are :"
                res=subprocess.Popen(["grep", "-EHi", permission, path])
        else:
            warnings.warn("<<<<<<<<<<<<<< missing security declaration >>>>>>>>>>>>>>>")
    else:
        exit()


hookOnCommit()


