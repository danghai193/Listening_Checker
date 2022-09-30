# Nhập thư viện
from gtts import gTTS
from playsound import playsound
from os import remove, path, getcwd, chdir
from random import randint
from linecache import getline

#Check để thay prompt lần đầu hoặc lần sau
firstTime = 0
PROMPT0 = 'Nhập 1 để nghe, 0 để thoát:   '
PROMPT1 = 'Nhập 1 để nghe từ khác, 2 để nghe lại, 3 để nghe lại (chậm hơn), 4 để nghe đánh vần, 5 để lấy đáp án, 0 để thoát:   '
PROMPT2 = '\n'+ 'ĐÃ PHÁT AUDIO!'.center(40, '-') + '\n' + 'Từ mà bạn nghe thấy là?    '
PROMPT3 = 'Bạn đã nhập dữ liệu không chính xác. Đang thoát...'
PROMPT4 = '\n'+ 'CHÍNH XÁC!'.center(40, '-')
PROMPT5 = '\n'+ 'CHƯA CHÍNH XÁC'.center(40, '-')

# Lấy vị trí file user
USER_FOLDER = path.expanduser('~') + '\wordfile.mp3'

chdir(path.expanduser('~'))
print(getcwd())

def wordCheck():
    userInput = input(PROMPT2)
    if userInput == chosenWord:
        print(PROMPT4)
        return True
    else: 
        print(PROMPT5)
        return False

while True:
    try:
        #Lấy dữ liệu từ người dùng
        if firstTime == 0:
            userChoice = int(input(PROMPT0))
            firstTime += 1
        else:
            userChoice = int(input(PROMPT1))
            
        if userChoice == 1:
            try: remove(f'{USER_FOLDER}')
            except: pass
            # Lấy ngẫu nhiên một dòng
            lineNumber = randint(1,370105)
            
            # Lấy dữ liệu của dòng vừa lấy ngẫu nhiên
            chosenWord = getline(r"C:\Users\dangv\words_alpha.txt", lineNumber).rstrip('\n').lower()
            
            # Lấy audio của từ
            tts_module = gTTS(text=chosenWord)
            
            # Lưu file
            tts_module.save("wordfile.mp3")

            # Chạy file
            playsound(f"{USER_FOLDER}")
            if wordCheck() == True: 
                firstTime = 0
                continue
            else:
                continue
            
        elif userChoice == 2:
            playsound(f"{USER_FOLDER}")
            if wordCheck() == True: 
                firstTime = 0
                continue
            else:
                continue
        
        elif userChoice == 3:
            tts_module = gTTS(text=chosenWord, slow=True)
            remove(f"{USER_FOLDER}")
            tts_module.save("wordfile.mp3")
            playsound(f"{USER_FOLDER}")
            if wordCheck() == True: 
                firstTime = 0
                continue
            else:
                continue
            
        elif userChoice == 4:
            chosenWordSlow = ', '.join(list(chosenWord))
            tts_module = gTTS(text=chosenWordSlow, slow=True)
            remove(f"{USER_FOLDER}")
            tts_module.save("wordfile.mp3")
            playsound(f"{USER_FOLDER}")
            if wordCheck() == True: 
                firstTime = 0
                continue
            else:
                continue
        
        elif userChoice == 5:
            print(f'ĐÁP ÁN: {chosenWord}\n')
            firstTime = 0
            continue
        
        elif userChoice == 0:
            remove(f"{USER_FOLDER}")
            exit()
        else: 
            print(PROMPT3)
            exit()
            
    except ValueError:
        print(PROMPT3)
        exit()

    
