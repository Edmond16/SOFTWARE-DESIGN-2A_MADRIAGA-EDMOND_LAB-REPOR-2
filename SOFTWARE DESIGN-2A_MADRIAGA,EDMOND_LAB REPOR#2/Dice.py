#Roll and Dice Setup
die1 = 0
die2 = 0

def roll():
    global rollHard, pointIsOn, die1, die2
    rollHard = False
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    if d1 > d2 or d1 == d2:
           die1 = d1
           die2 = d2
    else:
           die1 = d2
           die2 = d1
           total = die1 + die2
if die1 == die2 and total in [4, 6, 8, 10]:
    rollHard = True
    print("{} the Hard Way!".format(total))
elif total in [7, 11] and pointIsOn == False:
    print("{total} winner! Pay the line, take the don't!".format(total=total))
else:
    call = randint(1, 10)
    if call <=5 or total in [2, 3, 11, 12]:
        print("{tot}, {call}!".format(tot=total, call=stickman(total)))
    else:
        print("{tot}, a {d1} {d2} {tot}!".format(tot=total, d1=die1, d2=die2))
        return total

dealerCalls = {
    2: ["Craps", "eye balls", "two aces", "rats eyes", "snake eyes", "push the don't", "eleven in a shoe store", "twice in the rice", "two craps two, two bad boys from Illinois", "two crap aces", "aces in both places", "a spot and a dot", "dimples", "double the Field"],
    3: ["Craps", "ace-deuce", "three craps, ace caught a deuce, no use", "divorce roll, come up single", "winner on the dark side", "three craps three, the indicator", "crap and a half", "small ace deuce, can't produce", "2 , 1, son of a gun"],
    4: ["Double deuce", "Little Joe", "Little Joe from Kokomo", "Hit us in the 2 2", "2 spots and 2 dots", "Ace Tres"],
    5: ["After 5 the Field's alive", "Fiver Fiver Race Track Driver", "No Field 5", "Little Phoebe", "We got the fiver", "Five 5"],
    6: ["The national average", "Big Red, catch 'em in the corner", "Sixie from Dixie"],
    7: ["Line Away, grab the money", "the bruiser", "point 7", "Out", "Loser 7", "Nevada Breakfast", "Cinco Dos, Adios", "Adios", "3 4 on the floor"],
    8: ["a square pair", "eighter from the theater", "windows", "the Great!", "get yer mate"],
    9: ["niner 9", "center field 9", "Center of the garden", "ocean liner niner", "Nina from Pasadena", "nina Niner, wine and dine her", "El Nine-O", "Niner, nothing finer"],
    10: ["puppy paws", "pair o' roses", "The big one on the end", "55 to stay alive", "pair of sunflowers", "two stars from Mars", "64 out the door"],
    11: ["Yo Eleven", "Yo", "6 5, no drive", "yo 'leven", "It's not my eleven, it's Yo Eleven"],
    12: ["craps", "midnight", "a whole lotta crap", "craps to the max", "boxcars", "all the spots we gots", "triple field", "atomic craps", "Hobo's delight"]
}

def stickman(roll):
    return dealerCalls[roll][randint(0, len(dealerCalls[roll])-1)]

# Fire Bet Setup

fire = []
fireBet = 0

"""
win 4 numbers : 24:1
win 5 numbers: 249:1
win 6 numbers: 999:1
2, 3, 7, 11, 12 do not affect fire bet, only 7 outs in phase 2.
Once point is hit, the same point does not add to the fire bet. Fire bet must hit all 6 different point numbers.
Payout starts at 4 point numbers on a 7 out. 3 or less is a full loss.
"""

def fireBetting():
       global fireBet
       print("\tHow much on the Fire Bet?")
       fireBet = betPrompt()
       print("\tOk, ${} on the Fire Bet. Good Luck!".format(fireBet))

def fireCheck():
       global bank, fire, fireBet, comeOut, p2, chipsOnTable
       if p2 == 7:
              chipsOnTable -= fireBet
              if len(fire) < 4:
                     print("You lost ${} from the Fire Bet.".format(fireBet))
                     #bank -= fireBet
                     fireBet = 0
                     fire = []
              elif len(fire) == 4:
                     print("You won ${} on the Fire Bet! Great job!".format(fireBet * 25))
                     bank += fireBet * 25
                     fireBet = 0
                     fire = []
              elif len(fire) == 5:
                     print("You won ${} on the Fire Bet! Holy Crap!".format(fireBet * 250))
                     bank += fireBet * 250
                     fireBet = 0
                     fire = []
              elif len(fire) == 6:
                     print("Wowsers! You nailed the Fire Bet Jackpot and won ${}!!!".format(fireBet * 1000))
                     bank += fireBet * 1000
                     fireBet = 0
                     fire = []
              elif p2 in [4, 5, 6, 8, 9, 10] and p2 == comeOut:
                     if p2 not in fire:
                            fire.append(p2)
                            fire.sort()
                            print("Fire Bet Point Numbers: {}".format(fire))
                            # Hard Ways Setu
                            rollHard = False
                            hardOff = False
                            hardWays = {
                                   4: 0,
                                   6: 0,
                                   8: 0,
                                   10: 0
                                   }

