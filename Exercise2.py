import Helper



def execute(_FilePath):
    print("--- Execute exercise 2 ---")

    arrayOfRestaurantNames = Helper.readFile(_FilePath)
    print("arrayOfRestaurantNames: ", arrayOfRestaurantNames)

    matrixWithEditDistances = Helper.createMatrixWithEditDistances(arrayOfRestaurantNames)

    Helper.analyseMatrixAndCreateOutput(matrixWithEditDistances, arrayOfRestaurantNames, "outputExercise2.txt", 1, rewrite = True)
