# Create a list of 5 random numbers and print the list.
l_1=[5,6,7,8,3]
print(" The list:",l_1)
#Insert 3 new values to the list and print the updated list
l_1.append(10)
print(l_1)
#Try to use a for loop to print each element in the list.
l_2=["apple",34,"banana"]
for element in l_2:
    print(element)
# Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively.
d_1=dict(name="jhon",age="25",address="New york")
print(d_1)
#Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'.
d_1["phone"]='1234567890'
print(d_1)
#Create a set with values 1, 2, 3, 4, and 5
s_1={1,2,3,4,5}
print(s_1)
#Add the value 6 to the set created
s_1.add(6)
print(s_1)
# Remove the value 3 from the set created
s_1.remove(3)
print(s_1)
#Create a tuple with values 1, 2, 3, and 4
t_1=(1,2,3,4)
print(t_1)
#Print the length of the tuple created
print(len(t_1))



