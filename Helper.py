import EditDistance



def readFile(_FileName: str):
    resultArray = []
    with open(_FileName, "r") as inputFile:
        for lineEntity in inputFile:
            lineWithoutEnter = lineEntity.replace("\n", "")
            resultArray.append(lineWithoutEnter)
        inputFile.close()
    return resultArray


def cutArrayInBlocks(_ArrayOfWords: [str], _NumberOfBlocks):
    resultList = []
    blockLength = len(_ArrayOfWords) // _NumberOfBlocks
    for b in range(1, _NumberOfBlocks + 1):
        startPos = (b - 1) * blockLength
        endPos = b*blockLength if (b < _NumberOfBlocks) else b*blockLength + len(_ArrayOfWords) % _NumberOfBlocks
        resultList.append(_ArrayOfWords[startPos: endPos])
    return resultList



def createMatrixWithEditDistances(_ArrayOfWords: [str]):
    resultMatrix = [[0 for x in _ArrayOfWords] for y in _ArrayOfWords]

    for i in range(0, len(_ArrayOfWords)):
        for j in range(i + 1, len(_ArrayOfWords)):
            resultMatrix[i][j] = EditDistance.levenstein(_ArrayOfWords[i], _ArrayOfWords[j])
    return resultMatrix



def analyseMatrixAndCreateOutput(_MatrixWithEditDistances: [[int]], _ArrayOfRestaurantNames: [str], _OutputFile: str,
                                 _ThresholdValue: int, rewrite: bool):
    if(rewrite):
        with open(_OutputFile, "w+") as outputFile:
            for i in range(0, len(_MatrixWithEditDistances)):
                for j in range(i + 1, len(_MatrixWithEditDistances)):
                    if(_MatrixWithEditDistances[i][j] <= _ThresholdValue):
                        outputLine = "{word1} --- {word2} --- {value} \n".format(word1 = str(_ArrayOfRestaurantNames[i]),
                                                                              word2 = str(_ArrayOfRestaurantNames[j]),
                                                                              value = _MatrixWithEditDistances[i][j])
                        outputFile.write(outputLine)
            outputFile.close()
    else:
        with open(_OutputFile, "a") as outputFile:
            for i in range(0, len(_MatrixWithEditDistances)):
                for j in range(i + 1, len(_MatrixWithEditDistances)):
                    if(_MatrixWithEditDistances[i][j] <= _ThresholdValue):
                        outputLine = "{word1} --- {word2} --- {value} \n".format(word1 = str(_ArrayOfRestaurantNames[i]),
                                                                              word2 = str(_ArrayOfRestaurantNames[j]),
                                                                              value = _MatrixWithEditDistances[i][j])
                        outputFile.write(outputLine)
            outputFile.close()


def analyseMatrix(_MatrixWithEditDistances, _ArrayOfRestaurantNames, _ThresholdValue):
    resultList = []
    for i in range(0, len(_MatrixWithEditDistances)):
        for j in range(i + 1, len(_MatrixWithEditDistances)):
            if (_MatrixWithEditDistances[i][j] <= _ThresholdValue):
                resultList.append({
                    'word1': _ArrayOfRestaurantNames[i],
                    'word2': _ArrayOfRestaurantNames[j],
                    'value': _MatrixWithEditDistances[i][j]
                })
    return resultList


#for Exercise 4
def readFileAndRefactorInput(_FileName: str):
    resultArray = []
    with open(_FileName, "r") as inputFile:
        for lineEntity in inputFile:
            refactoredLine = refactorLine(lineEntity)
            resultArray.append(refactoredLine)
        inputFile.close()
    return resultArray


# deletes double spaces
# deletes before extra signs like ' or , or .
def refactorLine(_Word: str):
    _Word = _Word.replace("  ", " ")
    _Word = _Word.replace("\n", "")
    _Word = _Word.replace("\t", "")

    _Word = _Word.replace(" \'", '\'')
    _Word = _Word.replace(" ,", ',')
    _Word = _Word.replace(" .", '.')
    _Word = _Word.replace(" -", "-")
    _Word = _Word.replace("- ", "-")
    if(_Word.startswith(" ")):
        _Word = _Word[1:]

    return _Word


def cleanFile(_PathToFile: str):
    with open(_PathToFile, "w+") as outputFile:
        outputFile.write("")
        outputFile.close()


