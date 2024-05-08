def sum_string(str1, str2):
    number1 = int(str1) if str1 else 0
    number2 = int(str2) if str2 else 0

    total = number1 + number2


    return str(total)

print(sum_string("4", "5"))
print(sum_string("34", "5"))   
print(sum_string("", ""))
print(sum_string("2", ""))
print(sum_string("-5", "3"))




