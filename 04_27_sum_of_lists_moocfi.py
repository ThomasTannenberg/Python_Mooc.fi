# Write your solution here
def list_sum(a, b):
    sum_list = []
    for i in range(0, len(a)):
        sum_list.append(a[i] + b[i])
#        print(sum_list)
    
    return sum_list


if __name__ == "__main__":
    a = [1, 2 ,3]
    b = [7, 8, 9]

    print(list_sum(a, b))