def hardWaysBetting():
       global hardWays, chipsOnTable
       for key in hardWays:
              if hardWays[key] > 0:
                     print("You have ${bet} on the hard {num}.".format(bet=hardWays[key], num=key))
                     print("How much on the Hard {}?".format(key))
                     bet = betPrompt()
                     if bet > 0:
                            chipsOnTable -= hardWays[key]
                            hardWays[key] = bet
                            print("Ok, ${bet} on the Hard {num}.".format(bet=hardWays[key], num=key))
                     elif hardWays[key] > 0 and bet == 0:
                            print("Taking down your Hard {}.".format(key))
                            chipsOnTable -= hardWays[key]
                            bank += hardWays[key]
                            hardWays[key] = bet

def hardTakeDown():
       global hardWays, bank, chipsOnTable
       print("Taking down your Hard Ways.")
       for key in hardWays:
              chipsOnTable -= hardWays[key]
              bank += hardWays[key]
              hardWays[key] = 0
def hardAuto():
       global chipsOnTable, bank, hardWays
       print("How many $1 units on each of the Hard Ways?")
       hardAcr = betPrompt()
       chipsOnTable -= hardAcr
       for key in hardWays:
              chipsOnTable -= hardWays[key]
              bank += hardWays[key]
              hardWays[key] = hardAcr
              chipsOnTable += hardAcr
              print("Ok, ${} on each of the Hard Ways.".format(hardAcr))

def hardHigh(num):
       global chipsOnTable, bank, hardWays
       number = int(num[1:])
       print("How much to spread across the Hard Ways, high on the {}?".format(number))
       bet = betPrompt()
       for key in hardWays:
              chipsOnTable -= hardWays[key]
              bank += hardWays[key]
              if key == number:
                     hardWays[key] = bet - (bet//5*3)
              else:
                     hardWays[key] = bet//5
                     print("Ok, ${a} on the Hard {number}, ${b} each on the other Hard Ways for a total of ${bet}.".format(a=(bet-(bet//5*3)), b=(bet//5), number=number, bet=bet))


"""
algorithm for spreading wierd bets across with a high number:
bet - (bet//5 * 3) = high bet
bet//5 = low bets
"""

def hardCheck(roll):
       global bank, chipsOnTable, hardWays, rollHard
       if roll == 7:
              loss = 0
              for key in hardWays:
                     if hardWays[key] > 0:
                            loss += hardWays[key]
                            hardWays[key] = 0
                            if loss > 0:
                                   print("You lost ${} from the Hard Ways.".format(loss))
                                   #bank -= loss
                                   chipsOnTable -= loss
                            elif roll in [4, 6, 8, 10]:
                                   if hardWays[roll] > 0 and rollHard == True:
                                          if roll in [4, 10]:
                                                 win = hardWays[roll] * 8
                            elif roll in [6, 8]:
                                   win = hardWays[roll] * 10
                                   print("You won ${win} on the Hard {num}!".format(win=win, num=roll))
                                   bank += win
                                   print("Press your bet?")
                                   hardPress = input(">")
                                   if hardPress.lower() in ['y', 'yes']:
                                          print("How much on the Hard {}?".format(roll))
                                          chipsOnTable -= hardWays[roll]
                                          #bank += hardWays[roll]
                                          hardWays[roll] = betPrompt()
                                          if hardWays[roll] == 0:
                                                 print("Ok, taking down your Hard {} bet.".format(roll))
                                          else:
                                                 print("Ok, bumping up your Hard {num} bet to ${bet}.".format(num=roll, bet=hardWays[roll]))
                                   else:
                                          pass
                            elif hardWays[roll] > 0 and rollHard == False:
                                   print("You lost ${loss} from the Hard {num}.".format(loss=hardWays[roll], num=roll))
                                   #bank -= hardWays[roll
                                   chipsOnTable -= hardWays[roll]
                                   print("Go back up on your Hard {} bet?".format(roll))
                                   hardBack = input(">")
                                   if hardBack.lower() in ['y', 'yes']:
                                          print("How much on the Hard {}?".format(roll))
                                          hardWays[roll] = betPrompt()
                                          print("Ok, going back up on the Hard {num} for ${bet}.".format(num=roll, bet=hardWays[roll]))
                                   else:
                                          hardWays[roll] = 0


