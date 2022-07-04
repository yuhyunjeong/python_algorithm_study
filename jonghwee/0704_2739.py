import sys

N = int(sys.stdin.readline());
for i in range(1,10,1):
    print(str(N) + " * " + str(i) + " = " + str(N*i));
    #print(N,"*",i,"=",N*i);
    # , 로 나누면 자동으로 한칸씩 띄어지게 된다. 수동으로 띄어쓰기를 하려면 sep=""를 추가해준다.
    # 추가적으로 end=""를 해주면 print 마다 뒤에 원하는 것을 붙일 수 있다.