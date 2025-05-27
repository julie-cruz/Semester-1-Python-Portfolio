#juliana resendiz
#dog breeds
#CREATE,practice

from PIL import Image
import requests
from io import BytesIO
import random
import time

dog_breeds = ["Affenpinscher","AfghanHound","AiredaleTerrier","AkbashDog","Akita","AlapahaBlueBloodBulldog","AlaskanHusky","AlaskanMalamute","AmericanEskimoDog","AmericanFoxhound","AmericanPitBullTerrier","AmericanWaterSpaniel","AnatolianShepherdDog","AustralianKelpie","AustralianShepherd","Azawakh","Basenji","BassetBleudeGascogne","Beagle","Beauceron","BedlingtonTerrier","BelgianMalinois","BelgianTervuren","BerneseMountainDog","BlackandTanCoonhound","Bloodhound","BluetickCoonhound","Boerboel","BorderTerrier","BostonTerrier","BouvierdesFlandres","Boxer","BoykinSpaniel","BraccoItaliano","Briard","Brittany","Bullmastiff","CairnTerrier","CaneCorso","CardiganWelshCorgi","CatahoulaLeopardDog","CaucasianShepherd(Ovcharka)","CavalierKingCharlesSpaniel","ChineseCrested","Chinook","ChowChow","ClumberSpaniel","CockerSpaniel(American)","CotondeTulear","Dalmatian","DogoArgentino","EnglishShepherd","EnglishSpringerSpaniel","Eurasier","FieldSpaniel","FinnishLapphund","GermanPinscher","GermanShepherdDog","GermanShorthairedPointer","GiantSchnauzer","GlenofImaalTerrier","GoldenRetriever","GordonSetter","GreatDane","GreatPyrenees","Greyhound","Harrier","Havanese","IrishSetter","IrishWolfhound","ItalianGreyhound","JapaneseChin","Keeshond","Komondor","Kuvasz","LabradorRetriever","LagottoRomagnolo","Leonberger","LhasaApso","Maltese","MiniatureSchnauzer","Newfoundland","NorfolkTerrier","Papillon","PembrokeWelshCorgi","PharaohHound","Plott","Pug","RedboneCoonhound","RhodesianRidgeback","Rottweiler","Samoyed","Schipperke","ScottishDeerhound","ShihTzu","SilkyTerrier","SoftCoatedWheatenTerrier","SpanishWaterDog","Vizsla","Weimaraner"]
dog_weights = [6,50,40,90,65,55,38,65,20,65,30,25,80,31,35,33,22,35,20,80,17,40,40,65,65,80,45,110,12,10,70,50,25,55,70,30,100,13,88,25,50,80,13,10,50,40,55,20,9,50,80,44,35,40,35,33,25,50,45,65,32,55,45,110,85,50,40,7,35,105,7,4,35,80,70,55,24,120,12,4,11,100,11,3,25,40,40,14,45,75,75,50,10,70,9,8,30,30,50,55]
filtered_list = []
dog_temperaments = ["Stubborn,Curious,Playful,Adventurous,Active,Fun-loving","Aloof,Clownish,Dignified,Independent,Happy","Outgoing,Friendly,Alert,Confident,Intelligent,Courageous","Loyal,Independent,Intelligent,Brave","Docile,Alert,Responsive,Dignified,Composed,Friendly,Receptive,Faithful,Courageous","Loving,Protective,Trainable,Dutiful,Responsible","Friendly,Energetic,Loyal,Gentle,Confident","Friendly,Affectionate,Devoted,Loyal,Dignified,Playful","Friendly,Alert,Reserved,Intelligent,Protective","Kind,Sweet-Tempered,Loyal,Independent,Intelligent,Loving","StrongWilled,Stubborn,Friendly,Clownish,Affectionate,Loyal,Obedient,Intelligent,Courageous","Friendly,Energetic,Obedient,Intelligent,Protective,Trainable","Steady,Bold,Independent,Confident,Intelligent,Proud","Friendly,Energetic,Alert,Loyal,Intelligent,Eager","Good-natured,Affectionate,Intelligent,Active,Protective","Aloof,Affectionate,Attentive,Rugged,Fierce,Refined","Affectionate,Energetic,Alert,Curious,Playful,Intelligent","Affectionate,Lively,Agile,Curious,Happy,Active","Amiable,EvenTempered,Excitable,Determined,Gentle,Intelligent","Fearless,Friendly,Intelligent,Protective,Calm","Affectionate,Spirited,Intelligent,Good-tempered","Watchful,Alert,Stubborn,Friendly,Confident,Hard-working,Active,Protective","Energetic,Alert,Loyal,Intelligent,Attentive,Protective","Affectionate,Loyal,Intelligent,Faithful","Easygoing,Gentle,Adaptable,Trusting,EvenTempered,Lovable","Stubborn,Affectionate,Gentle,EvenTempered","Friendly,Intelligent,Active","Obedient,Confident,Intelligent,Dominant,Territorial","Fearless,Affectionate,Alert,Obedient,Intelligent,EvenTempered","Friendly,Lively,Intelligent","Protective,Loyal,Gentle,Intelligent,Familial,Rational","Devoted,Fearless,Friendly,Cheerful,Energetic,Loyal,Playful,Confident,Intelligent,Bright,Brave,Calm","Friendly,Energetic,Companionable,Intelligent,Eager,Trainable","Stubborn,Affectionate,Loyal,Playful,Companionable,Trainable","Fearless,Loyal,Obedient,Intelligent,Faithful,Protective","Agile,Adaptable,Quick,Intelligent,Attentive,Happy","Docile,Reliable,Devoted,Alert,Loyal,Reserved,Loving,Protective,Powerful,Calm,Courageous","Hardy,Fearless,Assertive,Gay,Intelligent,Active","Trainable,Reserved,Stable,Quiet,EvenTempered,Calm","Affectionate,Devoted,Alert,Companionable,Intelligent,Active","Energetic,Inquisitive,Independent,Gentle,Intelligent,Loving","Alert,Quick,Dominant,Powerful,Calm,Strong","Fearless,Affectionate,Sociable,Patient,Playful,Adaptable","Affectionate,Sweet-Tempered,Lively,Alert,Playful,Happy","Friendly,Alert,Dignified,Intelligent,Calm","Aloof,Loyal,Independent,Quiet","Affectionate,Loyal,Dignified,Gentle,Calm,Great-hearted","Outgoing,Sociable,Trusting,Joyful,EvenTempered,Merry","Affectionate,Lively,Playful,Intelligent,Trainable,Vocal","Outgoing,Friendly,Energetic,Playful,Sensitive,Intelligent,Active","Friendly,Affectionate,Cheerful,Loyal,Tolerant,Protective","Kind,Energetic,Independent,Adaptable,Intelligent,Bossy","Affectionate,Cheerful,Alert,Intelligent,Attentive,Active","Alert,Reserved,Intelligent,EvenTempered,Watchful,Calm","Docile,Cautious,Sociable,Sensitive,Adaptable,Familial","Friendly,Keen,Faithful,Calm,Courageous","Spirited,Lively,Intelligent,Loving,EvenTempered,Familial","Alert,Loyal,Obedient,Curious,Confident,Intelligent,Watchful,Courageous","Boisterous,Bold,Affectionate,Intelligent,Cooperative,Trainable","StrongWilled,Kind,Loyal,Intelligent,Dominant,Powerful","Spirited,Agile,Loyal,Gentle,Active,Courageous","Intelligent,Kind,Reliable,Friendly,Trustworthy,Confident","Fearless,Alert,Loyal,Confident,Gay,Eager","Friendly,Devoted,Reserved,Gentle,Confident,Loving","StrongWilled,Fearless,Affectionate,Patient,Gentle,Confident","Affectionate,Athletic,Gentle,Intelligent,Quiet,EvenTempered","Outgoing,Friendly,Cheerful,Sweet-Tempered,Tolerant,Active","Affectionate,Responsive,Playful,Companionable,Gentle,Intelligent","Affectionate,Energetic,Lively,Independent,Playful,Companionable","Sweet-Tempered,Loyal,Dignified,Patient,Thoughtful,Generous","Mischievous,Affectionate,Agile,Athletic,Companionable,Intelligent","Alert,Loyal,Independent,Intelligent,Loving,Cat-like","Agile,Obedient,Playful,Quick,Sturdy,Bright","Steady,Fearless,Affectionate,Independent,Gentle,Calm","Clownish,Loyal,Patient,Independent,Intelligent,Protective","Kind,Outgoing,Agile,Gentle,Intelligent,Trusting,EvenTempered","Keen,Loyal,Companionable,Loving,Active,Trainable","Obedient,Fearless,Loyal,Companionable,Adaptable,Loving","Steady,Fearless,Friendly,Devoted,Assertive,Spirited,Energetic,Lively,Alert,Obedient,Playful,Intelligent","Playful,Docile,Fearless,Affectionate,Sweet-Tempered,Lively,Responsive,Easygoing,Gentle,Intelligent,Active","Fearless,Friendly,Spirited,Alert,Obedient,Intelligent","Sweet-Tempered,Gentle,Trainable","Self-confidence,Fearless,Spirited,Companionable,Happy,Lovable","Hardy,Friendly,Energetic,Alert,Intelligent,Happy","Tenacious,Outgoing,Friendly,Bold,Playful,Protective","Affectionate,Sociable,Playful,Intelligent,Active,Trainable","Bold,Alert,Loyal,Intelligent","Docile,Clever,Charming,Stubborn,Sociable,Playful,Quiet,Attentive","Affectionate,Energetic,Independent,Companionable,Familial,Unflappable","StrongWilled,Mischievous,Loyal,Dignified,Sensitive,Intelligent","Steady,Good-natured,Fearless,Devoted,Alert,Obedient,Confident,Self-assured,Calm,Courageous","Stubborn,Friendly,Sociable,Lively,Alert,Playful","Fearless,Agile,Curious,Independent,Confident,Faithful","Docile,Friendly,Dignified,Gentle","Clever,Spunky,Outgoing,Friendly,Affectionate,Lively,Alert,Loyal,Independent,Playful,Gentle,Intelligent,Happy,Active,Courageous","Friendly,Responsive,Inquisitive,Alert,Quick,Joyful","Affectionate,Spirited,Energetic,Playful,Intelligent,Faithful","Trainable,Diligent,Affectionate,Loyal,Athletic,Intelligent","Affectionate,Energetic,Loyal,Gentle,Quiet","Steady,Aloof,Stubborn,Energetic,Alert,Intelligent,Powerful,Fast"]
dog_image = ["https://cdn2.thedogapi.com/images/0LJiOVlxp.jpg","https://cdn2.thedogapi.com/images/tChrH8dDJ.jpg","https://cdn2.thedogapi.com/images/PG8UPLSVU.jpg","https://cdn2.thedogapi.com/images/SyfsC19NQ_1280.jpg","https://cdn2.thedogapi.com/images/36TXlWMDf.jpg","https://cdn2.thedogapi.com/images/33mJ-V3RX.jpg","https://cdn2.thedogapi.com/images/-HgpNnGXl.jpg","https://cdn2.thedogapi.com/images/GhtSdrW29.jpg","https://cdn2.thedogapi.com/images/EB8A5HQHX.jpg","https://cdn2.thedogapi.com/images/uISezUGDV.jpg","https://cdn2.thedogapi.com/images/HkC31gcNm_1280.png","https://cdn2.thedogapi.com/images/SkmRJl9VQ_1280.jpg","https://cdn2.thedogapi.com/images/BJT0Jx5Nm_1280.jpg","https://cdn2.thedogapi.com/images/Hyq1ge9VQ_1280.jpg","https://cdn2.thedogapi.com/images/B1-llgq4m_1280.jpg","https://cdn2.thedogapi.com/images/SkvZgx94m_1280.jpg","https://cdn2.thedogapi.com/images/H1dGlxqNQ_1280.jpg","https://cdn2.thedogapi.com/images/BkMQll94X_1280.jpg","https://cdn2.thedogapi.com/images/Syd4xxqEm_1280.jpg","https://cdn2.thedogapi.com/images/HJQ8ge5V7_1280.jpg","https://cdn2.thedogapi.com/images/ByK8gx947_1280.jpg","https://cdn2.thedogapi.com/images/r1f_ll5VX_1280.jpg","https://cdn2.thedogapi.com/images/B1KdxlcNX_1280.jpg","https://cdn2.thedogapi.com/images/S1fFlx5Em_1280.jpg","https://cdn2.thedogapi.com/images/HJAFgxcNQ_1280.jpg","https://cdn2.thedogapi.com/images/Skdcgx9VX_1280.jpg","https://cdn2.thedogapi.com/images/rJxieg9VQ_1280.jpg","https://cdn2.thedogapi.com/images/HyOjge5Vm_1280.jpg","https://cdn2.thedogapi.com/images/HJOpge9Em_1280.jpg","https://cdn2.thedogapi.com/images/rkZRggqVX_1280.jpg","https://cdn2.thedogapi.com/images/Byd0xl5VX_1280.jpg","https://cdn2.thedogapi.com/images/ry1kWe5VQ_1280.jpg","https://cdn2.thedogapi.com/images/ryHJZlcNX_1280.jpg","https://cdn2.thedogapi.com/images/S13yZg5VQ_1280.jpg","https://cdn2.thedogapi.com/images/rkVlblcEQ_1280.jpg","https://cdn2.thedogapi.com/images/HJWZZxc4X_1280.jpg","https://cdn2.thedogapi.com/images/r1ifZl5E7_1280.jpg","https://cdn2.thedogapi.com/images/Sk7Qbg9E7_1280.jpg","https://cdn2.thedogapi.com/images/r15m-lc4m_1280.jpg","https://cdn2.thedogapi.com/images/SyXN-e9NX_1280.jpg","https://cdn2.thedogapi.com/images/BJcNbec4X_1280.jpg","https://cdn2.thedogapi.com/images/r1rrWe5Em_1280.jpg","https://cdn2.thedogapi.com/images/HJRBbe94Q_1280.jpg","https://cdn2.thedogapi.com/images/B1pDZx9Nm_1280.jpg","https://cdn2.thedogapi.com/images/Sypubg54Q_1280.jpg","https://cdn2.thedogapi.com/images/ry8KWgqEQ_1280.jpg","https://cdn2.thedogapi.com/images/rkeqWgq4Q_1280.jpg","https://cdn2.thedogapi.com/images/HkRcZe547_1280.jpg","https://cdn2.thedogapi.com/images/SyviZlqNm_1280.jpg","https://cdn2.thedogapi.com/images/SkJ3blcN7_1280.jpg","https://cdn2.thedogapi.com/images/S1nhWx94Q_1280.jpg","https://cdn2.thedogapi.com/images/H1QyMe5EQ_1280.jpg","https://cdn2.thedogapi.com/images/Hk0Jfe5VQ_1280.jpg","https://cdn2.thedogapi.com/images/S1VWGx9Nm_1280.jpg","https://cdn2.thedogapi.com/images/SkJfGecE7_1280.jpg","https://cdn2.thedogapi.com/images/S1KMGg5Vm_1280.jpg","https://cdn2.thedogapi.com/images/B1u4zgqE7_1280.jpg","https://cdn2.thedogapi.com/images/SJyBfg5NX_1280.jpg","https://cdn2.thedogapi.com/images/SJqBMg5Nm_1280.jpg","https://cdn2.thedogapi.com/images/H1NIzlcV7_1280.jpg","https://cdn2.thedogapi.com/images/H1oLMe94m_1280.jpg","https://cdn2.thedogapi.com/images/HJ7Pzg5EQ_1280.jpg","https://cdn2.thedogapi.com/images/SJ5vzx5NX_1280.jpg","https://cdn2.thedogapi.com/images/B1Edfl9NX_1280.jpg","https://cdn2.thedogapi.com/images/B12uzg9V7_1280.png","https://cdn2.thedogapi.com/images/ryNYMx94X_1280.jpg","https://cdn2.thedogapi.com/images/B1IcfgqE7_1280.jpg","https://cdn2.thedogapi.com/images/rkXiGl9V7_1280.jpg","https://cdn2.thedogapi.com/images/S1osGeqVm_1280.jpg","https://cdn2.thedogapi.com/images/Hyd2zgcEX_1280.jpg","https://cdn2.thedogapi.com/images/SJAnzg9NX_1280.jpg","https://cdn2.thedogapi.com/images/r1H6feqEm_1280.jpg","https://cdn2.thedogapi.com/images/S1GAGg9Vm_1280.jpg","https://cdn2.thedogapi.com/images/Bko0fl547_1280.jpg","https://cdn2.thedogapi.com/images/BykZ7ecVX_1280.jpg","https://cdn2.thedogapi.com/images/B1uW7l5VX_1280.jpg","https://cdn2.thedogapi.com/images/ryzzmgqE7_1280.jpg","https://cdn2.thedogapi.com/images/ByrmQlqVm_1280.jpg","https://cdn2.thedogapi.com/images/SJp7Qe5EX_1280.jpg","https://cdn2.thedogapi.com/images/B1SV7gqN7_1280.jpg","https://cdn2.thedogapi.com/images/SJIUQl9NX_1280.jpg","https://cdn2.thedogapi.com/images/Sk4DXl54m_1280.jpg","https://cdn2.thedogapi.com/images/B1ADQg94X_1280.jpg","https://cdn2.thedogapi.com/images/SkJj7e547_1280.jpg","https://cdn2.thedogapi.com/images/rJ6iQeqEm_1280.jpg","https://cdn2.thedogapi.com/images/Byz6mgqEQ_1280.jpg","https://cdn2.thedogapi.com/images/B1i67l5VQ_1280.jpg","https://cdn2.thedogapi.com/images/HyJvcl9N7_1280.jpg","https://cdn2.thedogapi.com/images/HJMzEl5N7_1280.jpg","https://cdn2.thedogapi.com/images/By9zNgqE7_1280.jpg","https://cdn2.thedogapi.com/images/r1xXEgcNX_1280.jpg","https://cdn2.thedogapi.com/images/S1T8Ee9Nm_1280.jpg","https://cdn2.thedogapi.com/images/SyBvVgc47_1280.jpg","https://cdn2.thedogapi.com/images/SkNjqx9NQ_1280.jpg","https://cdn2.thedogapi.com/images/BkrJjgcV7_1280.jpg","https://cdn2.thedogapi.com/images/ByzGsl5Nm_1280.jpg","https://cdn2.thedogapi.com/images/HJHmix5NQ_1280.jpg","https://cdn2.thedogapi.com/images/HJf4jl9VX_1280.jpg","https://cdn2.thedogapi.com/images/r1o0jx9Em_1280.jpg","https://cdn2.thedogapi.com/images/SyU12l9V7_1280.jpg"]
bred_for = ["Smallrodenthunting,lapdog","Coursingandhunting","Badger,otterhunting","Sheepguarding","Huntingbears","Guarding","Sledpulling","Haulingheavyfreight,Sledpulling","Circusperformer","Foxhunting,scenthound","Fighting","Birdflushingandretrieving","Livestockherding","Farmdog,Cattleherding","Sheepherding","Livestockguardian,hunting","Hunting","Huntingonfoot.","Rabbit,harehunting","Boarherding,hunting,guarding","Killingrat,badger,othervermin","Stockherding","Guarding,Drafting,Policework.","Draftwork","Huntingraccoons,nighthunting","Trailing","Huntingwithasuperiorsenseofsmell.","Guardingthehomestead,farmwork.","Foxbolting,ratting","Ratting,Companionship","Cattleherding","Bull-baiting,guardian","Turkeyretrieving","Versatilegundog","Herding,guardingsheep","Pointing,retrieving","Estateguardian","Boltingofotter,foxes,othervermin","Companion,guarddog,andhunter","Cattledroving","Drivinglivestock","Guarddogs,defendingsheepfrompredators,mainlywolves,jackalsandbears","Flushingsmallbirds,companion","Ratting,lapdog,curio","Sledpulling","Guardian,cartpulling,hunting","Birdflushing,retrieving","HuntingtheAmericanwoodcock","Accompanyingladiesonlongseavoyages,rattersonboardship.","Carriagedog-trotalongsidecarriagestoprotecttheoccupantsfrombanditryorotherinterference","Big-gamehunting","Herding&guardinglivestock,farmwatchdog","Birdflushing,retrieving","Companionship","Birdflushing,retrieving","Herdingreindeer","Watchdog,Huntingverminonthefarm.","Herding,Guarddog","Generalhunting","Herding,guarding","Ridthehomeandfarmofvermin,andhuntbadgerandfox","Retrieving","Findandpointgamebirds","Hunting&holdingboars,Guardian","Sheepguardian","Coursinghares","Huntingharesbytrailingthem","Companionship","Birdsetting,retrieving","Coursingwolves,elk","Lapdog","Lapdog","Bargewatchdog","Sheepguardian","Guardian,huntinglargegame","Waterretrieving","WaterretrievaldoginthemarshesofRomagna","Guardian,appearance.","Guardinginsidethehome,companion","Lapdog","Ratting","Allpurposewaterdog,fishingaid","Ratting,foxbolting","Lapdog","DrivingstocktomarketinnorthernWales","Huntingrabbits","Huntingbig-gamelikeBoar.","Lapdog","Huntingraccoon,deer,bear,andcougar.","Biggamehunting,guarding","Cattledrover,guardian,draft","Herdingreindeer,guardian,draft","Bargewatchdog","Coursingdeer","Lapdog","Smallverminhunting,companionship","Verminhunting,guarding,all-aroundfarmhelper","Herdingflocksofsheepandgoatsfromonepasturetoanother","Pointingandtrailing","Largegametrailingandversatilegundog"]
#^all the necessary lists for the functions below


