class Square:
   def __init__(self, a):
      self.a = a
   def area(self):
      return self.a * self.a
   def perimiter(self):
      return 4*self.a

square1 = Square(4)
square2 = Square(6)

print(f'Square with side 4:{ square1}')
print(f'Area is {square1.area()}, Perimeter is {square1.perimiter()}')
print (f'Square with side 6: {square2}')
print(f'Area is {square2.area()}, Perimeter is {square2.perimiter()}')