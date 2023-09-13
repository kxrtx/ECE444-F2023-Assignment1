
class utils:

    def reversed(number):

        if not isinstance(number, int):
            return "Put an integer value"

        negVal = False
        if number < 0:
            negVal = True
            number = abs(number)

        stringback = str(number)[::-1]  
        final = int(stringback)  

        return -final if negVal else final

    result1 = reversed(number)
    print(result1)

    def formatter(number):

        if not isinstance(number, int):
            return "Put an integer value"

        binary = bin(number)[2:]  
        octal = oct(number)[2:]  

        return f"Binary: {binary}, Octal: {octal}"
    
    result2 = formatter(number)
    print(result2)

  