#init




#function
def open_image(image): #one of the base functions to print a certain image whenever it was needed
    response = requests.get(image)
    img = Image.open(BytesIO(response.content))
    img.show()
    


def dog_size(): #function alows for user to recieve multiple dog breeds recomendations that meet their criteria/input
    x = input("What size dog are you looking for? (tiny, small, medium, large)")
    if x == "tiny":
        for i in range(len(dog_weights)):
            if dog_weights[i] <= 10:
                filtered_list.append(dog_breeds[i])
        print(filtered_list)
        dog = random.choice(filtered_list)
        print("Based on your preference above I recomend... ")#formal recomendation
        time.sleep(2)
        print("Dog Breed: "+dog)
    elif x == "small":
        for i in range(len(dog_weights)):
            if dog_weights[i] >= 11 and dog_weights[i] <= 25:
                filtered_list.append(dog_breeds[i])
        print(filtered_list)
        dog = random.choice(filtered_list)
        print("Based on your preference above I recomend... ")#formal recomendation
        time.sleep(2)
        print("Dog Breed: "+dog)
    elif x == "medium":
        for i in range(len(dog_weights)):
            if dog_weights[i] >= 26 and dog_weights[i] <= 60:
                filtered_list.append(dog_breeds[i])
        print(filtered_list)
        dog = random.choice(filtered_list)
        print("Based on your preference above I recomend... ")#formal recomendation
        time.sleep(2)
        print("Dog Breed: "+dog)
    elif x == "large":
        for i in range(len(dog_weights)):
            if dog_weights[i] > 60:
                filtered_list.append(dog_breeds[i])
        print(filtered_list)
        dog = random.choice(filtered_list)
        print("Based on your preference above I recomend... ")#formal recomendation
        time.sleep(2)
        print("Dog Breed: "+dog)
    else:
        print("No results found. Please try again")



