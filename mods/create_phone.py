# \- NoSecrets Module \- #
Auther = "tiantian520"
Date = "2023/1/11 12:19"
CN_Description = "创建新的手机号列表，用来跑现绑"
EN_Description = "Create new phone number list, and use it to find a phone number of his QQ account."
# -/ NoSecrets Module -/ #

# \- Import Modules \- #
import os
import sys
# -/ Import Modules -/ #


# -- Create Phone Function -- #
def create_phone(start_number,end_number,filename):
	content = ""
	num_len = 11-len(start_number)-len(end_number)
	start_time = time.time()
	for num in range(0,pow(10,num_len)):
		if(len(str(num)) < num_len):
			tmp = '0'*(num_len-len(str(num))) + str(num)
		else:
			tmp = str(num)
		content += start_number + tmp + end_number + ',' + start_number + tmp + end_number + '\n'
	with open('./tmp/'+filename+'.csv','w+', encoding='utf-8') as f:
		f.write(content)
	use_time = time.time() - start_time
	return use_time
# -- 规定名称函数，必须为 "模块文件名_help" -- #    
def create_phone_help():
    printGreen(CN_Description)
    printGreen(EN_Description)
    printGreen('Usage: create_phone')
# -- 规定名称函数，必须为 "模块文件名_main" -- #
def create_phone_main():
    try:
        printGreen('[*] 欢迎!')
        printGreen('[!] ' + CN_Description)
        while True:
            printGreen('输入手机号前面的已知部分> ')
            start_number = input()
            if start_number == '':
                printRed('[-] 无效的输入！请重新输入。')
            elif start_number.isnumeric():
                break
            else:
                printRed('[-] 无效的输入！请重新输入。')
        while True:
            printGreen('输入手机号后面的已知部分> ')
            end_number = input()
            if end_number == '':
                printRed('[-] 无效的输入！请重新输入。')
            elif end_number.isnumeric():
                break
            else:
                printRed('[-] 无效的输入！请重新输入。')
        printGreen('[*] 获取成功。')
        printGreen('[*] 正在生成...')
        try:
            filename = str(int(time.time()))+str(random.randint(0,9))
            printGreen('[*] 纯文本生成完毕！耗时'+str(create_phone(start_number,end_number,filename))+'秒。数据被保存至 ./tmp/'+filename+'.csv 中。')
            content = """@echo off
del """+os.getcwd()+"""\\tmp\\temp.txt
setlocal EnableDelayedExpansion
set /a line=1
for /f "tokens=1,2,3,4 delims=," %%a in ("""+os.getcwd()+"\\tmp\\"+filename+""".csv) do (
if !line! gtr 1 (
(echo BEGIN:VCARD)       >> PATH\\temp.txt
(echo VERSION:3.0) >> PATH\\temp.txt
(echo N:;%%a;;;) >> PATH\\temp.txt
(echo FN:%%a) >> PATH\\temp.txt
(echo TEL;TYPE=CELL:%%b) >> PATH\\temp.txt
(echo ORG:%%c) >> PATH\\temp.txt
(echo TITLE:%%d) >> PATH\\temp.txt
(echo END:VCARD) >> PATH\\temp.txt
)
set /a line+=1
)
copy PATH\\temp.txt PATH\\output\\result_"""+filename+""".vcf
del PATH\\temp.txt"""
            with open('./tmp/process_'+filename+'.bat','w+') as processor:
                processor.write(content.replace('PATH',os.getcwd()))
            os.system(os.getcwd()+'/tmp/'+'process_'+filename+'.bat')
            if os.path.exists(os.getcwd()+'\\output\\result_'+filename+'.vcf'):
                printGreen('[*] VCF生成完毕！数据被保存至 '+os.getcwd()+'\\output\\result_'+filename+'.vcf 中。')
                return 1
            else:
                printRed('[-] 生成过程中遇到未知错误，VCF文件未能生成，但CSV文件已经生成完毕。若您需要VCF格式文件，请重新尝试。')
                return -1    
        except Exception as e:
            printRed('[-] 生成过程中遇到未知错误。请重新尝试')
            printRed('[-] '+str(e))
            return -1
    except KeyboardInterrupt:
        printRed('[-] 用户取消了操作。')
        return 0

    

