for n=1:10
    a(n)=2^n;
end
disp(a)

m=1;
for i=1:2:10
    b(m)=2^i;
    m=m+1;
end
disp(b)

A=[1,2,5,6;2,3,4,5];
for i=1:2
    for j=1:3
        B(i,j)=A(i,j);
    end
end
B