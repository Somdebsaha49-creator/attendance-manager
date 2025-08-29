import numpy as np
dic={
    "Nikhil" : ["Present", "Absent", "Present", "Present"],
    "Suresh" : ["Present", "Absent", "Absent", "Present"],
    "Puneet" : ["Absent", "Absent", "Absent", "Present"]
}
print(dic)
print('')
a=[]
a=dic["Nikhil"]
b=[]
b=dic["Suresh"]
c=[]
c=dic["Puneet"]
a1=0
l1=0
b1=0
l2=0
c1=0
l3=0
for i in a:
    if i=="Present":
        a1=a1+1
    l1=l1+1
for j in b:
    if j=="Present":
        b1=b1+1
    l2=l2+1
for k in c:
    if k=="Present":
        c1=c1+1
    l3=l3+1
x1=(a1/l1)*100
x2=(b1/l2)*100
x3=(c1/l3)*100
print('Percentage Attendance for Nikhil is ',end='')
print(x1)
print('')
print('Percentage Attendance for Suresh is ',end='')
print(x2)
print('')
print('Percentage Attendance for Puneet is ',end='')
print(x3)
print('')
s=x1+x2+x3
avg=s/3
print('Average Class Attendance is ',end='')
print(avg)
print('')
X=np.array(["Puneet","Suresh","Nikhil"])
Y=np.array([x3,x2,x1])
import matplotlib.pyplot as plt
plt.bar(X,Y,color=['red','blue','green'],width=0.25)
plt.title('Bar Graph to Visualize Attendance')
plt.show()