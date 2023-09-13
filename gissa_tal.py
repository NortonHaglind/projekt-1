import random
import os
os.system="cls"
number=random.randint(1, 100)
life=7
game_active=True
acceptable = ["/s", "/f", "/q"] #lista för de som funkar

"""print(f"""##################################################################
        ##################################################################
        ##                                                              ##                                                         
        ##                                                              ##
        ##                                                              ##
        ##                                                              ##
        ##                                                              ##
        ##                                                              ##
        ##                                                              ##
        ##                                                              ##
        ##                                                              ##
        ##                                                              ##
        ##                                                              ##
        ##                                                              ##
        ##                                                              ##
        ##                                                              ##
        ##                                                              ##
        ##                                                              ##
        ##                                                              ##
        ##                                                              ##
        ##################################################################
        ##################################################################""")


print(f"""          Vill du starta skriv /s
          Vill du fuska skriv /f
          Vill du lämna skriv /q""")



while game_active:
    start=input("")
    if start in acceptable: #om det du skrev funkar
        if start=="/q":
            break
        elif start=="/f":
            print(f"{number}")
        elif start=="/s":
            print(f"då kör vi")        
    else:
        print(f"skriv en av dem")
        continue

    print(f"Gissa talet!")
    while game_active:
        try:
            guess=int(input("Skriv ditt tal!: "))
        except: 
            print(f"skriv faktiskt ett tal🤓🤓🤓")
            
        if guess==number:
            print(f"WOHO du klara det!!")
            print(f"Du klara det med {life} liv kvar!")
            game_active=False
        elif guess>number:
            print(f"Talet är lägre")
            life=-1
            print(f"Du har {life} kvar")
            continue
        elif guess<number:
            print(f"Talet är högre")
            life=-1
            print(f"Du har {life} kvar")
            continue
        



        
        


    

