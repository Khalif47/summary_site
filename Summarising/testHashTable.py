from Summarising.HashTable import HashTable


def testHash():
    test = HashTable()
    test['me'] = 'hi'
    test['sh'] = 'me'
    assert test['me'] == 'hi', 'wrong entry'
    assert test['sh'] == 'me', 'wrong entry'


if __name__ == '__main__':
    testHash()
    print('Hash table passed all test cases')
