def reverse_sort(a):
    current=0
    for i in a:
        min_value = min(a[current:])
        index_min=a[current:].index(min_value)
        a[current:index_min+1]=a[current:index_min+1][::-1]
        print(a)
        current=current+1

'''def reverse_sort(a):
    cost = 0
    for i in range(len(a)-1):

        # find minimum element from i to end
        m = min(a[i:])

        # find index of the minimum element
        print(a[i:])
        m_index = a[i:].index(m)
        print(m_index)

        # reverse from i to m_index
        a[i:m_index+i+1] = a[i:m_index+i+1][::-1]
        print(a)

        # keep track of cost
        cost += len(a[i:m_index+i+1])

    # print(*a)
    return cost'''

a=[4,2,1,3]
p=reverse_sort(a)
