import math


class Circle:

  def __init__(self, radius, y, x):
   self.x = x
   self.y = y
   self.radius = radius

  def input_Data(self):
      self.x = int(input("faka ikho odineythi zika x"))
      self.y = int(input("faka ikho odineythi zika y"))
      self.radius = int(input("fak irediyasi"))

  def perimeter(self):
      d = 2 * (3.14 * self.radius)
      print(" ipherimitha yesekile ngu", d)

  def Area(self):
      a = (3.14) * (self.radius * self.radius)
      print(" ieriya yesekile ngu ", a)


  def outsideinsidecircle(self):
      distance = math.sqrt((self.x-0) * (self.x-0) + (self.y-0) * (self.y-0))

      if distance < self.radius:
       print(" ipoynti ingaphakathi kwesekile")
      else:
       print(" ipoynti ingaphandle kwesekile")


if __name__ == '__main__':
    p = Circle(3, 5, 6)
    p.input_Data()
    p.perimeter()
    p.Area()
    p.outsideinsidecircle()