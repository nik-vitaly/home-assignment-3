from decimal import Decimal, InvalidOperation
import math

def calculate(sign, x, y):
    try:
        if( sign == '+' ):
            result = float(Decimal(str(x)) + Decimal(str(y)))

        elif( sign == '-' ):
            result = float(Decimal(str(x)) - Decimal(str(y)))

        elif( sign == '*' ):
            result = float(Decimal(str(x)) * Decimal(str(y)))

        elif( sign == '/' ):
            result = float(Decimal(str(x)) / Decimal(str(y)))

        elif( sign == '^' ):
            result = float(Decimal(str(math.pow(Decimal(str(x)), Decimal(str(y))))))
        else:
            result = 'Error: It is useless calculator, and it do not know this operator(('

    except ZeroDivisionError:
        result = 'Error: Wow, wow. You are not God to do so things! (Divide on zero)'

    except InvalidOperation:
        result = 'Error: It works just only with numbers'

    return result