# Complete the 'caesarCipher' function below.
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k

def caesarCipher(s, k):
    k %= 26
    cipher_text = ""
    for c in range(len(s)):
        ascii_char = ord(s[c])
        if ascii_char in range(65, 91) or ascii_char in range(97, 123):
            if (ascii_char in range(65, 91) and ascii_char + k > 90) or (ascii_char in range(97, 123) and ascii_char + k > 122):
                cipher_char = chr(ascii_char + k - 26)
            else:
                cipher_char = chr(ascii_char + k)
        else:
            cipher_char = s[c]
        cipher_text += cipher_char
    return cipher_text

# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    if m == 1:
        return 2
    elif n % 2 == 0:
        return 2
    else:
        return 1

#Zig Zag Sequence
def findZigZagSequence(a, n):
    a.sort()
    mid = int((n - 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return