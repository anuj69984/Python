# i am going to print my name.
''' multiline
comment '''
'''
print("Started learning python on 02-08-2018")
name="Anuj"
print(name)
print("***************")
print("Arithmetic operation")
print("power : ",2**5)
print(" checking 5//3 operator : ",5//3)
print(" checking 7//2 operator : ",7//2)

print("1-2+3*4 = ",1-2+3*4)

string1="I am not unique"
string2=" because we all are humans"
print(string1+string2)
print("%s %s %s" %('Always remember ',string1,string2))

print("I don't want newline", end="")
print(" : ok")

print("Now I want 5 new line", '\n' *5)
print("I got 5 newline")

'''

'''
print("********** *LIST* **************")
to_purchase1=['phone','charger','data cable']
print("To purchase : ",to_purchase1)
print('\n')

to_purchase2=['book','pen','copy']
print("To purchase : ",to_purchase2)
print('\n')
print("******************")
print("length of list1 : ",len(to_purchase1),'\n')
print("max of list1 : ",max(to_purchase1),'\n')
print("min of list1 : ",min(to_purchase1),'\n')
print("******************")
print("New purchase List: ")
print(to_purchase1,to_purchase2)
print('\n')
print("See the difference of () and []")
new_to_purchse=(to_purchase1,to_purchase2)
print(new_to_purchse)
print('\n')
new_to_purchse1=[to_purchase1,to_purchase2]
print(new_to_purchse1)
print('\n')
print("after Appending ",end="")
to_purchase1.append('speaker')
print("To purchase : ",to_purchase1)
print('\n')
print("inserting elements at particular index")
to_purchase1.insert(3,'laptop')
print(to_purchase1,'\n')
print("sorting ")
to_purchase1.sort()
print(to_purchase1,'\n')
print("reverse sort : ",to_purchase1.reverse())
print(to_purchase1,'\n')
print("removing speaker")
to_purchase1.remove('speaker');
print(to_purchase1,'\n')
print("removing from particular index")
del to_purchase1[1]
print(to_purchase1,'\n')

'''
print("********** *TUPLE* **************")
my_tuple=(2,3,4,5,6,7,8)
print(my_tuple)
print("converting tuple to list")
new_list=list(my_tuple);
print(new_list)
print("converting list to tuple")
new_tuple=tuple(new_list)
print(new_tuple)
print("length of tuple : ",len(new_tuple))
print("max of tuple : ",max(new_tuple))
print("min of tuple : ",min(new_tuple))