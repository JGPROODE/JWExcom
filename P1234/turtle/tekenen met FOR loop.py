import turtle

t=turtle.Pen()
 

for angle in range(0, 360, 15):
    t.setheading(angle)
    t.forward(100)
    t.write(str(angle) + '°')
    t.backward(100)

  

woord=""
for x in "banana":
  #print(x)
  if x=="a":
   continue
  woord+=x
  print(x)
print (woord)

  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Write a script that prints every even numbers between 1 and 100 inclusive, one per line.
for getal in range(1,101):
    print(str(getal))
