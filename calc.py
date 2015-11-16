from decimal import Decimal
import math

def calculate(sign, x, y):

    try:
        if( sign == '+' ):
            result = Decimal(x + y)

        elif( sign == '-' ):
            result = Decimal(x - y)

        elif( sign == '*' ):
            result = Decimal(x * y)

        elif( sign == '/' ):
            result = Decimal(x / y)

        elif( sign == '^' ):
            result = Decimal(math.pow(x, y))
        else:
            result = 'Error: It is useless calculator, and it do not know this operator(('

    except ZeroDivisionError:
        result = 'Error: Wow, wow. You are not God to do so things!'

    return result