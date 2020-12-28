def remove_with_for(my_list):
    result = []
    for n in my_list:
        if n not in result: # while
            result.append(n)
    return result


def remove_using_sets(my_list):
    return list(set(my_list))


print(remove_with_for([1,1,2,2,3,3,3,3,4]))
print(remove_using_sets([1,1,2,2,3,3,3,3,4]))
