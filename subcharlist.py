ls = ['e', 'f', 'a', 'g',4, 'h', 3, 'u', 'z', 6, 8, 'v']
def indentifySublist(digitCharList):
    startIndex = endIndexIn = 0
    count_int = count_char = 0
    legnagyobb = 0
    for i in range(len(digitCharList)):
        if digitCharList[i] != digitCharList[i - 1]:
            count_int = count_char = 0
        for j in range(len(digitCharList) + 1):

            if digitCharList[i:j] == []:
                continue

            if type(digitCharList[j -1]) == int:
                count_int += 1
            else:
                count_char += 1

            if count_int == count_char:
                if len(digitCharList[i:j]) > legnagyobb:
                    legnagyobb = len(digitCharList[i:j])
                    startIndex = i
                    endIndexIn = j - 1

    return (startIndex, endIndexIn)
print(indentifySublist(ls))