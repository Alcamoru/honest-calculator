def is_one_digit(v):
    return -10 < v < 10 and v.is_integer()


def check(v1: float, v2: float, v3: float):
    msg = ""
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


memory = 0
while True:
    print("Enter an equation")
    x, op, y = input().split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        x = float(x)
        y = float(y)
        if op in "+-*/":
            check(x, y, op)
            if op == "/" and float(y) == 0.0:
                print("Yeah... division by zero. Smart move...")
            else:
                if op == "+":
                    res = x + y
                elif op == "-":
                    res = x - y
                elif op == "*":
                    res = x * y
                elif op == "/":
                    res = x / y
                else:
                    res = None
                print(res)
                print("Do you want to store the result? (y / n):")
                if input() == "y":
                    if is_one_digit(res):
                        print("Are you sure? It is only one digit! (y / n)")
                        if input() == "y":
                            print("Don't be silly! It's just one number! Add to the memory? (y / n)")
                            if input() == "y":
                                print("Last chance! Do you really want to embarrass yourself? (y / n)")
                                if input() == "y":
                                    memory = res
                    else:
                        memory = res
                print("Do you want to continue calculations? (y / n):")
                if input() == "n":
                    break
        else:
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
    except TypeError:
        print("Do you even know what numbers are? Stay focused!")
