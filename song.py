Map = {"Zero":0,"one":1 ,"two":2,"Three":3,"Four":4 ,"five":5,"Six":6 ,"Seven":7,"Eight":8,"nine":9,"Ten":10,}
data=[]
for key,value in Map.items():
   data.append(key)
balance_lines = " green bottles, hanging on the wall,"
count = 10
while (count) > 0:
    print(str(data[count]) + (balance_lines))
    print(str(data[count]) + (balance_lines))
    value = 1
    print("But if " + str(data[value]) + " green bottle, should accidentally fall,")
    count = count - 1
    if (count) > 0:
        print("There'll be " + str(data[count]) + " green bottles, hanging on the wall.\n")
    else:
        print("Now there's NO green bottles, hanging on the wall . (END)")
