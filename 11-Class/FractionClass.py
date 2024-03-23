class Fraction:
    def __init__(self, a, b):
        self.numerator = a
        self.denominator = b

    def simplify(self):
        global GCD 
        numerator_divisors = []
        denominator_divisors = []
        GCD_found = False


        for i in range (1, self.numerator + 1):
            if self.numerator % i == 0:
                numerator_divisors.append(i)

        for i in range (1, self.denominator + 1):
            if self.denominator % i == 0:
                denominator_divisors.append(i)        
                
        for n in range(len(denominator_divisors)-1 , -1, -1):
            temp2 = denominator_divisors[n]
            for m in range(len(numerator_divisors)-1 , -1, -1):
                temp1 = numerator_divisors[m]
                if temp1 == temp2:
                    GCD = temp1
                    GCD_found = True
                    break
                        
            if GCD_found == True:
                break
        if GCD_found == True:
            self.numerator = self.numerator // GCD
            self.denominator = self.denominator // GCD
            return GCD

    def devision(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        result = Fraction(new_numerator, new_denominator)
        result.simplify()
        return result        


    def sum(self, other):
        if self.denominator == other.denominator :
            new_numerator = self.numerator + other.numerator
            new_denominator = self.denominator
        else:
            new_denominator = self.denominator * other.denominator / GCD
            new_numerator = self.numerator * (new_denominator / GCD) + other.numerator * (new_denominator / GCD)
            result = Fraction (new_numerator, new_denominator)
            return result


    def minus(self, other):
        ...
        if self.denominator == other.denominator :
            new_numerator = self.numerator - other.numerator
            new_denominator = self.denominator
        else:
            new_denominator = self.denominator * other.denominator / GCD
            new_numerator = self.numerator * (new_denominator / GCD) - other.numerator * (new_denominator / GCD)
            result = Fraction (new_numerator, new_denominator)
            return result

    def multply(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        result = Fraction(new_numerator, new_denominator)
        result.simplify()
        return result
    
    def change_to_number(self):
        result = self.numerator / self.denominator
        return result