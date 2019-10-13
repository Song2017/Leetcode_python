## 随机产生一个4位数随机码
import random
def randomcode(code_len = 4):
    all_code = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    last_code = len(all_code) - 1
    code = " "
    for _ in range(code_len):
        index = random.randint(0,last_code)
        print(index, code[1])
        code += code[index]
    return(code)
randomcode()