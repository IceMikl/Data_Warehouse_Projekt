import Helper


def execute(_FilePath, _NumberOfBlocks):
    print("--- Execute exercise 3 ---")

    arrayOfRestaurantNames = Helper.readFile(_FilePath)
    print("arrayOfRestaurantNames: ", arrayOfRestaurantNames)

    print("number of blocks: ", str(_NumberOfBlocks))
    listOfArrayBlocks = Helper.cutArrayInBlocks(arrayOfRestaurantNames, _NumberOfBlocks)


    for i, block in enumerate(listOfArrayBlocks):
        matrixWithDistances = Helper.createMatrixWithEditDistances(block)
        Helper.analyseMatrixAndCreateOutput(matrixWithDistances, block, "outputBlock{i}.txt".format(i = i+1), 1, True)
