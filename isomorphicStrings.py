def test_isomorph():
    assert isomorph('egg', 'add') == True, 'Test Case 1 Failed'
    assert isomorph('foo', 'bar') == False, 'Test Case 2 Failed'
    assert isomorph('paper', 'title') == True, 'Test Case 3 Failed'
    assert isomorph('aba', 'baa') == False, 'Test Case 4 Failed'
    assert isomorph('abc', 'def') == True, 'Test Case 5 Failed'
    assert isomorph('', '') == True, 'Test Case 6 Failed'
    assert isomorph('a', 'a') == True, 'Test Case 7 Failed'
    assert isomorph('badc', 'baba') == False, 'Test Case 8 Failed'
    print('All test cases pass')
    
def isomorph(s, t):
    #Check the length of the set of the strings as the number of different chars should be the same.
    if len(set(s)) != len(set(t)):
        return False
    mapped = {}
    for i in range(len(t)):
        if t[i] not in mapped:
            mapped[t[i]] = s[i]
        elif mapped[t[i]] != s[i]:
            return False
    return True

if __name__ == '__main__':
    test_isomorph()