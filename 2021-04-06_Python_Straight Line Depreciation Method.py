#Straight Line depreciation method python
# Computer Programming Tutor,April 5 2021

print("="*75)
print("Calculating Depreciation Using Straight Line Method")
BV = float(input("Enter Book Value: "))
Life = int(input("Enter Life: "))
slvg = float(input("Enter Selvage Value:"))
print("-"*75)
print('%15s'%"Year" '%15s'%"Dep" '%15s'%"BV")
print("-"*75)

for k in range(0,Life):
    Dep = ((BV -slvg)*k)/Life
    AccDep = ((BV-slvg)*(Life-k))/Life
    print('%12.0f'%k,'%12.2f'%Dep,'%12.2f'%AccDep)

print("-"*75)
