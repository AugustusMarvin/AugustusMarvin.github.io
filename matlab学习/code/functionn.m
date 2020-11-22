function x=freebody(x0,v0,t)
x=x0+v0.*t+1/2*9.8*t.*t;

distance = freebody([1,2],[2,3],[4,5])