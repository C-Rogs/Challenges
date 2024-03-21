
#
# Complete the 'plusMinus' function below.
# The function accepts INTEGER_ARRAY arr as parameter.
def plusMinus(arr):
    pos = neg = zer = 0.0

    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zer += 1
            
    print(format(pos/len(arr), '.6f'))
    print(format(neg/len(arr), '.6f'))
    print(format(zer/len(arr), '.6f'))

#
# Complete the 'miniMaxSum' function below.
# The function accepts INTEGER_ARRAY arr as parameter.
def miniMaxSum(arr):
    arr.sort()
    minimum = arr[0] + arr[1] + arr[2] + arr[3]
    maximum = arr[1] + arr[2] + arr[3] + arr[4]
    print(minimum, maximum)

#
# Complete the 'timeConversion' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
def timeConversion(s):
    hours = int(s[0:2])
    period = s[8:10]
    middle = s[2:8]
    
    if hours == 12 and period == "AM":
        hours = "00"
    elif hours == 12 and period == "PM":
        hours = "12"
    elif period == "PM":
        hours = str(hours + 12)
    else:
        hours = str(hours).zfill(2)
    
    return(f"{hours}{middle}")


if __name__ == '__main__':
    #n = int(input().strip())
    #arr = list(map(int, input().rstrip().split()))
    arr = [1,5,0,0,-3]
    plusMinus(arr)
    miniMaxSum(arr)
    print(timeConversion("12:56:23PM"))