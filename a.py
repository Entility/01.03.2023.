import random

names = []
surnames =[]

#Aaron, Hank';
#Abagnale, Frank;
# Abbey, Edward;
# Abel, Reuben;
# Abelson, Hal;
# Abourezk, James;
# Abrams, Creighton;
# Ace, Jane;
# Acton, John (Lord Acton);
# Adams, Abigail


#@Elchin
#Nevar arī kaut kā šādi?, tikai jāpievieno vēl vārdu sarakst.
file = open("uzd.csv", "w")
file.write("name, surname, email\n")

for i in range(1, 11):
    name = names[random.randint(0, 10)]
    surname = surnames[random.randint(0, 10)]
    email = name+"@gmail.com"
    cilvēks=[name, surname, email]
    file.write(F"cilvēks\n")
file.close()

#uzd
file = open("list.csv", "w")
file.write("name, surname, email\n")

for i in range(1, 11):
    file.write(f"Name{i}, Surname{i}, Email{i}\n")


file = open("list.csv", "w")
file.write("name, surname, email\n")

amount=input("How many preson contacts yopu need?":)
for i in range(1, (amount+1)):
    file.write(f"Name{i}, Surname{i}, Email{i}\n")



