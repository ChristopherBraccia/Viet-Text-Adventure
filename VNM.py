
import time
import sys
import pip

correct = True
while correct:
    print('+++++ Choose your own Adventure - Chris +++++')
    time.sleep(2)
    print('You have no memory of how you got here...')
    time.sleep(3)
    print('Your mouth is heavy with the taste of copper as you struggle to come to your senses.')
    time.sleep(3)
    print('As you open your eyes you can begin to make out your immediate surroundings.')
    print('You are laying on your back looking up at the sky, the air is dense and swirling with smoke.')
    time.sleep(3)
    print('Above you are scarred and battered Palm Trees. You begin to regain your hearing.')
    print('"What would you like to do? Take a moment to get your "Senses" or "Stand"?"')
    choice1 = input()
    if choice1 == 'Senses' or choice1 == 'senses':
        print('You decide to take a moment to regain your self.')
        time.sleep(3)
        print('You begin to notice that the area around you is charred and smoldering.')
        time.sleep(3)
        print('You can start to make out the sound of the wind ripping through the trees and another sound off in the distance.')
        time.sleep(4)
        print('As you sit up you notice you are surrounded by tall sawgrass hedges. The sound off in the distance is becoming steadly louder.')
        print('"What would you like to do? "Stand" or "Stay"?')
    if choice1 == 'Stand' or choice1 == 'stand':
        print('You begin to stand only to have your legs give out from under you.')
        time.sleep(3)
        print('You decide to take a moment to regain your strength.')
        time.sleep(3)
        print('You begin to notice that the area around you is charred and smoldering.')
        time.sleep(4)
        print('You can start to make out the sound of the wind ripping through the trees and another sound off in the distance.')
        time.sleep(4)
        print('As you sit up you notice you are surrounded by tall sawgrass hedges. The sound off in the distance is becoming steadly louder.')
        print('"What would you like to do? "Stand" or "Stay"?')
    choice2 = input()
    if choice2 == 'Stand' or choice2 == 'stand':
        print('You struggle to get to your feet. Your legs shake violently underneath you as blood rushes back into your lower body.')
        time.sleep(2)
        print('As your legs steady you can start to make out the distand sound that has been growing louder by the second.')
        print('Fortunate Son comes ripping through the air as a UH-1 Helicopter comes buzzing over head.')
        print('Are you "Viet" Cong or are you an "American".')
    choice3 = input()
    if choice3 == 'Viet' or choice3 == 'viet':
        print('The Helicopter has spotted you and begins to turn around.')
        print('Will you "Run" or "Stay"?')
    if choice3 == 'American' or choice3 == 'american' or choice3 == 'murican' or choice3 == 'Murican':
        print('The helicopter has spotted you and begins to turn around.')
        print