def dog_characteristics(): # allows user to input a specific dog breed they are curious about and displays dogs temperaments and an image of the dog breed
    dog = input("What kind of dog breed would you like to view and image of as well as learn its temperament/behaviors?")
    if dog in dog_breeds:
        x = dog_breeds.index(dog)
        print(dog)#formal recomendation
        print(dog_temperaments[x])
        pic = dog_image[x]
        open_image(pic)
    if dog not in dog_breeds:
        print("No results found. Please try again")



def breed_purpose(): #allows for user to input a purpose fo what they want a dog for and code outputs recomendation of dog breed from dog breeds that fir the criteria as well as displays a list with all the other dog breeds with the same criteria met
    breed = input("Dog breed purpose: ")
    for i in range(len(bred_for)):
        if breed in bred_for[i]:
            filtered_list.append(dog_breeds[i])
            recomendation = random.choice(filtered_list)
        else:
            recomendation = " No recomendation possible "
    print("Based on you wishes above I recomend you...")#formal recomendation
    time.sleep(2)
    print("Dog Breed: "+recomendation)
    print("Here are other options with the same purpose: ")
    print(filtered_list)
    if len(filtered_list) == 0:
        print("No results found, try another word")



def dog_breed_choosing():#giant function for all the code to be in a menu for the user to view more simply, contains all the previous functions under this one
    while True:
        print("Hello Welcome to your very own Dog Breed Chooser Assistant")
        print("THis program is here to: answer questions, provide recomendations based on criteria, provide lists fitting criteria")
        print("Where would you like to begin? \n Search dogs based on size (a) \n Search dogs based on characteristics (b) \n Search dogs based on breeds purpose (c) \n View all dog breeds in database (d) ")
        menu_choice = input("Menu Selection: ")
        if menu_choice == "a":
            dog_size()
            ans = input("Would you like to continue this program: yes or no ?")
            if ans == "no":
                break
        elif menu_choice == "b":
            dog_characteristics()
            ans = input("Would you like to continue this program: yes or no ?")
            if ans == "no":
                break
        elif menu_choice == "c":
            breed_purpose()
            ans = input("Would you like to continue this program: yes or no ?")
            if ans == "no":
                break
        elif menu_choice == "d": #not an already exisitng function just code to view all 100 dog breeds
            print("Here are all the different dog breeds that we currently have in our database")
            print(dog_breeds)
            ans = input("Would you like to continue this program: yes or no ?")

            if ans == "no":
                break
        else:
            print("Invalid Input Please try again.")


#main
dog_breed_choosing()
