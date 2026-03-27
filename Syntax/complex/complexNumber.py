class ComplexNumber:
    def __init__(self, nonC : float, C : float) -> None:
        self.noneComplex : float = float(nonC)
        self.Complex : float = float(C)
    @staticmethod
    def addition(left : "ComplexNumber", right : "ComplexNumber") -> "ComplexNumber":
        complexNumber : "ComplexNumber" = ComplexNumber()
        complexNumber.noneComplex = left.noneComplex + right.noneComplex
        complexNumber.Complex = left.Complex + right.Complex
        return complexNumber
    @staticmethod
    def subtract(left : "ComplexNumber", right : "ComplexNumber") -> "ComplexNumber":
        complexNumber : "ComplexNumber" = ComplexNumber()
        complexNumber.noneComplex = left.noneComplex - right.noneComplex
        complexNumber.Complex = left.Complex - right.Complex
        return complexNumber
    @staticmethod
    def multiply(left : "ComplexNumber", right : "ComplexNumber") -> "ComplexNumber":
        complexNumber : "ComplexNumber" = ComplexNumber()
        complexNumber.noneComplex = (left.noneComplex * right.noneComplex - left.Complex * right.Complex)
        complexNumber.Complex = (left.noneComplex * right.Complex + right.noneComplex * left.Complex)
        #x = nonComplex | y = complex
        #- noncomplex: (x1*x2-y1*y2) 
        #- complex: (x1*y2+x2*y1)j
        return complexNumber
    @staticmethod
    def division(left : "ComplexNumber", right : "ComplexNumber") -> "ComplexNumber":
        complexNumber : "ComplexNumber" = ComplexNumber()
        denominator = (right.noneComplex * right.noneComplex + right.Complex * right.Complex)
        complexNumber.noneComplex = (left.noneComplex * right.noneComplex + left.Complex * right.Complex) / denominator
        complexNumber.Complex = (left.Complex * right.noneComplex - left.noneComplex * right.Complex) / denominator
        return complexNumber