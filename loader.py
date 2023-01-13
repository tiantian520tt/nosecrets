logo1 = """                                                                                             
         ,--.                                                                                
       ,--.'|           .--.--.                                           ___                
   ,--,:  : |          /  /    '.                                       ,--.'|_              
,`--.'`|  ' :   ,---. |  :  /`. /                      __  ,-.          |  | :,'             
|   :  :  | |  '   ,'\;  |  |--`                     ,' ,'/ /|          :  : ' :  .--.--.    
:   |   \ | : /   /   |  :  ;_       ,---.     ,---. '  | |' | ,---.  .;__,'  /  /  /    '   
|   : '  '; |.   ; ,. :\  \    `.   /     \   /     \|  |   ,'/     \ |  |   |  |  :  /`./   
'   ' ;.    ;'   | |: : `----.   \ /    /  | /    / ''  :  / /    /  |:__,'| :  |  :  ;_     
|   | | \   |'   | .; : __ \  \  |.    ' / |.    ' / |  | ' .    ' / |  '  : |__ \  \    `.  
'   : |  ; .'|   :    |/  /`--'  /'   ;   /|'   ; :__;  : | '   ;   /|  |  | '.'| `----.   \ 
|   | '`--'   \   \  /'--'.     / '   |  / |'   | '.'|  , ; '   |  / |  ;  :    ;/  /`--'  / 
'   : |        `----'   `--'---'  |   :    ||   :    :---'  |   :    |  |  ,   /'--'.     /  
;   |.'                            \   \  /  \   \  /        \   \  /    ---`-'   `--'---'   
'---'                               `----'    `----'          `----'                         """
logo2 = """ _   _       _____                    _       
| \ | |     /  ___|                  | |      
|  \| | ___ \ `--.  ___  ___ _ __ ___| |_ ___ 
| . ` |/ _ \ `--. \/ _ \/ __| '__/ _ \ __/ __|
| |\  | (_) /\__/ /  __/ (__| | |  __/ |_\__ \\
\_| \_/\___/\____/ \___|\___|_|  \___|\__|___/                                     """
logo3 = """               .-'''-.                                 _..._                                                     
              '   _    \                            .-'_..._''.                                                  
   _..._    /   /` '.   \         __.....__       .' .'      '.\              __.....__                          
 .'     '. .   |     \  '     .-''         '.    / .'                     .-''         '.                        
.   .-.   .|   '      |  '   /     .-''"'-.  `. . '             .-,.--.  /     .-''"'-.  `.      .|              
|  '   '  |\    \     / /   /     /________\   \| |             |  .-. |/     /________\   \   .' |_             
|  |   |  | `.   ` ..' / _  |                  || |             | |  | ||                  | .'     |       _    
|  |   |  |    '-...-'`.' | \    .-------------'. '             | |  | |\    .-------------''--.  .-'     .' |   
|  |   |  |           .   | /\    '-.____...---. \ '.          .| |  '-  \    '-.____...---.   |  |      .   | / 
|  |   |  |         .'.'| |// `.             .'   '. `._____.-'/| |       `.             .'    |  |    .'.'| |// 
|  |   |  |       .'.'.-'  /    `''-...... -'       `-.______ / | |         `''-...... -'      |  '.'.'.'.-'  /  
|  |   |  |       .'   \_.'                                  `  |_|                            |   / .'   \_.'   
'--'   '--'                                                                                    `'-'              """
logo4 = """
      ___           ___           ___           ___           ___           ___           ___                         ___     
     /  /\         /  /\         /  /\         /  /\         /  /\         /  /\         /  /\          ___          /  /\    
    /  /::|       /  /::\       /  /::\       /  /::\       /  /::\       /  /::\       /  /::\        /__/\        /  /::\   
   /  /:|:|      /  /:/\:\     /__/:/\:\     /  /:/\:\     /  /:/\:\     /  /:/\:\     /  /:/\:\       \  \:\      /__/:/\:\  
  /  /:/|:|__   /  /:/  \:\   _\_ \:\ \:\   /  /::\ \:\   /  /:/  \:\   /  /::\ \:\   /  /::\ \:\       \__\:\    _\_ \:\ \:\ 
 /__/:/ |:| /\ /__/:/ \__\:\ /__/\ \:\ \:\ /__/:/\:\ \:\ /__/:/ \  \:\ /__/:/\:\_\:\ /__/:/\:\ \:\      /  /::\  /__/\ \:\ \:\\
 \__\/  |:|/:/ \  \:\ /  /:/ \  \:\ \:\_\/ \  \:\ \:\_\/ \  \:\  \__\/ \__\/~|::\/:/ \  \:\ \:\_\/     /  /:/\:\ \  \:\ \:\_\/
     |  |:/:/   \  \:\  /:/   \  \:\_\:\    \  \:\ \:\    \  \:\          |  |:|::/   \  \:\ \:\      /  /:/__\/  \  \:\_\:\  
     |__|::/     \  \:\/:/     \  \:\/:/     \  \:\_\/     \  \:\         |  |:|\/     \  \:\_\/     /__/:/        \  \:\/:/  
     /__/:/       \  \::/       \  \::/       \  \:\        \  \:\        |__|:|~       \  \:\       \__\/          \  \::/   
     \__\/         \__\/         \__\/         \__\/         \__\/         \__\|         \__\/                       \__\/    """
printColor(random.choice([logo1,logo2,logo3,logo4]),random.choice(['GREEN','RED','YELLOW','BLUE','WHITE']),'')
print()
text = "NoSecrets Beta"
for ch in text:
    printColor(ch,random.choice(['GREEN','RED','YELLOW','BLUE','WHITE']),'')
print()