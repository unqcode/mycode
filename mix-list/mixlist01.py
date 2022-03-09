#!/usr/bin/env python3

### How to make list.####

# my_list = [ "192.168.0.5", 5060, "UP" ] #my_list is a word that has value isnide brackets that forms a list.

# print("The first item in the list (IP): " + my_list[0] ) #add + value[number of index] to display info (pull first item)

# print("The second item in the list (port): " + str(my_list[1]) ) #add + str(value[number of index]). str is needed as index is an integer and need to combine as str.

# print("The last item in the list (state): " + my_list[2] ) #same as line:7 (pull last item)


iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
print("IP addresses: " + iplist[3] + ", and " + iplist[4])

