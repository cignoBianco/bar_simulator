# bar simulator
# by Anastasia Smirnova, cignoBianco, smiana123@gmail.com
import random

STRONG_DRINKS = ['HRENOVUHA', 'vodka', 'tekilla', 'SAMOGON']
ALCO_DRINKS = ['wine', 'cidre', 'beer', 'b52']
ZERO_DRINKS = ['coffee', 'just a water, please']

print('''Welcome to the shalopaii bar! Present yourself!\n Hey, I\'m ...''')
you = input('> ') 
you = you if you else 'Guest'

def main():
    simulate_bar_party()

def simulate_bar_party():
    print('Barmen say: Nice to meet you, {}'.format(you))

    your_alco_lvl = 0
    
    print('You came to the bar!')
    your_alco_lvl += get_drink()
    bar_people = look_around()
    # get_drink()

    people_you_know = []

    while your_alco_lvl < 100 and not len(people_you_know) == len(bar_people):
        print('It\'s time to meet with somebody...\nYou choose:')
        object_person = ''
        while not any(p['first_impression'] == object_person for p in bar_people) or any(p['first_impression'] == object_person for p in people_you_know):
            for person in bar_people:
                print('— {}'.format(person.first_impression))
            object_person = input('> ')
        
        object_person = next(person for person in bar_people if person["first_impression"] == object_person)
        meet(object_person)
        your_alco_lvl += get_drink()
        people_you_know.append(object_person)
    print('OH MY GOT! YOURE TOO DRUNK 😣')

def meet(person):
    print('He told that his name is {}.\n You say: Hi, {}! I\'m {}. Nice to meet you'.format(person.name, person.name, you))
    print('Good! \nWhat\'s next...')
    return person

def look_around():
    people = [{'name': 'John', 'first_impression': 'ordinary man'},
        {'name': 'Mary', 'first_impression': 'pretty girl'},
        {'name': 'David', 'first_impression': 'clever looking man'},
        {'name': 'Pablo', 'first_impression': 'dangerous man'},
        {'name': 'Denis', 'first_impression': 'like a child'},
        {'name': 'Sew', 'first_impression': 'very strange'},
        {'name': 'Ann', 'first_impression': 'ordinary girl'}]
    print('You looked around. Here are the people you saw:')
    for person in people:
        print('— {}'.format(person.first_impression))
    return people

def get_drink():
    your_choice = ''
    print('\nWhat do you prefer now:')
    all_drinks = ALCO_DRINKS + STRONG_DRINKS + ZERO_DRINKS
    for drink in all_drinks:
        print('- {}'.format(drink))
    while not your_choice in all_drinks and your_choice != 'random':
        your_choice = input('> ')
    if your_choice == 'random':
        your_choice = all_drinks[random.randint(0, len(DRINKS) - 1)]
    if your_choice == 'HRENOVUHA':
        print('\nYou drank your HRENOVUHA. Poor you!\n')
    else:
        print('\nNice choice! Barmen filled your glass. Here is your {}!\n'.format(your_choice))
    if your_choice in ALCO_DRINKS:
        print('🥳')
        return 25
    elif your_choice in STRONG_DRINKS:
        print('🥳🥳🥳')
        return 50
    else:
        return 0
main()
