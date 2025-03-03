# n=0
# for i in range(1,11):
#     x_sum=n+i
#     print(x_sum)
#     n=i
#
# x=int,input().split()
#  print(x)
# for num in x:
#     if x % 5==0:
#         print(x)

# x=int,input().split()
#
# for n in range(len(x)):
#     for i in range(n):
#         print(n,end="")
#
#     print("\n")
x= float(input("Enter the distance in KMs:"))

miles =float(x*0.62137)

print(f"The distance in miles is {round (miles,2)}")