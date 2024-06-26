#TASK 1.A  LIST OPERATIONS :

my_list = [1,"nitin",2,"vivek",3,4]
my_list.append(5)
print("AFTER APPENDING : ", my_list)
my_list.remove(3)
print("AFTER REMOVING :",my_list)
my_list[1]= 10
print("AFTER UPDATING : ",my_list)




#TASK 1.B DICTIONARIES OPERATIONS : 

my_dict = {"name":"nitin","program":"BCA","enroll_no":"TCA210"}
my_dict["gender"]="male"
print("AFTER ADDING :",my_dict)
del my_dict["program"]
print("AFTER REMOVING :",my_dict)
my_dict["enroll_no"]="TCA110"
print("AFTER UPDATING  :",my_dict)





#TASK 1.C SET OPERATIONS

my_set = {"nitin","rawat","bca"}
my_set.add("tca210")
print("AFTER ADDING :",my_set)
my_set.remove("rawat")
print("AFTER REMOVING :",my_set)
my_set.discard("nitin")
my_set.add("NITIN RAWAT")
print("AFTER UPDATING :",my_set)
