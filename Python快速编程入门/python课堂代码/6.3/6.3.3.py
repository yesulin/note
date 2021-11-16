def connect(ip, port=8080): #形参中带默认值 port=8080
    print(f"设备{ip}:{port}连接！")

connect('192.168.1.1') # 可以省略port的实参
connect('192.168.1.1','8000')
