import math


def merge_sort(my_list):
        #Find the lowest larger power of 2 than the size of the list
    log_2_len_u = math.ceil(math.log2(len(my_list)))
    req_len = math.pow(2,log_2_len_u)
    diff = int(req_len - len(my_list))

    my_max = max(my_list)+1
    for i in range(diff):
        my_list.append(my_max)

    group_size = 1
    while(group_size < len(my_list)):
            #Double the size of the subgroups
        group_size = int(group_size)

            #new_list is the list after sorting the subgroups
        new_list = []
        ind_list = []
            #For loop to find the sublists to consider
        for i in range(math.floor(len(my_list)/(group_size*2))):
            ind_list.append( 2*group_size*i )

        for i in ind_list:
            sub_1 = []
            sub_2 = []
            for j in range(group_size):
                sub_1.append(my_list[i+j])
                sub_2.append(my_list[i+group_size+j])
            #print("sub_1: ", sub_1)
            #print("sub_2: ", sub_2)
            #print("")
            #print("")
            sorted_list = pairwise_sorting(sub_1,sub_2)

            for value in sorted_list:
                new_list.append( value )
        my_list = new_list
        #print("my_list: ", my_list)
        group_size *= 2
    my_list = my_list[0:len(my_list)-diff]
    #print("Final List: ", my_list)
    

def pairwise_sorting(list1,list2):
    return_list = []
    while (len(list1) != 0 and len(list2) != 0):
        if (list1[0] <= list2[0]):
            return_list.append( list1.pop(0) )
        else:
            return_list.append( list2.pop(0) )
    if (len(list1) == 0):
        for value in list2:
            return_list.append( value )
    else:
        for value in list1:
            return_list.append( value )
    return return_list
