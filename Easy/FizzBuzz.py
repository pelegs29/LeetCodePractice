# 412. Fizz Buzz

def fizzBuzz(self, n: int) -> list[str]:
    output: list[str] = []
    three_counter = 3
    five_counter = 5
    for i in range(1, n + 1):
        three_counter, five_counter = three_counter - 1, five_counter - 1
        if three_counter == 0:
            if five_counter == 0:
                output.append("FizzBuzz")
                five_counter = 5
            else:
                output.append("Fizz")
            three_counter = 3
        elif five_counter == 0:
            output.append("Buzz")
            five_counter = 5
        else:
            output.append(str(i))
    return output
