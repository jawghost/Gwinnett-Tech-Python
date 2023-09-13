def main():
    golfFile = open("golf.txt", "r")

    playerName = golfFile.readline().rstrip("\n")

    while playerName != "":
        playerScore = golfFile.readline().rstrip("\n")

        print(playerName, "scored",  playerScore, "points")
        playerName = golfFile.readline().rstrip("\n")

    golfFile.close()
main()
