# bar simulator
# by Anastasia Smirnova, cignoBianco, smiana123@gmail.com
# and Anna Izgarova, ann-izgarova, izgarovaa@mail.ru
import random
import pandas as pd

STRONG_DRINKS = ['HRENOVUHA', 'vodka', 'tekilla', 'SAMOGON']
ALCO_DRINKS = ['wine', 'cidre', 'beer']
ZERO_DRINKS = ['coffee', 'just a water, please']
COCKTAILS =  pd.DataFrame([{'name': 'b52', 'alco': 35, 'message': 'The bartender set your cocktail on fire mmm (and accidentally set your sleeve on fire, oops)'},
              {'name': 'Aperol Spritz', 'alco': 23, 'message': "Wow, you got a nice fiery orange drink, It's getting hot💦💦"},
              {'name': 'Bloody Mary', 'alco': 25, 'message': 'Barmen bring thick red cocktail and winked ;)'}, 
              {'name': 'The Blue Lagoon', 'alco': 10, 'message': 'After the drink are ready to dance! MY LIFE MY RULES!!!'},
              {'name': 'Tequila Sunrise','alco': 18, 'message': 'Incredible 👏' }])

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
        while not object_person in bar_people.keys() or any(p['appearance'] == object_person for p in people_you_know):
            for person in bar_people.keys():
                print('— {}'.format(person))
            object_person = input('> ')
        
        object_person = {'appearance': object_person, 'name': bar_people[object_person]}
        meet(object_person['name'])
        your_alco_lvl += get_drink()
        people_you_know.append(object_person)
    print('OH MY GOT! YOURE TOO DRUNK 😣')

def meet(person):
    print('He told that his name is {}. You say: Hi, {}! I\'m {}. Nice to meet you'.format(person, person, you))
    print('Good! \nWhat\'s next...')
    return person

def look_around():
    people = {'ordinary man': 'John', 'pretty girl': 'Mary', 'clever looking man': 'David', 'dangerous man': 'Pablo',
              'like a child': 'Denis', 'very strange': 'Sew', 'ordinary girl': 'Ann'}
    print('You looked around. Here are the people you saw:')
    for person in people.keys():
        print('— {}'.format(person))
    return people

def get_drink():
    your_choice = ''
    print('\nWhat do you prefer now:')
    all_drinks = ALCO_DRINKS + STRONG_DRINKS + ZERO_DRINKS + list(COCKTAILS['name'])
    for drink in all_drinks:
        print('- {}'.format(drink))
    while not your_choice in all_drinks and your_choice != 'random':
        your_choice = input('> ')
    if your_choice == 'random':
        your_choice = all_drinks[random.randint(0, len(DRINKS) - 1)]
    if your_choice == 'HRENOVUHA':
        print('\nYou drank your HRENOVUHA. Poor you!\n')
    elif your_choice in list(COCKTAILS['name']):
        print('\n' + COCKTAILS[COCKTAILS.name == your_choice]['message'].values[0] + '\n')
    else:
        print('\nNice choice! Barmen filled your glass. Here is your {}!\n'.format(your_choice))
    if your_choice in ALCO_DRINKS:
        print('🥳')
        return 25
    elif your_choice in STRONG_DRINKS:
        print('🥳🥳🥳')
        return 50
    elif your_choice in list(COCKTAILS['name']):
        print('🥳🥳🥳🥳🥳🥳')
        return int(COCKTAILS[COCKTAILS.name == your_choice]['alco'])
    else:
        return 0
main()
