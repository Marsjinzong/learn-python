
#-*-coding:utf8;-*-
#qpy:2
#qpy:console

print "This is console module"
def checkid(idnum):
 a={i:(2**(18-i))%11 for i in range(1,18)}
 end ={0:"1",1:"0",2:"X",3:"9",4:"8",5:"7",6:"6",7:"5",8:"4",9:"3",10:"2"}
 if len(idnum)!=18:
  return "wrong number"
 else: 
  sum =0
  for i, j in enumerate(idnum,start =1):
   if i==18 and end[sum%11]==j:
	return "True"
   elif i==18 and end[sum%11]!=j:
    return  "False"
   else: 
    sum=sum +int(j)*a[i]
idnum  =raw_input("input id: ")
print checkid(idnum)
print u'以下是随机生成的身份证号进行验证：'
import random
ranid=""
for i in range(18):
 if i==17:
  ranid += str(random.choice(range(10)+["X"]))
 else: 
  ranid +=str(random.randint(0,9))
print ranid
print checkid(ranid)
print u'以下是从文件中读取到的身份证号并进行验证，验证结果如下：'
file = open('C:\Users\Lenovo\Desktop\id_number.txt','r')
for val in file:
	idnum = str(val)
	print checkid(idnum)
