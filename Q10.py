# big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]

def max_marks(list_1):
    max=list_1[0]
    for marks in list_1:
        if marks>max:
            max=marks
    return max
    # return
for m_list in marks:
    print(max_marks(m_list))
