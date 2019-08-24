def remove_duplicates(dup_list):
    withoutDup = []
    for ele in dup_list:
        if ele not in withoutDup:
            withoutDup.append(ele)
    return withoutDup

dup_list = ['Duplicate', 'Duplicate', '21321312', '37247232']
print(len(dup_list))
print(remove_duplicates(dup_list))
