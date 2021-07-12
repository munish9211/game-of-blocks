import hashlib as hs
import time
st = str(input("Enter a String :"))
thres = int('0x0000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF',16)
i=0
t_begin = time.time_ns()
while(1):
    sttemp=st + str(i)
    temp = hs.sha256(sttemp.encode())
    temp2 = int(temp.hexdigest(),16)
    if(temp2 < thres):
        break
    i+=1
print("Smallest Nonce value for 4 zeros time :",i)
t_end = time.time_ns() - t_begin
print("Time(in nanoseconds) to calculate Nonce :",t_end)
