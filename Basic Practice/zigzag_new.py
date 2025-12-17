# Design ZigZag Pattern Program

# Generates a zigzag pattern of stars.
import sys, time


def zigzag(rows, columns):
    maxlen = (rows + columns - 1)

    try:
        for row in range((2*rows - 1)):
            
            # calculate space count
            sp = abs(maxlen - columns - row)
            #space print
            for space in range (sp):
                print(" ", end=" ")

            # print star pattern
            for col in range(columns):
                print("*", end=" ")
                time.sleep(0.03)  # Adding a small delay for visual effect
            print() # move to the next line
            time.sleep(0.1)  # Adding a small delay between rows
    except KeyboardInterrupt:
            print("\nProcess interrupted by user.")
            sys.exit(0)

#Enter a number of rows (growth of the pattern)
rows = int(input("Enter number of rows: "))
#Enter a number of columns (no of stars in the pattern)
columns = int(input("Enter number of columns: "))

zigzag(rows, columns)