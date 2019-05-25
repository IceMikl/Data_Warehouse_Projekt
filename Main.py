import Exercise1, Exercise2, Exercise3, Exercise4
import time
import EditDistance
import nltk
import Helper

import phonetics

def main():

    startTime = time.time()

    #Exercise1.execute('RestaurantNames.txt')
    #Exercise2.execute('RestaurantNames.txt')
    #Exercise3.execute('RestaurantNames.txt', 8)
    #Exercise4.execute('RestaurantNames.txt')
    #print(EditDistance.levenstein(""))

    #jaccardDistance()

    print("\n\nExecution time: ", time.time() - startTime, "seconds\n\n")




def jaccardDistance():
    print("--- Execute exercise 1 ---")

    arrayOfRestaurantNames = Helper.readFile('RestaurantNamesTest.txt')
    print("arrayOfRestaurantNames: ", arrayOfRestaurantNames)

    for name1 in arrayOfRestaurantNames:
        for name2 in arrayOfRestaurantNames:
            try:
                if(nltk.jaccard_distance(set(name1), set(name2)) < 0.2 and nltk.jaccard_distance(set(name1), set(name2)) > 0.05):
                    print(name1, " ; ", name2, "\t = ", 1 - nltk.jaccard_distance(set(name1), set(name2)))
            except:
                print("Error in: ", name1, " , ", name2)



main()