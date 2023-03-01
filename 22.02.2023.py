
def shapes():
    print('=======')
    print(' -x+x-')
    print('=======')
    
name = input('What is your name?: ')
shapes()
age = input('How old are you?: ')
shapes()
drink = input('What is yout favorite drink?: ')
shapes()
print(f'Hello {name}! You are {age} y.o.\nYour favorite drink is {drink}.')


def printModelis():
    print('=======')
    print(' -x+x-')
    print('=======')

name = input('What is your name?: ')
printModelis()
age = input('How old are you?: ')
printModelis()
drink = input('What is yout favorite drink?: ')
printModelis()
print(f'Hello {name}! You are {age} y.o.\nYour favorite drink is {drink}.')


def SumTwoNumbers(x, y):
  print(x+y)
SumTwoNumbers(5,6)


def SumTwoNumbers(x, y):
  return x+y
n1=int(input('Choose number one: '))
n2=int(input('Choose number two: '))
result = SumTwoNumbers(n1,n2)
print(result)



print("Mans")
#@Elchin
#Šis ir interesants veids kā varēja uzdot tos jautājumus + šim vienklāršāk varētu puielikt daudz vairāk jautājumus
def nice_shapes():
    print('=======')
    print(' -x+x-')
    print('=======')
    
i=0
while i < 3:
    saraksts = ['name','age','drink']
    ask = ['What is your name?:','How old are you?:','How old are you?:']
    saraksts[i] = input(ask[i])
    nice_shapes()
    i=i+1
print(saraksts)
print(f'Hello {name}! You are {age} y.o.\nYour favorite drink is {drink}.')


cont =[]
name = input('Enter name: ')
surname = input('Enter surname: ')
age = input('Enter number: ')
email = input('Enter email: ')

contacts = [name, surname, age, email]
cont.append(contacts)




#bišku atšķirīgi
contacts = []
a=input("Want to continue:")
while a=="Yes" or a=="yes":
    name = input('Enter name: ')
    surname = input('Enter surname: ')
    number = input('Enter number: ')
    email = input('Enter email: ')

    contact = {
        'name': name, 
        'surname': surname, 
        'number': number,
        'email': email
        }
    contacts.append(contact)
    a=input("Want to continue:")
print(contacts)




import json
dictionary = {'contacts': []}
while True:
    response = input('(1)add contact (2)print contacts (3)exit: ')
    if response == '1':
        person_name = input('Name: ')
        person_surname = input('Surname: ')
        person_phone = input('Phone: ')
        person_email = input('Email: ')

        person_contact = {
            'name': person_name,
            'surname': person_surname,
            'phone': person_phone,
            'email': person_email
        }
        dictionary['contacts'].append(person_contact)

    elif response == '2':
        for contact in dictionary['contacts']:
            print("---CONTACT---")
            print(f"{contact['name']} {contact['surname']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")        
        
    elif response == '3':
        print('Saving data....')
        with open('contacts.json', 'w', encoding='utf-8') as file:
            json.dump(dictionary, file, indent=4)
        print('Data saved.')
        print('Bye')
        exit()
    else:
        print('Please respond with 1, 2 or 3')



def print_contacts():
    for contact in contacts:
            print(f"{contact['name']} {contact['surname']} {contact['number']} {contact['email']}")

contacts = []
while(True):
    response = input('N-add new, P-print, E-exit: ')
    if response == 'N':
        name = input('Enter name: ')
        surname = input('Enter surname: ')
        number = input('Enter number: ')
        email = input('Enter email: ')

        contact = {
            'name': name, 
            'surname': surname, 
            'number': number,
            'email': email
        }

        contacts.append(contact)
        print(contacts)
    elif response == 'P':
        print_contacts()
    elif response == 'E':
        break




    






