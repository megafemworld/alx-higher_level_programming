#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    try:
        for i in range(list_length):
            a = my_list_1[i]
            b = my_list_2[i]
            if a == 0 or b == 0:
                div_list.append(0)
                print("division by 0")
            elif type(a) is not int or type(b) is not int:
                if type(a) is not float or type(b) is not float:
                    div_list.append(0)
                    print("wrong type")
            elif a < b or a < 0 or b < 0:
                div_list.append(0)
            else:
                div_list.append(a/b)
    except Exception as e:
        div_list.append(0)
        print("out of range")
    finally:
        return div_list
