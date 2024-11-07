#!/usr/bin/python3
number_of_attempt_allowed =3
#assigning number to attempt
attempt=0
while attempt!= number_of_attempt_allowed:
    #requesting user input of pin
    userpin=int(input('please enter your pin:'))
#setting pin to int
    pin=1234
    # Comparing user pin entered to pin
    if userpin==pin:
        print('Access granted')
        break
    else:
        attempt+=1
else:
    if attempt==number_of_attempt_allowed:
        print('Too many incorrect attempt accessed blocked')
        exit()
