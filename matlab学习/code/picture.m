A=[1 2 3 4 5 6;6 5 4 3 2 1;1 6 6 4 6 6;3 4 5 6 6 6;1 4 6 6 2 3;1 3 6 4 6 6];
for(k=1:6)
    s=find(A==k);
    ns=length(s);
    h(k)=ns;
end
h
figure(1);bar(h)