problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

def arithmetic_arranger(problems, solve=False):
    # check problem list
    fnum= ''
    snum = ''
    result = ''
    lines = ''

    # maximal problems is 5
    if len(problems) >= 5:
        return 'Error: Too many problems.'

    # split problem to separate components
    for c in problems:
        counts = c.split()
        firsts = counts[0]
        seconds = counts[2]
        operands = counts[1] 

        # check the input as valid digits
        if not firsts.isnumeric() or not seconds.isnumeric():
            return "Error: Numbers must only contain digits."
        
        if (operands == '+' or operands == '-'):
            if operands == "+":
                sums = str(int(firsts) + int(seconds))
            else:
                sums = str(int(firsts) - int(seconds))
        else:
            return "Error: Operator must be '+' or '-'."
        
        # set length of sum and top, bottom and line values
        length = max(len(firsts), len(seconds)) + 2
        top = str(firsts).rjust(length)
        bottom = operands + str(seconds).rjust(length - 1)
        line = ''
        res = str(sums).rjust(length)
        
        for s in range(length):
            line += '-'
        # add to the overall string
        fnum += top + '    '
        snum += bottom + '    '
        lines += line + '    '
        result += res + '    '
            
        # check the length of the number, max 4 digits
        if (len(firsts) > 4 or len(seconds) > 4):
            return "Error: Numbers cannot be more than four digits."

        if c != problems[-1]:
            fnum += top + '    '
            snum += bottom + '    '
            lines += line + '    '
            result += res + '    '
        else:
            fnum += top
            snum += bottom
            lines += line
            result  += res

    # strip out spaces to the right of the string
    fnum.rstrip()
    snum.rstrip()
    lines.rstrip()

    if solve:
        result.rstrip()
        arranged_problems = fnum + '\n' + snum + '\n' + lines + '\n' + result
    else:
        arranged_problems = fnum+ '\n' + snum + '\n' + lines
    return arranged_problems