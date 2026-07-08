def rgb(r, g, b):
    
    def hex(digit):
        return [*"0123456789ABCDEF"][digit]
    
    ans = ""
    
    for decimal in [r, g, b]:
        if (decimal < 0): decimal = 0
        elif (decimal > 255): decimal = 255
        
        ans += hex(int(decimal/16)) + hex(decimal-(int(decimal/16)*16))
    
    return ans