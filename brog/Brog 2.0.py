def brog():
  x=input('What word do you want to brogify?\n');
  lX=list(x);
  y=0
  n=0;
  if(len(x)<3):
    print('Not a big enough word!')
    brog()
  for n in x:
    lX[y]='o';
    y+=1;
  lX[0]='B';
  lX[1]='r';
  lX[-1]='g';
  x2=''.join(lX);
  print(x2)
  print(x2[::-1])
  brog()
brog()
