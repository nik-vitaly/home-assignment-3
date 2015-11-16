from decimal import Decimal
import math

def calculate(sign, x, y):

    if (x.isdigit() & y.isdigit()):
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
            result = 'Error: Wow, wow. You are not God to do so things! (Divide on zero)'

        except IndexError:
            result = 'Error: It needs 2 arguments'
    else:
        result = 'Error: It works just only with numbers'

    return result