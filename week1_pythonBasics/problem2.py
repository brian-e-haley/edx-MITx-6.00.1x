import re


def find_bob(string: str) -> int:
    count = len(re.findall('(?=bob)', s))
    return count


s = 'azcbobobegghakl'  # insert a string, remove before submission
print('Number of times bob occurs is: ' + str(find_bob(s)))
