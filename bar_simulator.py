# bar simulator
# by Anastasia Smirnova, cignoBianco, smiana123@gmail.com
import random
YOUR_NAME = 'Eugene'

STRONG_DRINKS = ['HRENOVUHA', 'vodka', 'tekilla', 'SAMOGON']
ALCO_DRINKS = ['wine', 'cidre', 'beer']
ZERO_DRINKS = ['coffee', 'just a water, please']

def main():
    simulate_bar_party()

def simulate_bar_party():
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
    print('He told that his name is {}. You say: Hi, {}! I\'m {}. Nice to meet you'.format(person, person, YOUR_NAME))
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
