import time
def main():
    k=int(input("set time : "))
    countdown(k)

def countdown(sec):
    while sec>0:
        min,secs=divmod(sec,60)
        timer=f"{min:02d}:{secs:02d}"
        print(timer,end="\r")
        time.sleep(1)
        sec-=1
    print("*********TIME UP *********")

main()