#AP CSP Create Task Project


#init
from PIL import Image
import requests
from io import BytesIO
import time
import random



menu = ["https://sigmawire.net/i/04/ANVB9S.png"] #original menu created by me
capybaras =["https://tinyurl.com/2wekrz25", # one capybara with another in the background. Image Source: Tasting Table. 2022. Accessed Via: https://tinyurl.com/2u4wsruc
            "https://tinyurl.com/5bw4sksr", # majestic capybara.  Image Source: Tasting Table. 2022. Accessed Via: https://tinyurl.com/2u4wsruc
            "https://tinyurl.com/36xufrec", # cute capybara with oranges on its side. Image Source: Interesting Animals. 2024. Accessed Via: https://tinyurl.com/yc3zn6az
            "https://tinyurl.com/28jrmp5y", # capybara w/ bird on head. Image Source: Interesting Animals. 2024. Accessed Via: https://tinyurl.com/yc3zn6az
            "https://tinyurl.com/ytkkync8", # capybara in water. Image Source: Interesting Animals. 2024. Accessed Via: https://tinyurl.com/yc3zn6az
            "https://tinyurl.com/2t5bvxwz", # mama capy with baby on back. Image Source: Interesting Animals. 2024. Accessed Via: https://tinyurl.com/yc3zn6az
            "https://tinyurl.com/2hr6a849", # portrait of capy. Image Source: Interesting Animals. 2024. Accessed Via: https://tinyurl.com/yc3zn6az
            "https://tinyurl.com/2276wyku", # capy staring at camera. Image Source: Interesting Animals. 2024. Accessed Via: https://tinyurl.com/yc3zn6az
            "https://tinyurl.com/bpajcwkj", # rude capy giving sideye. Image Source: Rested Paws. 2022. Accessed Via: https://tinyurl.com/5ypcf287
            ]
personalities = ["Dave: playful, extroverted", #all names and personalities were made up by me
                 "Stuart: calm, introverted",
                 "Kevin: lazy, introverted",
                 "Bob: calm, extroverted",
                 "Tom and Carl: cuddly, friendly, extroverted",
                 "Jerry: calm, introverted",
                 "Phil: cuddly, extroverted",
                 "Tim: shy, introverted",
                 "Dave: lazy, introverted"] #names and personalities for all capybaras, match up with images/in order with images
filtered_list = []


#function
def open_image(image): #one of the base functions to print a certain image whenever it was needed
    response = requests.get(image)
    img = Image.open(BytesIO(response.content))
    img.show()


def capys():
    open_image(capybaras[0])#dave
    open_image(capybaras[1])#stuart
    open_image(capybaras[2])#kevin
    open_image(capybaras[3])#bob
    open_image(capybaras[4])#tom and carl
    open_image(capybaras[5])#jerry
    open_image(capybaras[6])#phil
    open_image(capybaras[7])#tim
    open_image(capybaras[8])#dave


