from modules import *
from commands import *
commands.update(loaded_modules)
def commands_help():
    for name in commands.keys():
        print('--> '+name)
        try:
            printGreen('----> Auther: '+module_helps[name][0])
            printGreen('----> Date: '+module_helps[name][1])
            try:
                printGreen('----> EN - Description: '+module_helps[name][2])
            except:
                pass
            try:
                printGreen('----> CN - Description: '+module_helps[name][3])
            except:
                pass
        except Exception as e:
            printGreen('----> NoSecrets Command')
            
        
while True:
    prompt = "NoSecrets> "
    for ch in prompt:
        printColor(ch,random.choice(['GREEN','RED','YELLOW','BLUE','WHITE']),'')
    cmds = input().split()
    # -- 0索引为命令名 后续索引为参数--#
    cmd = commands[cmds[0]]+'('
    for i in range(1,len(cmds)):
        cmd += '"' + cmds[i] + '"'
        if i != len(cmds)-1:
            cmd += ','
    cmd += ')'
    try:
        exec(cmd)
    except TypeError:
        exec(cmds[0]+'_help()')
    except Exception as e:
        printRed(str(e))
        printRed('[-] Bad command.')
        printRed('[-] 错误的命令。')
    #except:
    #    printRed('[-] Bad command.')
