# 不用for循环来遍历一个序列中的每一个元素
with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end="")
