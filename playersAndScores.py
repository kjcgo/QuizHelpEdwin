#open the file
my_file = open("players.txt", 'r')

#variables to store current scores and players, and the best score and player
currentPlayer= ''
bestPlayer = ''

currentScore = 0
bestScore = 0

#set isPlayer to true
isPlayer = True

#iterate over each line in the file
for line in my_file:

    #if the line contains a player's name
    if(isPlayer):

        #the currentPlayer we are looking at is the current line
        currentPlayer = line

        #switch for next iteration
        isPlayer = False

    #if the line contains a score
    else:

        #handle exception
        try:

            #the currentScore we are looking at is at the current line
            currentScore = int(line)

            #if this score is better than the current best, replace the best
            if currentScore > bestScore:
                bestScore = currentScore

                #the currentPlayer is now the best player
                bestPlayer = currentPlayer.rstrip("\n")

        #if an incorrect data type
        except ValueError:

            #print the player's name with a star
            print(currentPlayer.rstrip("\n") + "*")

        #switch for next iteration
        isPlayer = True

#display the best player
print(bestPlayer + " is the MVP!")

#close the file
my_file.close()
