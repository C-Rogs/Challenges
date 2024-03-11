def canConstruct(ransomNote, magazine):
    counter = {}
    for m in magazine: 
        if m in counter:
            counter[m] += 1
        else:
            counter[m] = 1
    
    for r in ransomNote: 
        if r in counter and counter[r] > 0:
            counter[r] -= 1
        else:
            return False
    return True

print(canConstruct("aabc","caamerob"))