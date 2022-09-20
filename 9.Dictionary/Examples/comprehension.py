with open(r'C:\Users\kherad\Desktop\withopen.txt','a') as new:
    print(new.tell())
    new.write('new append')


with open(r'C:\Users\kherad\Desktop\withopen.txt','r') as p:
    p.seek(10)
    print(p.readlines(1))
print()

with open(r'C:\Users\kherad\Desktop\withopen.txt','r') as f:
    a2=f.readlines()
    a2.insert(2,'testing with open')
with open(r'C:\Users\kherad\Desktop\withopen.txt','w') as f2:
    f2.writelines((a2))
print()

with open(r'C:\Users\kherad\Desktop\withopen.txt','r') as X:
    X.seek(18)
    X.write('using seek in file ')

d={'name':'mohammad','age':20,'height':1.81}
s={v*4 for v in d.values()}
print(s)
s2={5*v if not isinstance(v,str) else v*2 for v in d.values()}
print()
print(s2)

from pprint import pprint
d2={k:v*2 if not isinstance(v,int) else v+2 for k,v in d.items()}
print()
print(d2)
dic={"result":
         {"a":[
             {'color':'red','code':(0,4,5),'hue':(1,4,7)}
             ,{'color':'blue','code':(8,2,4,),'hue':(8,8,9)}]
            ,'b':[{'name':'mohammad'}]}}
pprint(dic)



