from math import sqrt

def quadratic(a,b,c):
  print('Y-int:'+str(c));
  if(a<0):
    print('Opens:down');
  elif(a>0):
    print('Opens:up');
  if(abs(a)>1):
    print('Parabola width:Narrows');
  elif(0<abs(a)<1):
    print('Parabola width:Widens');
  elif(abs(a)==1):
    print('Parabola width:Standard');
  x=(-1*(b))/(2*(a));
  print('Axis of symmetry:x='+str(x))
  v=(a*(x**2))+(b*x)+c;
  print('Vertex:('+str(x)+','+str(v)+')');
  posInt=((-1*b)+sqrt((b**2)-((4*a)*(c))))/(2*a);
  negInt=((-1*b)-sqrt((b**2)-((4*a)*(c))))/(2*a);
  print('X-ints:'+str(posInt)+','+str(negInt));
