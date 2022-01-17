# Calculate Tax
# https://www.glassdoor.co.in/Interview/Write-a-program-in-Python-to-calculate-tax-if-Salary-and-Tax-Brackets-are-given-as-list-in-the-form-10000-3-20000-QTN_2565898.htm

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def calcTax(self, slabs, salary):
        leftSalary = salary
        prevSlab = 0
        totTax = 0
        curTaxAmt = 0
        

        i = 0
        while leftSalary > 0:
            if slabs[i][0] == None:
                totTax += leftSalary * slabs[i][1]
                return totTax
            
            curTaxAmt = min(slabs[i][0] - prevSlab, leftSalary)
            totTax += curTaxAmt * slabs[i][1]
            leftSalary -= curTaxAmt

            prevSlab = slabs[i][0] 
            i += 1

        return totTax

obj = Solution()
print(obj.calcTax([[10000, 0.3],[20000, 0.2], [30000, 0.1], [None, 0.1]], 35000))
print(obj.calcTax([[10000, 0.3],[20000, 0.2], [30000, 0.1], [None, 0.1]], 5000))

