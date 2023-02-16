# bar simulator
# by Anastasia Smirnova, cignoBianco, smiana123@gmail.com
# and Anna Izgarova, ann-izgarova, izgarovaa@mail.ru
import random

DRINKS = {
    'strong': [
        {'name': 'SAMOGON', 'alco_lvl': 50, 'message': 'SOS 🚁🚁🚁 SOS Helicopters attcack!!!'},
        {'name': 'tekilla', 'alco_lvl': 38, 'message': 'El tiempo vuela cuando te diviertes 🌮 Wanna some tacos?'},
        {'name': 'vodka', 'alco_lvl': 40, 'message': 'Very strong choice. For a very strong person.'},
        {'name': 'HRENOVUHA', 'alco_lvl': 60, 'message': 'You drank your HRENOVUHA. Poor you!'},
    ],
    'alco': [
        {'name': 'wine', 'alco_lvl': 12, 'message': 'Is it true that if you mix white wine and red wine, you get the rose one? 🤔🧐 '},
        {'name': 'cidre', 'alco_lvl': 5, 'message': 'Nice choice! Barmen filled your glass. Here is your apple cidre!'},
        {'name': 'beer', 'alco_lvl': 7, 'message': '🍺 beer foam drew a mustache on you 🍻'},
    ],
    'cocktails': [
        {'name': 'b52', 'alco_lvl': 35, 'message': 'The bartender set your cocktail on fire mmm (and accidentally set your sleeve on fire, oops)'},
        {'name': 'Aperol Spritz', 'alco_lvl': 23, 'message': 'Wow, you got a nice fiery orange drink, It\'s getting hot💦💦'},
        {'name': 'Bloody Mary', 'alco_lvl': 25, 'message': 'Barmen bring thick red cocktail and winked'},
        {'name': 'The Blue Lagoon', 'alco_lvl': 10, 'message': 'After the drink are ready to dance! MY LIFE MY RULES!!!'},
        {'name': 'Tequila Sunrise', 'alco_lvl': 18, 'message': 'Incredible 👏'},
    ],
    'zero': [
        {'name': 'just a water, please', 'alco_lvl': 0, 'message': 'Bartender filled your glass of water 💧'},
        {'name': 'coffee', 'alco_lvl': 0, 'message': 'Okaaay... Here is your capuccino ☕️'},
    ]
}

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
        print('\nIt\'s time to meet with somebody...\nYou choose:')
        object_person = ''
        while not any(p['first_impression'] == object_person for p in bar_people) or any(p['first_impression'] == object_person for p in people_you_know):
            for person in bar_people:
                print('— {}'.format(person['first_impression']))
            object_person = input('\n> ')
        
        object_person = next(person for person in bar_people if person["first_impression"] == object_person)
        meet(object_person)
        your_alco_lvl += get_drink()
        people_you_know.append(object_person)

        if len(people_you_know) == 2 and not any(p['is_spy'] for p in people_you_know):
            print('Oooops! Spy has stolen your pocket.......')

    print('OH MY GOT! YOURE TOO DRUNK 😣')
    spy = next(person for person in bar_people if person["is_spy"])
    print('The spy was {} {}'.format(spy['first_impression'], spy['name']))

def meet(person):
    print('He told that his name is {}.\n You say: Hi, {}! I\'m {}. Nice to meet you'.format(person['name'], person['name'], you))
    if person['is_spy']:
        print('YOU FOUND THE SPY!!!')
    else:
        print('Good! \nWhat\'s next...')
    return person

def look_around():
    people = [{'name': 'John', 'first_impression': 'ordinary man', 'is_spy': False},
        {'name': 'Mary', 'first_impression': 'pretty girl', 'is_spy': False},
        {'name': 'David', 'first_impression': 'clever looking man', 'is_spy': False},
        {'name': 'Pablo', 'first_impression': 'dangerous man', 'is_spy': False},
        {'name': 'Denis', 'first_impression': 'like a child', 'is_spy': False},
        {'name': 'Sew', 'first_impression': 'very strange', 'is_spy': False},
        {'name': 'Ann', 'first_impression': 'ordinary girl', 'is_spy': False}]
    people[random.randint(0, len(people) - 1)]['is_spy'] = True

    print('You looked around. Here are the people you saw:')
    for person in people:
        print('— {}'.format(person['first_impression']))
    return people

def get_drink():
    print('\nWhat do you prefer now:')
    all_drinks = [item for sublist in DRINKS.values() for item in sublist]
    for drink in all_drinks:
        print('- {}'.format(drink['name']))
    
    your_choice = ''
    while not any(drink['name'] == your_choice for drink in all_drinks) and your_choice != 'random':
        your_choice = input('> ')
    if your_choice == 'random':
        your_choice = all_drinks[random.randint(0, len(DRINKS) - 1)]
    else: 
        your_choice = next(drink for drink in all_drinks if drink['name'] == your_choice)
    
    print('\n' + your_choice['message'] + '\n')
    return your_choice['alco_lvl']

main()
