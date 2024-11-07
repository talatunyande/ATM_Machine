#!/usr/bin/python3
userpin=int(input("enter user pin:"))
pin=1234
if userpin==pin:
                        
                            new_pin =int(input ("enter your new four digit pin : "))
                            if 1001 <= new_pin <=9001:
                                confirm_pin=int(input("confirm  your new pin :"))
                                pin=new_pin
                                print ("your new pin has been changed successfully")
                            else:
                                print("pin do not match . please try again .")
else:
                                 print("new pin must be a four digit integer")