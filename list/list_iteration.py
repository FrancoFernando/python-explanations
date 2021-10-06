def list_iteration():

    my_list = [0,1,2,3,4,5]

    for i in range(0, len(my_list)):
        print(my_list[i])

    for i in range(0, len(my_list),2):
        print(my_list[i])

    for i, num in enumerate(my_list):
        print("index " + str(i) + " value " + str(num))
