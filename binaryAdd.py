def addBinary(a: str, b: str):
    s = bin(int(a,2)+int(b,2))
    return s[2::]

def test_addBinary():
    assert addBinary('0', '0') == '0'
    assert addBinary('1', '1') == '10'
    assert addBinary('1010', '1011') == '10101'
    assert addBinary('1111', '1111') == '11110'
    assert addBinary('1101', '101') == '10010'
    print("Test cases pass.")

test_addBinary()