def eliminateCommonChars(listOne, listTwo):
    for i in range(len(listOne)):
        for j in range(len(listTwo)):
            if listOne[i] == listTwo[j]:
                c = listOne[i]
                listOne.remove(c)
                listTwo.remove(c)
                listThree = listOne + ["*"] + listTwo
                return [listThree, True]
    listThree = listOne + ["*"] + listTwo
    return [listThree, False]
if __name__ == "__main__":
    print("welcome to FLAMES game...!")
    playerOne = input("enter the first name : ")
    playerOne = playerOne.lower()
    playerOne.replace(" ", "")
    playerOneList = list(playerOne)
    playerTwo = input("enter the second Name : ")
    playerTwo = playerTwo.lower()
    playerTwo.replace(" ", "")
    playerTwoList = list(playerTwo)
    proceed = True
    while proceed:
        retList = eliminateCommonChars(playerOneList, playerTwoList)
        conList = retList[0]
        proceed = retList[1]
        starIndex = conList.index("*")
        playerOneList = conList[: starIndex]
        playerTwoList = conList[starIndex + 1:]
    theCount = len(playerOneList) + len(playerTwoList)
    res = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]
    while len(res) > 1:
        splitIndex = (theCount % len(res) - 1)
        if splitIndex >= 0:
            right = res[splitIndex + 1:]
            left = res[: splitIndex]
            res = right + left
        else:
            res = res[: len(res) - 1]
    print("Relationship Status :", res[0])