#!/usr/bin/python3
# assigning a variable balance to 1000
balance=(1000)
#assigning number to variable number_of_attempt_allowed
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

        total_deposits =0
        total_withdrawals =0
        #using whileTrue to loop to display the main menu
    while True:
        print("\n--- Main_Menu---")
        print("\n 1.Check Balance","\n 2.Deposit Funds","\n 3.withdraw Funds","\n 4.Change Pin","\n 5. Exixt")

        #using If,else,elif statements for cjecking balance,depositingfunds,changing pin and existing

        Option=int(input("select Options (1-5):"))
        if Option==1:
            print(f"you have ${balane} left")
        elif Option==2:
            deposited_fund=float(input("Input deposit amount :"))
            if deposited_fund >0:
                total_deposits+=deposited_fund
                print(f"you have deposited ${deposited_fund}. Your new balance is ${balance}")
            else:
                print("please enter a positive number .")

        elif Option==3:
            amount_withdrawn = float(input("input amount to withdraw : "))
            if amount_withdrawn >0:
                if balance !=amount_withdrawn:
                    total_withdrawals +=amount_withdrawn
                    print (f"you have withdrawn ${amount_withdrawn}.new balance is: ${balance}")
                elif Option==4:
                    userpin=int(input("enter user pin:"))
                    if userpin==pin:
                        while True:
                            new_pin =int(input ("enter your new four digit pin : "))
                            if 1001 <= new_pin <=9001:
                                confirm_pin=int(input("confirm  your new pin :"))
                                pin=new_pin
                                print ("your new pin has been changed successfully")
                                break
                            else:
                                print("pin do not match . please try again .")
                        else:
                          print("new pin must be a four digit integer")
                                

                    elif Option==5:
                        print(f"total withdrawal is :${total_withdrawals} and total deposit made is ${total_deposits}\n total amount is ${balance}")
                        break
                    else:
                        print("invalid option, please try again")





        