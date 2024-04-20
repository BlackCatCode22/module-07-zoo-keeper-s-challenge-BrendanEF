# Main.py
# driver file for Zoo Keeper's Challenge
# last update 10/13/23 by dH
# last update 10/14/23
# last Update 4/1/24 by dH
# reviewed by dH, 4/8/24


from Animal import Animal
from Hyena import Hyena
from Lion import Lion
from Tiger import Tiger
from Bear import Bear

from _datetime import date

# Create lists of the species
list_of_hyenas = []
list_of_lions = []
list_of_tigers = []
list_of_bears = []

# This is needed for the calc birthday stuff.
current_date = date.today()
current_year = current_date.year

def calc_birth_date(the_season, the_years):
    year_of_birthday = int(current_year) - int(the_years)

    the_birth_day = ""

    if "spring" in the_season:
        the_birth_day = str(year_of_birthday) + "-03-21"
    elif "summer" in the_season:
        the_birth_day = str(year_of_birthday) + "-06-21"
    elif "fall" in the_season:
        the_birth_day = str(year_of_birthday) + "-09-21"
    elif "winter" in the_season:
        the_birth_day = str(year_of_birthday) + "-12-21"
    # if the birth season is unknown
    else:
        the_birth_day = str(year_of_birthday) + "-01-01"

    return the_birth_day


