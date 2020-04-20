import random as ran
o = 21
print("welcome to stick game")
print("Playing against Computer")
print("Choose nunber between 0 and 4\n")

while o>0:
  print("sticks left : %d " %o)
  if o==1:
      print("you lose")
      break
  u = int(input("YOUR turn! "))
  if u>4 and u<o:
      print("invalid ")
      continue
  o=o-u
  print("sticks left : %d " %o)
  if o==1:
      print("you win")
      break
  c = ran.randrange(1,5)
  if c>o:
      c=1
  if o==4:
      c=3
  print("Computer choose : %d " %c)
  o=o-c
  
  
