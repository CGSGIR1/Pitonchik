#Родин Илья 8-1

def int_k(value, k):
    x = value % (2 ** k)
    if x < (2 ** k) // 2:
        return x
    else:
        return x - (2 ** k)
    
    
def uint_k(value, k):
    return value % (2 ** k)


def uint_k_code(value, k):
    x = uint_k(value, k)
    weight = k // 4
    return f"{x:0{weight}X}"

if __name__ == "__main__":
    print(uint_k(40000, 16))
    print(int_k(40000, 16))
    print(uint_k_code(27, 16))
    chisla = (27, -27, 150, -150, 1000, -1000, 40000, -40000,
              1000000, -1000000, 4000000000, 1200, -1200)
    print(f"{'число':{7}}", end="/")
    print(f"{'uint8code':{7}}", end="/")
    print(f"{'uint8':{7}}", end="/")
    print(f"{'int8':{10}}", end="/")
    print(f"{'uint16code':{7}}", end="/")
    print(f"{'uint16':{7}}", end="/")
    print(f"{'int16':{7}}", end="/")
    print(f"{'uint32code':{7}}", end="/")
    print(f"{'uint32':{7}}", end="/")
    print(f"{'int32':{7}}")
    for i in chisla:
        print(f"{i:{10}}", end=" ")
        print(f"{uint_k_code(i, 8):{1}}", end=" ")
        print(f"{uint_k(i, 8):{10}}", end=" ")
        print(f"{int_k(i, 8):{10}}", end=" ")
        print(f"{uint_k_code(i, 16):{10}}", end=" ")
        print(f"{uint_k(i, 16):{5}}", end=" ")
        print(f"{int_k(i, 16):{10}}", end=" ")
        print(f"{uint_k_code(i, 32):{10}}", end=" ")
        print(f"{uint_k(i, 32):{10}}", end=" ")
        print(f"{int_k(i, 32):{10}}")