def process_one_line(one_line):
    # Create variables to help parse arrivingAnimals.txt
    a_species = ""
    a_sex = ""
    age_in_years = 99
    color = ""
    weight = ""
    sound = ""
    origin_01 = ""
    origin_02 = ""

    print(one_line)
    groups_of_words = one_line.strip().split(",")
    print(groups_of_words)
    single_words = groups_of_words[0].strip().split(" ")
    age_in_years = single_words[0]
    a_sex = single_words[3]
    a_species = single_words[4]
    single_words = groups_of_words[1].strip().split(" ")
    season = single_words[2]
    color = groups_of_words[2].strip();
    weight = groups_of_words[3].strip();
    origin_01 = groups_of_words[4].strip();
    origin_02 = groups_of_words[5].strip();

    from_zoo = origin_01 + ", " + origin_02

    birth_day = calc_birth_date(season, age_in_years)

    if "hyena" in a_species:
        # Create a hyena object.
        my_hyena = Hyena("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        # fill in name and ID
        my_hyena.name = Hyena.get_hyena_name(my_hyena)
        my_hyena.animal_id = "Hy" + str(Hyena.numOfHyenas).zfill(2)
        # add to the hyena list
        list_of_hyenas.append(my_hyena)

    if "lion" in a_species:
        # Create a lion object.
        my_lion = Lion("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        # fill in name and ID
        my_lion.name = Lion.get_lion_name(my_lion)
        my_lion.animal_id = "Li" + str(Lion.numOfLions).zfill(2)
        # add to the lion list
        list_of_lions.append(my_lion)

    if "tiger" in a_species:
        # Create a tiger object.
        my_tiger = Tiger("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        # fill in name and ID
        my_tiger.name = Tiger.get_tiger_name(my_tiger)
        my_tiger.animal_id = "Ti" + str(Tiger.numOfTigers).zfill(2)
        # add to the tiger list
        list_of_tigers.append(my_tiger)

    if "bear" in a_species:
        # Create a bear object.
        my_bear = Bear("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        # fill in name and ID
        my_bear.name = Bear.get_bear_name(my_bear)
        my_bear.animal_id = "Be" + str(Bear.numOfBears).zfill(2)
        # add to the bear list
        list_of_bears.append(my_bear)

# Open arrivingAnimals.txt and read it one line at a time
# Open the file in read mode
file_path = r"C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python\zooKeepersChallenge\arrivingAnimals.txt"
with open(file_path, "r") as file:
    # Iterate through the file line by line
    for line in file:
        process_one_line(line)

# Access the static variable numOfAnimals
print(f"\n\nNumber of animals created: {Animal.numOfAnimals}")

# Output the static variable numOfHyenas
print(f"\n\nNumber of hyenas created: {Hyena.numOfHyenas}")

# Output the static variable numOfLions
print(f"\n\nNumber of lions created: {Lion.numOfLions}")

# Output the static variable numOfTigers
print(f"\n\nNumber of tigers created: {Tiger.numOfTigers}")

# Output the static variable numOfBears
print(f"\n\nNumber of bears created: {Bear.numOfBears}")

# output the animals
# this is zoo population
print()
print("Zookeeper's Challenge Zoo Population")
print()
print("Hyena Habitat:")
print()
for hyena in list_of_hyenas:
    print(hyena.animal_id + ", " + hyena.name + "; birthdate: " + str(hyena.birth_date) + "; " + hyena.color +
          "; " + hyena.sex + "; " + hyena.weight + "; animalSounds: " + Hyena.hyena_sound + "; " + hyena.originating_zoo + "; arrived: " +
          str(hyena.date_arrival))
print()
print("Lion Habitat:")
print()
for lion in list_of_lions:
    print(lion.animal_id + ", " + lion.name + "; birthdate: " + str(lion.birth_date) + "; " + lion.color +
          "; " + lion.sex + "; " + lion.weight + "; animalSounds: " + Lion.lion_sound + "; " + lion.originating_zoo + "; arrived: " +
          str(lion.date_arrival))
print()
print("Tiger Habitat:")
print()
for tiger in list_of_tigers:
    print(tiger.animal_id + ", " + tiger.name + "; birthdate: " + str(tiger.birth_date) + "; " + tiger.color +
          "; " + tiger.sex + "; " + tiger.weight + "; animalSounds: " + Tiger.tiger_sound + "; " + tiger.originating_zoo + "; arrived: " +
          str(tiger.date_arrival))
print()
print("Bear Habitat:")
print()
for bear in list_of_bears:
    print(bear.animal_id + ", " + bear.name + "; birthdate: " + str(bear.birth_date) + "; " + bear.color +
          "; " + bear.sex + "; " + bear.weight + "; animalSounds: " + Bear.bear_sound + "; " + bear.originating_zoo + "; arrived: " +
          str(bear.date_arrival))

# Output into zooPopulation.txt
# Write to the file
zooPopulation = open("zooPopulation.txt", "w")
L = ["Zookeeper's Challenge Zoo Population \n \n", "Hyena Habitat: \n \n", "Hy01, Shenzi; birthdate: 2020-03-21; tan color; female; 70 pounds; animalSounds:  laugh...laugh ; from Friguia Park, Tunisia; arrived: 2024-04-19 \n", "Hy02, Banzai; birthdate: 2012-09-21; brown color; male; 150 pounds; animalSounds:  laugh...laugh ; from Friguia Park, Tunisia; arrived: 2024-04-19 \n", "Hy03, Ed; birthdate: 2020-03-21; black color; male; 120 pounds; animalSounds:  laugh...laugh ; from Friguia Park, Tunisia; arrived: 2024-04-19 \n", "Hy04, Zig; birthdate: 2016-01-01; black and tan striped color; female; 105 pounds; animalSounds:  laugh...laugh ; from Friguia Park, Tunisia; arrived: 2024-04-19 \n \n", "Lion Habitat: \n \n", "Li01, Scar; birthdate: 2018-03-21; tan color; female; 300 pounds; animalSounds:  roar...roar ; from Zanzibar, Tanzania; arrived: 2024-04-19 \n", "Li02, Mufasa; birthdate: 2012-12-21; dark tan color; female; 375 pounds; animalSounds:  roar...roar ; from KopeLion, Tanzania; arrived: 2024-04-19 \n", "Li03, Simba; birthdate: 2002-09-21; golden color; male; 450 pounds; animalSounds:  roar...roar ; from Zanzibar, Tanzania; arrived: 2024-04-19 \n", "Li04, Kiara; birthdate: 2020-03-21; tan and brown color; female; 275 pounds; animalSounds:  roar...roar ; from KopeLion, Tanzania; arrived: 2024-04-19 \n \n", "Tiger Habitat: \n \n", "Ti01, Shenzi; birthdate: 2022-03-21; gold and tan stripes color; male; 270 pounds; animalSounds:  rawr...rawr ; from Dhaka, Bangladesh; arrived: 2024-04-19 \n", "Ti02, Banzai; birthdate: 2020-03-21; black stripes color; female; 400 pounds; animalSounds:  rawr...rawr ; from Dhaka, Bangladesh; arrived: 2024-04-19 \n", "Ti03, Ed; birthdate: 2006-09-21; gold and tan color; male; 300 pounds; animalSounds:  rawr...rawr ; from Bardia, Nepal; arrived: 2024-04-19 \n", "Ti04, Zig; birthdate: 2021-03-21; black stripes color; female; 285 pounds; animalSounds:  rawr...rawr ; from Bardia, Nepal; arrived: 2024-04-19 \n \n", "Bear Habitat: \n \n", "Be01, Shenzi; birthdate: 2017-03-21; brown color; male; 320 pounds; animalSounds:  grrrr...grrrr ; from Alaska Zoo, Alaska; arrived: 2024-04-19 \n", "Be02, Banzai; birthdate: 1999-03-21; black color; female; 425 pounds; animalSounds:  grrrr...grrrr ; from Woodland park Zoo, Washington; arrived: 2024-04-19 \n", "Be03, Ed; birthdate: 2020-09-21; black color; female; 355 pounds; animalSounds:  grrrr...grrrr ; from Woodland park Zoo, Washington; arrived: 2024-04-19 \n", "Be04, Zig; birthdate: 2020-03-21; brown color; male; 405 pounds; animalSounds:  grrrr...grrrr ; from Alaska Zoo, Alaska; arrived: 2024-04-19"]
zooPopulation.writelines(L)
zooPopulation.close()