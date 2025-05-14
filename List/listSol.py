'''
Python Assignment
List
'''
#------- EASY ------
#Q1
def filter_even_numbers(list):
    result = []
    for i in list:
        if(i%2 == 0):
            result.append(i)
    return result
#Q2
def merge_sorted_lists (l1, l2):
    result = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i+=1
        else:
            result.append(l2[j])
            j+=1
    result.extend(l1[i:])
    result.extend(l2[j:])
    return result

#------- MEDIUM ------
#Q1
def generate_matrix (rows, col):
    result = []
    for i in range(rows):
        row = []
        for j in range(col):
            row.append(i*j)
        result.append(row)
    return result
#Q2
def transpose_matrix (matrix):
    trans = []
    col = len(matrix)
    rows = len(matrix[0])
    for i  in range(col):
        row = []
        for j in range(rows):
            row.append(matrix[j][i])




#------- HARD ------
#Q1
def find_peak(list):
    result = []
    for i in range(1,len(list)-1):
        if(list[i]<list[i+1] and list[i]>list[i+1]):
            result.append(i)
    return result
#Q2
def rotate_list(lst, k):
    n = len(lst)
    if n == 0:
        return lst

    k = k % n  # To handle k > length of list
    rotated = []

    # Step 1: Add the last k elements to the front
    for i in range(n - k, n):
        rotated.append(lst[i])

    # Step 2: Add the first n-k elements after that
    for i in range(n - k):
        rotated.append(lst[i])

    return rotated


#-----------------------------
#   Testcase - main function
#-----------------------------

if __name__ == "__main__":
    #easy
    print("easy\n\n")
    print(filter_even_numbers([1, 2, 3, 4, 5, 6]))
    print(filter_even_numbers([1, 3, 5]))

    print(merge_sorted_lists([1,10,12,34,50],[2,7,11,45,50]))
    #medium
    print("medium\n\n")
    print(generate_matrix(3,3))
    print(generate_matrix(4,3))
    print(transpose_matrix([[1,2,3],
                            [4,5,6],
                            [7,8,9]]
                            ))
    #hard
    print("hard\n\n")
    print(find_peak([1,2,3,4,3,5,6,7,6,5,7,8,9,10]))
    print(rotate_list([2,1,3,4,3,2,6,4,5],5))