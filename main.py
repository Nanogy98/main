pi=2
r=input('縦の値')
R=int(r)
l=input('横の値')
L=int(l)
menseki=R*L/pi
print('三角形の面積は '+str (menseki))

###########################################

r=input('縦の値')
R=int(r)
l=input('横の値')
L=int(l)
menseki=R*L
print('四角形の面積は '+str (menseki))

###########################################

pi=3.14
r=input('半径の値')
R=int(r)
menseki=R*R/pi
print('円の面積は '+str (menseki))

###########################################

ti=2
r=input('上底の値')
R=int(r)
l=input('下底の値')
L=int(l)
t=input('高さ')
T=int(t)
menseki=(r+l)*t/2
print('台形の面積は '+str (menseki))
 
###########################################

l=input("数字の桁数を数えます")
L=int(l)
text=l
print(len (text))
