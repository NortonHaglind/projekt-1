import random
import os
os.system="cls"
number=random.randint(1, 100)
life=7
game_active=True
acceptable = ["/s", "/f", "/q"] #lista för de som funkar

print(f"""        ##################################################################
        ##################################################################
        ##                                                              ##                                                         
        ##                 ..           __             __               ##
        ##           \  /  /\  |   |/  |  | |\/| |\/| |__ |\ |          ##
        ##            \/  /  \ |__ |\  |__| |  | |  | |__ | \|          ##
        ##                                                              ##
        ##                      _____                                   ##
        ##                        |   | |   |                           ##
        ##                        |   | |__ |__                         ##
        ##                                                              ##
        ##                    ___     __   __    _                      ##
        ##                   |  __ | |__  |__   /_\                     ##
        ##                   |___| |  __|  __| /   \                    ##
        ##                                                              ##
        ##                  _____   _        __ _____                   ##
        ##                    |    /_\  |   |__   |                     ##
        ##                    |   /   \ |__ |__   |                     ##
        ##                                                              ##
        ##                                                              ##
        ##################################################################
        ##################################################################""")






while game_active:
    

    print(f"Gissa talet!")
    while game_active:
        while True:
            try:
                guess=int(input("Skriv ditt tal!: "))
                break
            except: 
                print(f"skriv faktiskt ett tal🤓🤓🤓")
                continue
        
        
            
        if life==1:
            print(f"du dogade. talet var {number}")
            print(f"""            Vill du försöka igen? skriv /s
            Vill du fusk-köra igen? skriv /f
            Vill du ge upp? skriv /q""")
            while True:
                start=input("")
                if start in acceptable: #om det du skrev funkar
                    if start=="/q":
                        print(f"gg loser ;)")
                        game_active=False
                        break
                    elif start=="/f":
                        print(f"{number}")
                        life=7
                        break
                    elif start=="/s":
                        print(f"då kör vi")  
                        life=7  
                        break 
                else:
                    print(f"skriv en av dem")
                    continue   
        
        elif guess==number:
            print(f"WOHO du klara det!!")
            print(f"Du klara det med {life} liv kvar!")
            game_active=False
        elif guess>number:
            print(f"Talet är lägre")
            life= life-1
            print(f"Du har {life} kvar")
            continue
        elif guess<number:
            print(f"Talet är högre")
            life= life-1
            print(f"Du har {life} kvar")
            continue
          
        



        
        


    

