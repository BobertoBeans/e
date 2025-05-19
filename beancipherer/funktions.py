def bean():
  print('Please enter the word you want to beancipher!');
  word=input('');
   
  word=word.lower();
   
  wordlist=list(word);

  wordlist=list(word);

  alph='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz';

  n=0;
  x=0;
  y=0;

  while(n<len(word)):
      bool=False;
      while(bool==False):
         bool=word[x]==alph[y];
         y+=1;
      wordlist[x]=alph[y+x];
      y=0;
      x+=1;
      n+=1;
      bool=False;
  wordlist=''.join(wordlist);
  print(wordlist.upper());
  menu();

def debean():
    print("Please enter the word you want to debeancipher('Z's don't work)!")
    word=input('');
   
    word=word.lower();

    wordlist=list(word);

    alph='                 abcdefghijklmnopqrstuvwxyz';

    n=0;
    x=0;
    y=0;

    while(n<len(word)):
      bool=False;
      while(bool==False):
         bool=word[x]==alph[y];
         y-=1;
      wordlist[x]=alph[y-x];
      y=0;
      x+=1;
      n+=1;
      bool=False;
    wordlist=''.join(wordlist);
    print(wordlist.upper());
    menu();

def menu():
   print('1, 2 or 3?'); x=input('');

   if(x=='1'):
         bean();
   elif(x=='2'):
         debean();
   elif(x=='3'):
         print('                ░░░░░░░░░                    ')
         print('               ▓▒░░░░░░░░▒                   ')
         print('               ▒░░░░░▒▒░▒▒▓                  ')
         print('              ████▒███▓▓▒▒▓                  ')
         print('             █▓▒▒█░▓██▓▓▓▓▓                  ')
         print('             ███▒▓░▒▓▓▓▓░▒▓                  ')
         print('             ▒▒▒▒▓░▒▒▒▒▒▒▓█                  ')
         print('             ▒▓█████▓▓█████                  ')
         print('              ▒████▓▓▓▓████                  ')
         print('               ░▓██▓▓▒▓▓███                  ')
         print('               ░███▓▓▓▓▓▓▓█                  ')
         print('               ▒███▓▓▓▓▓▓▒▓                  ')
         print('               ▓▓█▓▓▓▓▓▓█▒▓                  ')
         print('               █▒█▓▓▓▓▓▓█▓▓                  ')
         print('               █▓█▓▓▓▓▓▓█▒▓                  ')
         print('               ▓▓█▓▓▓▓▓▓█▒▓                  ')
         print('              ▓▒▓██▓▓▓▓▓▒▓▓                  ')
         print('              ██▓██▓▓▓▓▓▓▓                   ')
         print('              ▒▒████▓▓███                    ')
         print('             ▒▒▓ ███ █▓██                    ')
         print('            ▒▒▓█ ▓▓█ ▓▓▓█                    ')
         print('           ▒▒▓█  ▓▓█ ▓▓▓█                    ')
         print('          ▒▒▓    ███  █▓▓                    ')
         print('         ▒▒▓█     ██  █▓▓                    ')
         print('       ▒▒▒▓█      ██  ███                    ')
         print('      ▓▓▓██       ██  ███                    ')
         print('    ▓▓▓▓██       ░▒▓█ ▓▓▓                    ')
         print('   ▓▓▓▓██   ░░░░░▒▓▓█▒░▒▓▓                   ')
         print('   █████  ▓▓▒▒▒▒▓███▒░▒▒▒▒                   ')
         print('            ████   ▓▓▓▓▓▓▓                   ')
         exit();
   else:
         print('Please enter 1, 2 or 3!');
         menu();
