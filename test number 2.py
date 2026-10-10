print("=====FUCTION_CALCULATOR======")

user=int(input("what operation do you want"))
while:
 try:
  if user == "+":
   user=int(input("what is the first number you want to input"))
   user2=int(input("what is the second number you want to input"))
   ans=print("ANS=",user+user2)
 except ValueError:
  print("you need to type in a number")

  if user == "-":
   user=int(input("what is the first number you want to input"))
   user2=int(input("what is the second number you  want to input"))
   print("ANS=",user-user2)
 except ValueError:
  print("you need to type in a number")

  if user == "**":
   user=int(input("what is the first number you want to input"))
   user2=int(input("what is the second number you  want to input"))
   print("ANS=",user**user2)
 except ValueError:
  print("you need to type in a number")

  if user == "//":
   user=int(input("what is the first number you want to input"))
  print("ANS=",user+user2)
 except ValueError:
  print("you need to type in a number")

  user2=int(input("what is the second number you want to input"))
  print("ANS=",user//user2)
 except ValueError:
  print("you need to type in a number")
 except ZeroDivisionError:
  print("you can't divide by zero")
 



