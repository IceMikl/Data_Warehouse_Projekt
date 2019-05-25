import Helper


def execute(_FilePath):
    print("--- Execute exercise 1 ---")

    arrayOfRestaurantNames = Helper.readFile(_FilePath)
    print("arrayOfRestaurantNames: ", arrayOfRestaurantNames)

    matrixWithEditDistances = Helper.createMatrixWithEditDistances(arrayOfRestaurantNames)

