#juliana resendiz


#init
import random
pokemon_level = 0
pokemon_name = "Evee"
day = 1

#function
def level_check():
    if pokemon_level == 5 or 6:
        pokemon_name = "Flareon"
        print("CONGRATULATIONS Your Pokemon has evolved to: "+str(pokemon_name))
    elif pokemon_level == 10 or 11:
        pokemon_name = "Electreon"
        print("CONGRATULATIONS Your Pokemon has evolved to: "+str(pokemon_name))


def game():
    while True:
        day = day + 1
        print("Welcome to Pokemon Evolution, Day: " +str(day))
        print("Select an activity for the day")
        print("""1. Train
2. Gym Battle
3. Rest
4. Quit""")
        activity = int(input("Activity: "))
        if activity == 1:
            global pokemon_level
            pokemon_level = pokemon_level + 1
            level_check()
            print("Pokemon Level: "+str(pokemon_level))
        if activity == 2:
            outcome = random.randint(1,2)
            if outcome == 1:
                pokemon_level = pokemon_level + 2
                level_check()
                print("Pokemon Level: "+str(pokemon_level))
            elif outcome == 2:
                print("Pokemon Level: "+str(pokemon_level))
        if activity == 3:
            print("Pokemon Level: "+(str(pokemon_level)))
            print("Pokemon: "+str(pokemon_name))
        if activity == 4:
            break


#main
game()