def capybara_cafe(name):
    Total = 0
    while True:
        print("─── ⋆⋅☆⋅⋆ ──WELCOME "+name+" to the Grand Opening of our Capybara Cafe─── ⋆⋅☆⋅⋆ ──")
        print("\n")
        print("At our cafe you can: \n 1. Order Drinks☕ \n 2. Order Pastries🥐 \n 3. Order Lunch🥪 \n 4. Choose a Capybara to keep you company🧸 \n 5. Exit the Cafe🛑")
        ans = input("Please enter the according number based on where you would like to start: ")
        if ans == "1": 
            print("Please take a look at our menu and make your selection")
            open_image(menu[0])
            drink = input("Drink Choice: ")
            if drink == "Cappyccino":
                print("...making drink...")
                print("\n")
                time.sleep(3)
                print("Great Choice! Enjoy your drink🍵")
                Total = Total + 7
            elif drink == "Americano":
                print("...making drink...")
                print("\n")
                time.sleep(3)
                print("Great Choice! Enjoy your drink☕")
                Total = Total + 5
            elif drink == "Latte":
                print("...making drink...")
                print("\n")
                time.sleep(3)
                print("Great Choice! Enjoy your drink🍵")
                Total = Total + 6
            elif drink == "Lemonade":
                print("...making drink...")
                print("\n")
                time.sleep(3)
                print("Great Choice! Enjoy your drink☕")
                Total = Total + 3
            else:
                print("Invalid Input, Please Try Again.")
        elif ans == "2":#code for option 2
            print("Please take a look at our menu and make your selection")
            open_image(menu[0])
            pastry = input("Pastry Choice: ")
            if pastry ==  "Croissant":
                print("...warming up pastry...")
                print("\n")
                time.sleep(3)
                print("Great Choice! Enjoy your freshly baked pastry🍰")
                Total = Total + 4
            elif pastry == "Danish":
                print("...warming up pastry...")
                print("\n")
                time.sleep(3)
                print("Great Choice! Enjoy your freshly baked pastry🥐")
                Total = Total + 3
            elif pastry == "Macarons":
                print("...warming up pastry...")
                print("\n")
                time.sleep(3)
                print("Great Choice! Enjoy your freshly baked pastry🍰")
                Total = Total + 6
            elif pastry == "Cheesecake" or pastry ==  "Cheesecake Slice":
                print("...baking pastry...")
                print("\n")
                time.sleep(3)
                print("Great Choice! Enjoy your freshly baked pastry🥐")
                Total = Total + 8
            elif pastry == "Strawberry Cake" or pastry == "Strawberry Cake Slice":
                print("...baking pastry...")
                print("\n")
                time.sleep(3)
                print("Great Choice! Enjoy your freshly baked pastry🍰")
                Total = Total + 7
        elif ans == "3": #code for option 3
            print("Please take a look at our menu and make your selection")
            open_image(menu[0])
            lunch = input("Lunch Choice: ")
            if lunch ==  "Cobb Salad":
                print("...tossing salad ingredients...")
                print("\n")
                time.sleep(3)
                print("Great Choice! Enjoy your salad🥗")
                Total = Total + 12
            elif lunch == "Bacon, Egg, Cheese":
                print("...cooking up eggs and bacon...")
                print("\n")
                time.sleep(3)
                print("Great Choice! Enjoy your sandwich🥯")
                Total = Total + 13
            elif lunch == "BLT":
                print("...assembling sandwich...")
                print("\n")
                time.sleep(3)
                print("Great Choice! Enjoy your sandiwich🥯")
                Total = Total + 15
            elif lunch == "Beef Toast":
                print("...spreading beef...")
                print("\n")
                time.sleep(3)
                print("Great Choice! Enjoy your sandwich🥯")
        elif ans == "4": #code for option 4
            cap = input("Would you like to: \n a. Choose your own capybaras \n b. Receive a capybara recommendation")
            print("*Having a capybara companion costs $10")
            if cap == "a":
                print("Here are all of our available capybaras:")
                capys()
                print("And here are their names and temperaments:")
                print(personalities[0])
                print(personalities[1])
                print(personalities[2])
                print(personalities[3])
                print(personalities[4])
                print(personalities[5])
                print(personalities[6])
                print(personalities[7])
                print(personalities[8])
                ans = input("Enter the name of your desired capybara companion: ")
                if ans == "Dave": #code for what comes after a certain capybara is chosen
                    print("")
                    print("Great choice!")
                    personalities[0]
                    capybaras[0]
                    print("Enjoy your time with your capybara")
                    Total = Total + 10
                elif ans == "Stuart":
                    print("")
                    print("Great choice!")
                    personalities[1]
                    capybaras[1]
                    print("Enjoy your time with your capybara")
                    Total = Total + 10
                elif ans == "Kevin":
                    print("")
                    print("Great choice!")
                    personalities[2]
                    capybaras[2]
                    print("Enjoy your time with your capybara")
                    Total = Total + 10
                elif ans == "Bob":
                    print("")
                    print("Great choice!")
                    personalities[3]
                    capybaras[3]
                    print("Enjoy your time with your capybara")
                    Total = Total + 10
                elif ans == "Tom and Carl":
                    print("")
                    print("Great choice!")
                    personalities[4]
                    capybaras[4]
                    print("Enjoy your time with your capybara")
                    Total = Total + 10
                elif ans == "Jerry":
                    print("")
                    print("Great choice!")
                    personalities[5]
                    capybaras[5]
                    print("Enjoy your time with your capybara")
                    Total = Total + 10
                elif ans == "Phil":
                    print("")
                    print("Great choice!")
                    personalities[6]
                    capybaras[6]
                    print("Enjoy your time with your capybara")
                    Total = Total + 10
                elif ans == "Tim":
                    print("")
                    print("Great choice!")
                    personalities[7]
                    capybaras[7]
                    print("Enjoy your time with your capybara")
                    Total = Total + 10
                elif ans == "Dave":
                    print("")
                    print("Great choice!")
                    personalities[7]
                    capybaras[7]
                    print("Enjoy your time with your capybara")
                    Total = Total + 10
            elif cap == "b":
                capy = input("What kind of temperament would you like? (playful, cuddly, shy, lazy, calm, extroverted, introverted)")
                for i in range(len(personalities)): #finds the users input in personalities and adds the corresponding image into a filtered list
                    if capy in personalities[i]:
                        filtered_list.append(capybaras[i])
                        recommendation = random.choice(filtered_list)# a recommendation is pulled from that filtered list and given to the user
                print("Based on you wishes above I recomend you...")#formal recommendation
                time.sleep(2)
                open_image(recommendation)
                print("We hope you appreciate your recommendation")
                if len(filtered_list) == 0:
                    print("No results found, try another word")
            else:
                print("Invalid input. Please enter a or b.")
        elif ans == "5": #code for option 5
            print("Thank you for your time. We hope you enjoyed your stay")
            print("Your total after your stay with us is: $"+str(Total)) #cost of items and capybaras is tallied up and presented when user wishes to end/exit the function
            print("\n")
            print("Come again soon❗")
            Total = 0
            break
        else:
            print("Invalid Input. Please enter the correct number according to the menu.")

#main
capybara_cafe("")#enter name or name you wish to be called by here in the quotations.

