import Helper
import phonetics

def execute(_FilePath):

    print("--- Execute exercise 4 ---")

    Helper.cleanFile("outputExercise4.txt")

    listOfRestaurantNames = Helper.readFile(_FilePath)
    print("listOfRestaurantNames: ", listOfRestaurantNames)

    listOfNamesWithSoundexCodes = createCodesForStrings(listOfRestaurantNames)
    print("listOfNamesWithSoundexCodes: ", listOfNamesWithSoundexCodes)

    resultList = []


    blocksBySoundexCodes = createBlocksBySoundexCodes(listOfNamesWithSoundexCodes)
    for key in blocksBySoundexCodes:
        if(len(blocksBySoundexCodes[key]) > 1):
            print(key, "\t", blocksBySoundexCodes[key])

    for key in blocksBySoundexCodes:
        if(len(blocksBySoundexCodes[key]) > 1):
            matrixWithEditDistances = Helper.createMatrixWithEditDistances(blocksBySoundexCodes[key])
            resultList = resultList + Helper.analyseMatrix(matrixWithEditDistances, blocksBySoundexCodes[key], 1)


    blocksByFirstCharacter = createBlocksByFirstCharacter(listOfRestaurantNames)
    print("blocksByFirstCharacter: ", blocksByFirstCharacter)

    sortedBlocksByStringLength = sortBlocksByStringLength(blocksByFirstCharacter)
    print("sortedBlocksByStringLength: ", sortedBlocksByStringLength)
    counter = 0
    for key in sortedBlocksByStringLength:
        if(len(sortedBlocksByStringLength[key]) > 0):
            minLength = len(sortedBlocksByStringLength[key][0])
            maxLength = len(sortedBlocksByStringLength[key][-1])

            windowLength = 1 # it is threshold value from exercise 2
            for i in range(minLength, maxLength-windowLength+1):
                counter += 1
                words = getWordsWithLength(sortedBlocksByStringLength[key], i, windowLength)

                matrixWithEditDistances = Helper.createMatrixWithEditDistances(words)
                tmpList = Helper.analyseMatrix(matrixWithEditDistances, words, 1)

                for elementDict in tmpList:
                    reverseElement = {
                        'word1': elementDict['word2'],
                        'word2': elementDict['word1'],
                        'value': elementDict['value']
                    }
                    if(elementDict not in resultList and reverseElement not in resultList):
                        resultList.append(elementDict)
    print("counter: ", str(counter))

    with open("outputExercise4.txt", "w") as fileOutput:
        for elementDict in resultList:
            outputLine = "{word1} --- {word2} --- {value} \n".format(word1=elementDict['word1'],
                                                                     word2=elementDict['word2'],
                                                                     value=elementDict['value'])
            fileOutput.write(outputLine)
        fileOutput.close()


def getWordsWithLength(listOfWords: [str], lengthOfWord: int, windowLength: int):
    resultList = []
    for word in listOfWords:
        if(len(word)>= lengthOfWord and len(word) <= lengthOfWord + windowLength):
            resultList.append(word)
    return resultList



def createCodesForStrings(listOfString):
    resultList = []
    for string in listOfString:
        resultList.append({
            'code': phonetics.metaphone(string)[1:],
            'string': string
        })
    return resultList


def createBlocksBySoundexCodes(listWithSoundexAndString):
    resultDict = {}
    for soundexAndString in listWithSoundexAndString:
        if(soundexAndString['code'] not in resultDict):
            resultDict[soundexAndString['code']] = [soundexAndString['string']]
        else:
            resultDict[soundexAndString['code']] = resultDict[soundexAndString['code']] + [soundexAndString['string']]
    return resultDict



def createBlocksByFirstCharacter(listOfStrings):
    resultDict = {}
    for string in listOfStrings:
        if(len(string) > 0):
            if (string[0] not in resultDict):
                resultDict[string[0]] = [string]
            else:
                resultDict[string[0]] = resultDict[string[0]] + [string]
    return resultDict


def sortBlocksByStringLength(dictOfLists):
    for key in dictOfLists:
        tmpList = dictOfLists[key]
        dictOfLists[key] = sorted(tmpList, key = len)
    return dictOfLists



