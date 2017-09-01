import os, sys
from sys import platform as _platform
import shutil
try:
    from termcolor import colored
except ImportError:
    print '[!] Failed to Import termcolor'
    try:
        choice = raw_input('[*] Wana install termcolor? [y/n] ')
    except KeyboardInterrupt:
        print '\n[!] User Interrupted Choice'
        sys.exit(1)
    if choice.strip().lower()[0] == 'y':
        print '[*] Attempting to Install termcolor... ',
        sys.stdout.flush()
        try:
            import pip
            pip.main(['install', '-q', 'termcolor==1.1.0'])
            from termcolor import colored
            print '[DONE]'
        except Exception:
            print '[FAIL]'
            sys.exit(1)
    elif choice.strip().lower()[0] == 'n':
        print '[*] User Denied Auto-install'
        sys.exit(1)
    else:
        print '[!] Invalid Decision'
        sys.exit(1)
try:
    import colorama
except ImportError:
    print '[!] Failed to Import colorama'
    try:
        choice = raw_input('[*] Wana install colorama? [y/n] ')
    except KeyboardInterrupt:
        print '\n[!] User Interrupted Choice'
        sys.exit(1)
    if choice.strip().lower()[0] == 'y':
        print '[*] Attempting to Install colorama... ',
        sys.stdout.flush()
        try:
            import pip
            pip.main(['install', '-q', 'colorama==0.3.9'])
            import colorama
            print '[DONE]'
        except Exception:
            print '[FAIL]'
            sys.exit(1)
    elif choice.strip().lower()[0] == 'n':
        print '[*] User Denied Auto-install'
        sys.exit(1)
    else:
        print '[!] Invalid Decision'
        sys.exit(1)


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

loc = os.getcwd()
file = loc+'\pynet.bat'
contfile = loc+'\pynet.py'
cont = '''@echo off
python %s
pause'''%(contfile)
out = open(file, 'w')
out.write(cont)
out.close()
os.system('cls')
print green("\n\n\n[!] Script Generated pynet.bat file")
dest = os.environ['WINDIR']
full_file_name = file
try:
	shutil.copy(full_file_name, dest)
except IOError:
	print red("\nError:")+white(" Permission denied While moving pynet.bat to C:\Windows")
	print green("\n[!] Please copy pynet.bat file to C:\Windows")
	print green("\n[+] For test open CMD and enter pynet\n\n\n")