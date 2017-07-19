import random
alp='a b c d e f g h i j k l m n o p q r s t u v w x y z'
alp=alp.split();
fo=open("wordlist.txt","r+")
st2=fo.read()
ans="";
st=st2.split()[random.randint(0,170)]
#print(st)
ans=len(st)*'-'
l=6
ch="@"
HANGMANPICS = ['''

   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

while '-' in ans and l>0:
    while True:
        ch = str(input("Guess me !!"))
        if ch not in alp:
            print("already used")
            #print(alp)
        else:
            alp=[x.replace(ch,'')for x in alp]
            break
    if ch not in st:
        l=l-1
        print(HANGMANPICS[6-l])
    pp=find(st,ch)
    for i in pp:
        lst1=list(ans)
        lst1[i]=ch
        ans = ''.join(lst1)
    print(ans)
    print("chances left :"+str(l))
    ch="@"
    
if '-' not in ans:
    print("You Win!")
elif '-' in ans or l==0:
    print("you lose ,the word was :"+st)
