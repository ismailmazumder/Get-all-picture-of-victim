import os,socket,time,random
path = os.getcwd()
one_logo = '''
  _    _             _              ____             _
 | |  | |           | |            |  _ \           | |
 | |__| |_   _ _ __ | |_ ___ _ __  | |_) |_ __ _   _| |_ ___
 |  __  | | | | '_ \| __/ _ \ '__| |  _ <| '__| | | | __/ _ \
 | |  | | |_| | | | | ||  __/ |    | |_) | |  | |_| | ||  __/
 |_|  |_|\__,_|_| |_|\__\___|_|    |____/|_|   \__,_|\__\___|

'''
two_logo = '''
 _   _             _             ______            _
| | | |           | |            | ___ \          | |
| |_| |_   _ _ __ | |_ ___ _ __  | |_/ /_ __ _   _| |_ ___
|  _  | | | | '_ \| __/ _ \ '__| | ___ \ '__| | | | __/ _ \
| | | | |_| | | | | ||  __/ |    | |_/ / |  | |_| | ||  __/
\_| |_/\__,_|_| |_|\__\___|_|    \____/|_|   \__,_|\__\___|
'''
three = '''

██   ██ ██    ██ ███    ██ ████████ ███████ ██████      ██████  ██████  ██    ██ ████████ ███████ 
██   ██ ██    ██ ████   ██    ██    ██      ██   ██     ██   ██ ██   ██ ██    ██    ██    ██      
███████ ██    ██ ██ ██  ██    ██    █████   ██████      ██████  ██████  ██    ██    ██    █████   
██   ██ ██    ██ ██  ██ ██    ██    ██      ██   ██     ██   ██ ██   ██ ██    ██    ██    ██      
██   ██  ██████  ██   ████    ██    ███████ ██   ██     ██████  ██   ██  ██████     ██    ███████                                                                                                   
'''
four = '''

ooooo   ooooo                             .                           oooooooooo.                           .             
`888'   `888'                           .o8                           `888'   `Y8b                        .o8             
 888     888  oooo  oooo  ooo. .oo.   .o888oo  .ooooo.  oooo d8b       888     888 oooo d8b oooo  oooo  .o888oo  .ooooo.  
 888ooooo888  `888  `888  `888P"Y88b    888   d88' `88b `888""8P       888oooo888' `888""8P `888  `888    888   d88' `88b 
 888     888   888   888   888   888    888   888ooo888  888           888    `88b  888      888   888    888   888ooo888 
 888     888   888   888   888   888    888 . 888    .o  888           888    .88P  888      888   888    888 . 888    .o 
o888o   o888o  `V88V"V8P' o888o o888o   "888" `Y8bod8P' d888b         o888bood8P'  d888b     `V88V"V8P'   "888" `Y8bod8P'                                                                                                                                                                                                                                                                                                                                                                              
'''
logo_list = [one_logo,two_logo,three,four]
print(random.choice(logo_list))
print("May you lose some file. If you want to get better experience you need high speed internet.\n Thank You.")
ip = "127.0.0.1"
port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip,port))
fol_name = input("Enter the folder name : ")
try:
    os.mkdir(fol_name)
except:
    pass
fol_path = path+f"\\{fol_name}"
os.chdir(fol_path)
server.listen(10)
conn , addr = server.accept()
while True:
    try:
        file_name = conn.recv(1096).decode('ascii')
        print(file_name)
    except:
        file_name = conn.recv(1096)
        print(file_name)
        break
    file_make = open(file_name,"wb")
    file_data = conn.recv(2000)
    while file_data:
        file_make.write(file_data)
        file_data = conn.recv(2000)
        try:
            file_data_str = file_data.decode('utf-8')
            if "jpg" in file_data_str or ".png" in file_data_str:
                print(file_data_str)
                file_make = open(file_data_str,"wb")
                file_data = conn.recv(2000)
        except:
            #print(file_data)
            #print("Try again. It is for your internet connection or ngrok.")
            pass