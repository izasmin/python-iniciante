https://www.casio-calculadoras.com/images/casio-news/CASIO_NEWS_N22_2022.pdf

Escreva um programa, em linguagem Python, que determina a equação reduzida da
reta s, perpendicular à reta r definida por y = mx + b (com m "≠" 0) e que contém o
ponto P de coordenadas (xP , yP).

print("Equacao da reta s")
print("perpendicular a r")
print("e que contem P: ")

print("r: y=mx+b")
m1 = float(input("m="))
b1 = float(input("b="))
print ("P(xP, yP)")
x = float(input("xP="))
y = float(input("yP="))

m2 = -1 / m1
b2 = y + x/m1

print()
print("s: y=", m2, "x+", b2)

Escreva um programa, em linguagem Python, que calcula a soma dos N primeiros
termos de uma progressão aritmética ou geométrica, conhecendo o primeiro termo
e a razão

print("Soma dos N primeiros \n termos de uma: ")
print("-prog. aritmetica: \n prima [1]")
print("-prog. geométrica: \n prima[2]")
p = int(input("?"))

if p!=1 and p!-2:
  print("Valor invalido!")
else:
  u1 = float(input("u1 = "))
  r = float(input("r = "))
  N = int(input("N = "))
  if p==1:
    uN = u1+(N-1) *r
    s = (u1+uN) *N/2
   else:
    s = u1*(1-r**N)/ (1-r)
   print("Soma: s =", s)
