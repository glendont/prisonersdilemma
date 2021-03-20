
import AIsimulation, AhumanGame, alwaysCollude, alwaysDefect, titForTat, randomBasic, randomColluding, randomDefecting, \
    grudger, pavlov, Sanjin, myStrategy

choices = {'1-alwaysCollude', '2-alwaysDefect', '3-titForTat', '4-randomBasic', '5-randomColluding',
           '6-randomDefecting', '7-grudger', '8-pavlov', '9-Sanjin', '10-myStrategy'}

strategies = {1: alwaysCollude, 2: alwaysDefect, 3: titForTat, 4: randomBasic, 5: randomColluding, 6: randomDefecting,
              7: grudger, 8: pavlov, 9: Sanjin, 10: myStrategy}

print("******************************************************************************")
print('Here are your game options')
print('press 1 to test your AI strategy against all other AI strategies')
print('press 2 to play against an AI strategy of your choice ')
print("******************************************************************************")
choice = int(input())

if choice == 1:
    print('here are the strategies, choose one: ')
    # print(choices)
    print("1. alwaysCollude \n2. alwaysDefect\n3. titForTat \n4. randomBasic\n5. randomColluding \n6. randomDefecting\n7. grudger \n8. pavlov\n9. Sanjin \n10. myStrategy\n")
    num = int(input('choose a strategy via number'))
    strategy = strategies[num]
    AIsimulation.testStrategy(strategy, 20)

if choice == 2:
    print('who do you want to play against')
    # print(choices)
    print("1. alwaysCollude \n2. alwaysDefect\n3. titForTat \n4. randomBasic\n5. randomColluding \n6. randomDefecting\n7. grudger \n8. pavlov\n9. Sanjin \n10. myStrategy\n")
    num = int(input('choose a strategy via number: '))
    strategy = strategies[num]
    rounds = int(input('how many rounds do you want to play:'))
    AhumanGame.play(strategy, rounds)