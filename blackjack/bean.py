import random
import time

def hit():
  global stuff
  x=random.randint(0,11)
  num=int(str(deck[x][0]))
  deck[x].pop(0)
  stuff=stuff+num

def hitd():
  global stuff1
  x=random.randint(0,12)
  if x == 0:
    if stuff1 < 11:
      x=11
    elif stuff1 > 10:
      x=1
  num=int(str(deck[x][0]))
  deck[x].pop(0)
  stuff1=stuff1+num

def go():
  print("Yours:"+str(stuff))
  e=input('1.HIT\n2.STAND\n3.EXIT\n')
  if e == '1':
    hit()
  elif e == '2':
    bjd()
  elif e == '3':
    print('Bye!')
    exit()
  else:
    print("Not 1, 2, or 3!")
    go()

def bj():
  aces=[[1,1,1,1],[11,11,11,11]]
  twos=[2,2,2,2]
  threes=[3,3,3,3]
  fours=[4,4,4,4]
  fives=[5,5,5,5]
  sixes=[6,6,6,6]
  sevens=[7,7,7,7]
  eights=[8,8,8,8]
  nines=[9,9,9,9]
  tens=[10,10,10,10]
  jacks=[10,10,10,10]
  queens=[10,10,10,10]
  kings=[10,10,10,10]
  global stuff1
  stuff1=0
  global deck
  deck=[aces,twos,threes,fours,fives,sixes,sevens,eights,nines,tens,jacks,queens,kings]
  global stuff
  stuff=int(0)
  hit()
  hit()
  while True:
    if stuff == 21:
      bjd()
    if stuff < 22:
      go()
    else:
      print(stuff)
      print('You lose!')
      menu()

def end():
  if stuff == stuff1:
    print("Tie!")
    bj()
  if stuff < stuff1:
    print("Dealer wins!")
    menu()
  elif stuff > stuff1:
    print("You win!")
    menu()

def bjd():
  hitd()
  hitd()
  time.sleep(1)
  print("Dealer's:"+str(stuff1))
  while True:
    if stuff1 < 22:
      if stuff1 < 17:
        hitd()
        time.sleep(1)
        print("Dealer's:"+str(stuff1))
      elif stuff1 > stuff:
        print("Dealer wins!")
        menu()
      else:
        end()
    else:
      print("You win!")
      menu()
      
def menu():
  u=input("1.START\n2.EXIT\n")
  if u == '1':
    bj()
  elif u == '2':
    exit()
  else:
    print('Not 1 or 2!')
    menu()
menu()
