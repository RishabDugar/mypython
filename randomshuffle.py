import random
dict={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
fo=open("word.txt","r+")
wlist=fo.read()
st=wlist.split()
#word1=st[0]
new_dict={}
s=0
for i in st:
        for word,k in dict.items():
                if word in i:
                        s+=k
                #print(s)
                new_dict[i]=s
        print(new_dict)

for i in st:
        word1=i[1:-1]
        print (str(i[0])+str(''.join(random.sample(word1, len(word1))))+str(i[-1]))
