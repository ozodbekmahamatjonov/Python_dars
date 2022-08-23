import turtle

def kv(a):
    for i in range(5):
        bob.forward(a)
        
bob = turtle.Turtle()
bob.speed(1)
bob.width(3)

uzunlik = 40
for i in range(10):
    kv(uzunlik)
    bob.right(10)
    uzunlik = uzunlik + 100
