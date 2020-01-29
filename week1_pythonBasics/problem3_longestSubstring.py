def longest_substring(string: str) -> str:
    substring = {
        'current': '',
        'longest': ''
    }
    counter = 0
    while counter <= len(string) - len(substring['longest']):
        i = counter
        substring['current'] = string[counter]
        for i in range(counter + 1, len(string)):
            if string[i] >= substring['current'][-1]:
                substring['current'] += string[i]
            if i == len(string) - 1 or string[i] < substring['current'][-1]:
                if len(substring['current']) > len(substring['longest']):
                    substring['longest'] = substring['current']
                break
        counter += 1
    return substring['longest']


s = 'abcdefghijklmnopqrstuvwxyz'  # insert a string, remove before submission
print('Longest substring in alphabetical order is: ' + str(longest_substring(s)))
