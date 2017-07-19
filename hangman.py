import random
st='league'
ans='------'
l=10
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

while '-' in ans:
        ch = str(input("Guess me !!"))
        pp=find(st,ch)
        for i in pp:
                ans[i]=ch
        print(pp)
        print(ans)
        break
