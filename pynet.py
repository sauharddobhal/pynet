#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os, re, time, sys
from subprocess import check_output
from sys import platform as _platform
from termcolor import colored
if _platform == 'win32':
    import colorama
    colorama.init()

def yellow(text):
    return colored(text, 'yellow', attrs=['bold'])

def green(text):
    return colored(text, 'green', attrs=['bold'])

def red(text):
    return colored(text, 'red', attrs=['bold'])

def white(text):
    return colored(text, 'white', attrs=['bold'])


infrm = '''
                                                                                     _   
                                                                                    | |  
                                                              _ __  _   _ _ __   ___| |_ 
                                                             | '_ \| | | | '_ \ / _ \ __|
                                                             | |_) | |_| | | | |  __/ |_ 
                                                             | .__/ \__, |_| |_|\___|\__|
                                                             | |     __/ |               
                                                             |_|    |___/ by srootx              

***************************************************************************************************************************************************************
Port      RemoteIP            PID       Executable Name                    User                              Title
***************************************************************************************************************************************************************'''
	

def id_netstat_processes():
    result = check_output("netstat -aon", shell=True)
 
    clean_up_array = [
        ("Active Connections", ""),
        ("Proto", ""),
        ("Local Address", ""),
        ("Foreign Address", ""),
        ("State", ""),
        ("PID", ""),
        ("\r", ""),
        ("\t", " ")
    ]
 
    
    for find, replace in clean_up_array:
        result = result.replace(find, replace)
 
    
    reexstring = " *(UDP|TCP) *([0-9]*\\.[0-9]*\\.[0-9]*\\.[0-9]*|\\[ *[a-z0-9]*:* *[a-z0-9]*:* *[a-z0-9]*:* *[a-z0-9]*:* *[a-z0-9%]*\\]):([0-9]*) *([0-9]*\\.[0-9]*\\.[0-9]*\\.[0-9]*|\\[:*\\]|\\*):(\\*|[0-9]*) *(LISTENING|ESTABLISHED|TIME_WAIT|CLOSE_WAIT)* *([0-9]*)"
 
    regexcompiled = re.compile(reexstring)
 
    items = regexcompiled.finditer(result)
 
    networkitems = []
 
    for match in items:
       
        networktype = match.group(1).strip()
        localip = match.group(2).strip()
        localport = match.group(3).strip()
        remoteip = match.group(4).strip()
        remoteport = match.group(5).strip()
 
        if not match.group(6) is None:
            status = match.group(6).strip()
        else:
            status = ""
        pid = match.group(7).strip()
        networkitems.append(( localip, localport, remoteip, remoteport, status, pid))
 
    tasklist = check_output("tasklist /v", shell=True)
 
    
    clean_up_array = [
        ("Image Name", "" ),
        ("PID", "" ),
        ("Session Name", "" ),
        ("Session#", "" ),
        ("Mem Usage", "" ),
        ("Status", "" ),
        ("User Name", "" ),
        ("CPU Time", "" ),
        ("Window Title", "" ),
        ("=",""),
        ("\r", ""),
        ("\t", " ")
    ]
 
    
    for find, replace in clean_up_array:
        tasklist = tasklist.replace(find, replace)
 
    regexstring2 = "^(.*?)   *([0-9]*) *(.*?)  *([0-9]*) *([0-9,]* .) *(.*?)  *(.*?)   *([0-9:]*) *(.*?)  "
 
    tasks = {}
 
    regexcompiled2 = re.compile(regexstring2, re.MULTILINE)
 
    items = regexcompiled2.finditer(tasklist)
 
    for match in items:
       
        imagename = match.group(1).strip()
        pid = match.group(2).strip()
 
        if pid == '':
            continue
 
        sessionname = match.group(3).strip()
        sessionnumber = match.group(4).strip()
        memory = match.group(5).strip()
        status = match.group(6).strip()
        user = match.group(7).strip()
        cputime = match.group(8).strip()
        title = match.group(9).strip()
 
       
        tasks[pid] = (imagename,sessionname,sessionnumber,memory,status,user,cputime,title)

    output = ""
   
    for item in networkitems:
       
        localip, localport, remoteip, remoteport, status, pid = item
 
        if pid in tasks.keys():
            
            imagename,sessionname,sessionnumber,memory,status,user,cputime,title = tasks[pid]
            output += localport.ljust(10) + remoteip.ljust(20) + pid.ljust(10) + imagename.ljust(35)  + user.ljust(35) + title + "\n"
        else:
            
            output += localport.ljust(10) + remoteip.ljust(20) + "PID "+ pid +" Missing" + "\n"

	os.system('mode 160')
	os.system('title pynet by srootx V1.0')
	print green(infrm)
	print white(output)

if __name__ == "__main__":
  
    id_netstat_processes()