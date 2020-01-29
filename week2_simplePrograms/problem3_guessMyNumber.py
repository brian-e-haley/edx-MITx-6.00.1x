bounds = {
    'low': 0,
    'high': 100
}
guess = {
    'low': bounds['low'],
    'high': bounds['high'],
    'middle': int((bounds['high'] + bounds['low']) / 2)
}
response = 'h'
print('Please think of a number between ' + str(bounds['low']) + ' and ' +
      str(bounds['high']) + '!')

while response != 'c':
    print('Is your secret number ' + str(guess['middle']) + '?')
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' "
                     "to indicate the guess is too low. Enter 'c' to indicate "
                     "I guessed correctly.")
    if response == 'h':
        guess['high'] = guess['middle']
        guess['middle'] = int((guess['high'] + guess['low']) / 2)
    elif response == 'l':
        guess['low'] = guess['middle']
        guess['middle'] = int((guess['high'] + guess['low']) / 2)
    elif response == 'c':
        print('Game over. Your secret number was: ' + str(guess['middle']))
    else:
        print('Sorry, I did not understand your input.')
