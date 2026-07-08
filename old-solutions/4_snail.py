def snail(snail_map):
    n = len(snail_map[0])
    
    ans = []
    while (snail_map):
        
        top = snail_map[0]
        snail_map = snail_map[1:n]
        
        try: bottom = snail_map[n-2] 
        except: bottom = []
        bottom.reverse()
        snail_map = snail_map[0:n-2]
        
        right = [row[n-1] for row in snail_map]
        snail_map = [row[0:n-1] for row in snail_map]
        
        left = [row[0] for row in snail_map]
        left.reverse()
        snail_map = [row[1:n-1] for row in snail_map]
        
        ans += top+right+bottom+left
        n -= 2
        print(ans)
    
    return ans