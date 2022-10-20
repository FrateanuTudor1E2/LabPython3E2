string = str(input())
ctr = 0
for i in string:
    if(i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i =='o' or i=='O' or i=='u' or i=='U'):
        ctr = ctr+1
print("Number of vowels is: ")
print(ctr)