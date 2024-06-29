#list=[1,2,3,4,5,4,4,64,4]
list=list(input("Input your List:\n"))
SearchNumInList=input("Input number to search in list:")
#print(str(SearchNumInList),list)
print("Count of",str(SearchNumInList),"in list:",end=" ")
print(list.count(SearchNumInList))