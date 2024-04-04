#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    try:
        for i in range(list_length):
            if my_list_1[i] == 0 or my_list_2[i] == 0:
                div_list.append(0)
                print("division by 0")
            elif type(my_list_1[i]) is str or type(my_list_2[i]) is str:
                div_list.append(0)
                print("wrong type")
            else:
                div_list.append(my_list_1[i]/my_list_2[i])
        return div_list
    except Exception as e:
        div_list.append(0)
        print("out of range")
    finally:
        print("{}".format(div_list))
