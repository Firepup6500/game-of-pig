import firepup650 as fp

fp.replitCursor = fp.bcolors.REPLIT + "> " + fp.bcolors.RESET

who, cheat = fp.menu(
    {
        "I want to go first": (False, False),
        "The computer can go first": (True, True),
        "The computer can cheat, but I want to go first": (False, True),
        "The computer can cheat and go first": (True, True),
        "Actually I don't want to play at all": (-1, -1),
    },
    "Who goes first?",
)

if who == -1:
    exit()

pScore, cScore = (0, 0)


def roll(doCheating):
    if not doCheating:
        return (fp.randint(1, 6),)
    return (fp.randint(1, 6), fp.randint(1, 6))


def doRound(turn, canCheat, player, computer):
    bank = 0
    rollCounter = 0
    cheatFlag = 0
    if turn:
        print("Computer's turn...")
        shouldRoll = 1
        while shouldRoll:
            res = roll(canCheat)
            if canCheat:
                rollCounter += 1
                print(f"Computer roll {rollCounter}:")
                if res[0] == 1:
                    print(f"Computer rolled a 1 and lost it's bank")
                    break
                bank += res[0]
                rollCounter += 1
                print(f"Computer rolled a {res[0]}, bank is now {bank}")
                if res[1] == 1:
                    rollCounter -= 1
                    shouldRoll = 0
                    cheatFlag = 1
                    break
                bank += res[1]
                print(f"Computer roll {rollCounter}:")
                print(f"Computer rolled a {res[1]}, bank is now {bank}")
                shouldRoll = fp.randint(0, 1)
            else:
                rollCounter += 1
                print(f"Computer roll {rollCounter}:")
                if res[0] == 1:
                    print(f"Computer rolled a 1 and lost it's bank")
                    break
                bank += res[0]
                print(f"Computer rolled a {res[0]}, bank is now {bank}")
                shouldRoll = fp.rint(0, 1)
        if not shouldRoll:
            print(
                f"Computer stopped rolling after {rollCounter} roll(s), bank was {bank} points{' (!! CHEAT !!)' if cheatFlag else ''}"
            )
            computer = computer + bank
    else:
        print("Your turn!")
        shouldRoll = 1
        while shouldRoll:
            rollCounter += 1
            print(f"Your roll {rollCounter}")
            res = roll(False)[0]
            if res == 1:
                print(f"You rolled a 1 and lost your bank")
                break
            bank += res
            print(f"You rolled a {res}, bank is now {bank}")
            shouldRoll = not fp.replitInput("Do you want to keep rolling? (Y|n)").lower().startswith("n")
        if not shouldRoll:
            print(
                f"You stopped rolling after {rollCounter} roll(s), bank was {bank} points"
            )
            player = player + bank
    return player, computer


while max(pScore, cScore) < 100:
    pScore, cScore = doRound(who, cheat, pScore, cScore)
    print(f"\nNew Scores:\nPlayer: {pScore}\nComputer: {cScore}\n")
    who = not who
