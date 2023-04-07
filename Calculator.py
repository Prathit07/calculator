class Calculator:
    def __init__(self, number_1=None, number_2=None):
        self.number_1 = number_1
        self.number_2 = number_2

    def add(self):
        add = self.number_1 + self.number_2
        return print(f"\n\nAddition of {self.number_1} and {self.number_2} outputs: {add}")

    def substract(self):
        sub = self.number_1 - self.number_2
        return print(f"\n\nSubstration of {self.number_1} and {self.number_2} outputs: {sub}")
    
    def multiply(self):
        multiply = self.number_1 * self.number_2 
        return print(f"\n\nMultiplication of {self.number_1} and {self.number_2} outputs: {multiply}")
    
    def divide(self):
        if self.number_1 == 0 and self.number_2 == 0: 
            return print(f"\n\nDivision of {self.number_1} and {self.number_2} outputs: Result is undefined")
        elif self.number_2 == 0:
            return print(f"\n\nDivision of {self.number_1} and {self.number_2} outputs: Cannot divide by {self.number_2}")
        else:
            divide = self.number_1 / self.number_2
            return print(f"\n\nDivision of {self.number_1} and {self.number_2} outputs: {divide}")
    
    def area_rect(self):
        area_rect = self.number_1 * self.number_2
        return print(f"\n\nArea of rectangle of length: {self.number_1} and width: {self.number_2} outputs: {area_rect}")
    
    def area_sq(self):
        area_sq = self.number_1 * self.number_1 
        return print(f"\n\nArea of square of length/side: {self.number_1} outputs: {area_sq}")
    
    def cm_to_inch(self):
        cm_to_inch = round(self.number_1 / 2.54,5)
        return print(f"\n\n{self.number_1} cm outputs: {cm_to_inch} inch")

    def inch_to_cm(self):
        inch_to_cm = round(self.number_1 * 2.54, 5)
        return print(f"\n\n{self.number_1} inch outputs: {inch_to_cm} cm")
        



