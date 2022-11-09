from turtle import *
import math

# Fractal No.1 - Binary Tree Fractal
def tree(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(45)
     tree(n-1, l/2, pen)
     pen.right(90)
     tree(n-1, l/2, pen)
     pen.left(45)
     pen.backward(l)

#end
     
# Fractal No.2 - Dandelion Fractal
def dandelion(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(90)
     dandelion(n-1, l/2, pen)
     pen.right(60)
     dandelion(n-1, l/2, pen)
     pen.right(60)
     dandelion(n-1, l/2, pen)
     pen.right(60)
     dandelion(n-1, l/2, pen)
     pen.left(90)
     pen.backward(l)

#end 

# Generate Koch element for Snowflake Fractal
def koch(n, l, pen):
     #termination
     if n==0 or l<2 :
          pen.forward(l)
          return
     #endif
     koch(n-1, l/3, pen)
     pen.left(60)
     koch(n-1, l/3, pen)
     pen.right(120)
     koch(n-1, l/3, pen)
     pen.left(60)
     koch(n-1, l/3, pen)

#end
     
# Fractal No.3 - Snowflake Fractal
def flake(n, l, pen):
     #termination
     for i in range(3):
          koch(n, l, pen)
          pen.right(120)
     #endfor
          
 #end
          
# Fractal No.4 - Antiflake Fractal
def antiflake(n, l, pen):
     #termination
     for i in range(3):
          koch(n, l, pen)
          pen.left(120)
     #endfor
          
 #end

# Fractal No.5 - Fern Fractal
def fern(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(2*l/3)
     pen.left(45)
     fern(n-1, l/2, pen)
     pen.right(45)
     pen.forward(2*l/3)
     pen.right(30)
     fern(n-1, l/2, pen)
     pen.left(30)
     pen.forward(2*l/3)
     pen.right(10)
     fern(n-1, 0.75*l, pen)
     pen.left(10)
     pen.backward(2*l)

#end

# Fractal No.6 - Sierpinski's Gasket
def sgasket(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     sgasket(n-1, l/2, pen)
     pen.forward(l)
     pen.left(120)
     sgasket(n-1, l/2, pen)
     pen.forward(l)
     pen.left(120)
     sgasket(n-1, l/2, pen)
     pen.forward(l)
     pen.left(120)

#end

# Fractal No.7 - Sierpinski's Carpet
def scarpet(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     for i in range(4):
          scarpet(n-1, l/3, pen)
          pen.forward(l/3)
          scarpet(n-1, l/3, pen)
          pen.forward(2*l/3)
          pen.right(90)

#end

# Fractal No.8 - octahedron Fractal
def tri3D(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     tri3D(n-1, l/2, pen)
     pen.forward(l/2)
     tri3D(n-1, l/2, pen)
     pen.forward(l/2)
     pen.left(150)
     pen.forward((l/2)/math.cos(0.523599))
     pen.left(60)
     pen.forward(((l/2)/math.cos(0.523599))/2)
     pen.left(150)
     tri3D(n-1, l/2, pen)
     pen.right(150)
     pen.forward(((l/2)/math.cos(0.523599))/2)
     pen.left(150)

# Fractal No.8 - octahedron Fractal
def octahedron(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     elif n==1:
          tri3D(n, l, pen)
          octahedron(n-1, l/2, pen)
          pen.forward(l/2)
          octahedron(n-1, l/2, pen)
          pen.forward(l/2)
          pen.right(120)
          tri3D(n, l, pen)
          pen.forward(l)
          pen.right(120)
          tri3D(n, l, pen)
          octahedron(n-1, l/2, pen)
          pen.forward(l)
          pen.right(90)
          for i in range(5):
               pen.forward((l/2)/math.cos(0.523599))
               pen.right(60)
          #endfor
          pen.forward((l/2)/math.cos(0.523599))
          pen.right(90)

     elif n>1:
          tri3D(n, l, pen)
          octahedron(n-1, l/2, pen)
          pen.forward(l/2)
          octahedron(n-1, l/2, pen)
          pen.right(120)
          tri3D(n-1, l/2, pen)
          pen.forward(l/2)
          pen.left(120)
          tri3D(n-1, l/2, pen)
          pen.forward(l/2)
          pen.left(120)
          tri3D(n-1, l/2, pen)
          pen.forward(l/2)
          pen.right(120)
          pen.forward(l/2)
          pen.right(120)
          tri3D(n, l, pen)
          pen.forward(l)
          pen.right(120)
          tri3D(n, l, pen)
          octahedron(n-1, l/2, pen)
          pen.forward(l)
          pen.right(90)
          for i in range(5):
               pen.forward((l/2)/math.cos(0.523599))
               pen.right(60)
          #endfor
          pen.forward((l/2)/math.cos(0.523599))
          pen.right(90)
#end

# Fractal No.9 - C-Curve         
def c(n, l, pen):
     if n==0 :
          pen.forward(l)
          return
     #endif
     c(n-1, l, pen)
     pen.right(90)
     c(n-1,l, pen)
     pen.left(90)

#end

# Fractal No.10 - Pentagon with spacing
def pent(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     for i in range(5):
          pent(n-1, l/3, pen)
          pen.forward(l)
          pen.left(72)
#end

# Fractal No.11 - Pentagon without spacing
def pent0(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     for i in range(5):
          pent0(n-1, 0.3819660114*l, pen)
          pen.forward(l)
          pen.left(72)
     
#end

# Fractal No.12 - Circle Fractal
# The radius for the inner 4 circles is calculated by Rbig = Rsmall + sqrt.2
def circle(n, r, pen):
     if n==0 or r<1 :
          return
     elif n==1:
          pen.circle(r)
     elif n>1:
          pen.circle(r)
          for i in range(4):
               pen.circle(0.41421356237*r)
               pen.up()
               pen.left(90)
               pen.forward(0.41421356237*r)
               pen.right(90)
               pen.forward(0.41421356237*r)
               pen.right(90)
               pen.down()
               pen.circle(0.17157287525*r)
               pen.up()
               pen.right(90)
               pen.forward(0.41421356237*r)
               pen.right(90)
               pen.forward(0.41421356237*r)
               pen.right(90)
               pen.down()
               pen.circle(0.17157287525*r)
               pen.up()
               pen.left(90)
               pen.forward(0.17157287525*r)
               pen.right(90)
               pen.forward(r)
               pen.left(90)
               pen.down()
               circle(n-1, 0.41421356237*r, pen)
          #endfor
     #endif
          
#end
