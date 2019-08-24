def remove_duplicates(dup_list):
    withoutDup = []
    for ele in dup_list:
        if ele not in withoutDup:
            withoutDup.append(ele)
    return withoutDup

dup_list = ['Trip ID', 'Trip ID', '181223303826', '1812311005872']
print(len(dup_list))
print(remove_duplicates(dup_list))
