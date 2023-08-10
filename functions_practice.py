def hello():
    print("Greeting User")

def pack(a,b,c):
    return[a,b,c]

def eat_lunch(lunch):
    if len(lunch) == 0:
        print("My lunchbox is empty")
    else: 
        for i in range(len(lunch)):
            if i == 0:
                print(f"First I eat {lunch[0]}")
            else:
                print(f"Next I eat {lunch[i]}")

hello()
print(pack("a", "b", "c"))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["berries", "carrots", "cupcake", "sandwich"])