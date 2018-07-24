import random
from os import system, name
from time import sleep

class Character: 
 def __init__(self):
  pass

 def getchar(self,a):
  if a == 1:
   b = self.capital_let()
  elif a == 2:
   b = self.small_let() 
  elif a == 3:
   b = self.digit()
  elif a == 4:
   b = self.special_char()
  elif a == 0:
   b = " bye! see you soon"
  return(b)

 def capital_let(self):
  return(chr(random.randint(65,90)))

 def small_let(self):
  return(chr(random.randint(97,122)))

 def digit(self):
  return(str(random.randint(0,9)))

 def special_char(self):
  temp = []
  temp.append(random.randint(33,47))
  temp.append(random.randint(58,64))
  temp.append(random.randint(91,96))
  return(chr(random.choice(temp)))


class password_generator(Character):
 passLen = 0
 passAmt = 0 
 pwds = []
 def __init__(self):
  self.getParameters()

 def getParameters(self):
  self.passAmt = int(input("No. of passwords: "))
  self.passLen = int(input("Length of password: "))

 def generate(self):
  while True:
   p = ''
   for j in range(self.passLen):
    p += super().getchar(random.randint(1,4))
    #print('~',p)
   if self.check(p):
    self.pwds.append(p)
   if len(self.pwds) == self.passAmt:
    break
  print(self.passLen,self.passAmt)
  return(self.pwds)

 def check(self,str):
  (capLat,smLat,digit,spChr) = (False, False,False,False)
  for i in str:
   if i.isupper():
    capLat = True
   elif i.islower(): 
    smLat = True
   elif i.isdigit():
    digit = True
   else:
    spChr = True
   if capLat and smLat and digit and spChr:
    break
  return(capLat and smLat and digit and spChr)   
 

def clear():
 if name == 'nt':
   _ = system('cls')
 else:
  _ = system('clear')



while True:
 clear()
 print('===================Password Generator===================')
 print('========================================================\n\n')  
 object = password_generator()
 for i in object.generate():
  sleep(1)
  print(i,'\b')
 x = int(input('\nPress 0 to Exit(), else to Retry'))
 if x == 0:
  clear()
  print("\n\n\n\t\t\tGood to see you, Bye!")
  sleep(3)
  break
  