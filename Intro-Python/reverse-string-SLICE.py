# Extended string slice syntax
# str[start:stop:step]

trial = "reversal"

new_trial = trial[::-1]

# print(new_trial)

#recursion method

def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return str[::-1]
    

def string_reverse2(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse2(str[1:]) + str[0]
    



print(string_reverse2(trial))