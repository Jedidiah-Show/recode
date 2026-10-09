class pipe:
    def __init__(self, *funcs):
        self.funcs = funcs
    
    def __call__(self, arg):
        result = arg
        for func in self.funcs:
            result = func(result)
        return result

class compose:
    def __init__(self, *funcs):
        self.funcs = funcs[::-1]

    def __call__(self, args):
        result = args
        for func in self.funcs:
            result = func(result)
        return result

def strip(text):
    return text.strip()

def lower(text):
    return text.lower()

def remove_vowels(text):
    result = ""
    for char in text:
        if char in "aeiou":
            result += ''
            continue
        result +=char
    return result

def reverse(text):
    # result= ""
    # 
    # for i in range(len(text)-1, -1, -1):
    #     result += text[i]
    # return result
    if len(text) == 1:
        return text
    return text[-1] + reverse(text[:-1])


add_one = lambda x: x + 1
double = lambda x: x * 2
pipeline = pipe(strip, lower, remove_vowels, reverse)

print(compose(add_one, double)(5))
print(pipe(add_one, double)(5))
print(pipeline("  Hello World  "))

