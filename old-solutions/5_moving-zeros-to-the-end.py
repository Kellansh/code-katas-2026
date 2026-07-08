def move_zeros(lst):
    
    if not hasattr(lst, "__len__"):
        raise Exception("Invalid input")
    if lst != [*lst]:
        raise Exception("Invalid input")
    
    countzeros = lst.count(0)
    
    for i in range(countzeros):
        lst.remove(0)
        lst.append(0)
    
    return lst