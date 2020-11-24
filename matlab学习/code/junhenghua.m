%%%2020.11.24%%%
%%%???%%%
A=[1 3 9 9 8;2 1 3 7 3;3 6 0 6 4;6 8 2 0 5;2 9 2 6 0];
A
[m,n]=size(A);
last=0;
for k=0:9
    s=find(A==k);
    ns=length(s);
    p(k+1)=(last+ns)/25;
    h(k+1)=ns;
end
p
h
P2(1)=p(1);
for j=2:10
    P2(j)=P2(j-1)+p(j);
end
P2(1)=0;
P2
for i=0:9
    P1(i+1)=P2(i+1)*9;
    P1(i+1)=uint8(P1(i+1));
end
P1
for x=1:m
    for y=1:n
        o=A(x,y);
        A(x,y)=P1(o+1);
    end
end
A