# \- NoSecrets Module \- #
Auther = "tiantian520"
Date = "2023/1/11 14:51"
CN_Description = "查看文件内容"
EN_Description = "Read a file and output."
# -/ NoSecrets Module -/ #

# -- 规定名称函数，必须为 "模块文件名_help" -- #
def cut_help():
    printGreen(CN_Description)
    printGreen(EN_Description)
    printGreen('Usage: cut [(MUST)FILENAME] [ENCODING]')
    printGreen('用法: cut [(必须)文件名] [编码方式]')
# -- 规定名称函数，必须为 "模块文件名_main" -- #
def cut_main(filename,encode='utf-8'):
    try:
        with open(filename,'r',encoding=encode) as f:
            print(f.read())
        return 1
    except KeyboardInterrupt:
        printRed('[-] 用户取消了操作。')
        printRed('[-] KeyboardInterrupt')
        return 0
    except UnicodeDecodeError:
        printRed('[-] 指定了错误的编码方式。')
        printRed('UnicodeDecodeError')
        printYellow('[!] 您可以尝试指定ENCODING来读取文件。例如：cut test.txt utf-8')
        printYellow('[!] You can try: cut test.txt utf-8')
        return -1
    except Exception as e:
        printRed('[-] 遇到错误')
        printRed(str(e))
        return -1

    

