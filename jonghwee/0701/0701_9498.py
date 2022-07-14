import sys

score = int(sys.stdin.readline());
#input() 은 하나 계산 끝나고 새로 계산을 시작하기 때문에 시간이 다소 걸림.
# readline을 쓰면 동시적으로 계산함. 시간이 덜 걸림.
if (100>=score>=90) : print("A");
elif (score>=80) : print("B");
elif (score>=70) : print("C");
elif (score>=60) : print("D");
else : print("F");