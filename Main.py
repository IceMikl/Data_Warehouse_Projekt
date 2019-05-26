import Exercise1, Exercise2, Exercise3, Exercise4
import time


def main():

    startTime = time.time()

    Exercise1.execute('RestaurantNames.txt')
    Exercise2.execute('RestaurantNames.txt')
    Exercise3.execute('RestaurantNames.txt', 8)
    Exercise4.execute('RestaurantNames.txt')

    print("\n\nExecution time: ", time.time() - startTime, "seconds\n\n")



main()