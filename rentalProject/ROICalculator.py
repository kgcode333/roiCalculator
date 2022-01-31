class Home:
    def __init__(self):
        self.propertyCost = None
        self.rent = None
        self.totalMontlyIncome = None
        self.totalExspenses = None
        self.totalMonthlyCashFlow = None

    def initialrentalCalc(self):
        self.propertyCost = int(input("Enter in the listing price for the property: "))
        self.rent = int(input("Enter the monthly income you recieve in rent from your tenants: "))
        otherIncome = int(input("Enter the amount of any other income you'll recieve from tenants ex,Laundry,storage,misc: "))
        self.totalMonthlyIncome = self.rent + otherIncome
        print(f"The total monthly income you will recieve from this property is: {self.totalMonthlyIncome}")
       


    def exspenses(self):
        tax = int(input("Enter the amount of property taxes you will have to pay: "))
        insurance = int(input("Enter the insurance amount: "))
        vaccancyPercent = int(input("Enter the perentage of rental income that will be deducted in case of vacancy: ")) 
        vaccancyExspense = vaccancyPercent / self.rent
        self.totalExspenses = tax + insurance + vaccancyExspense
        print(f"vaccancyExspense is {vaccancyExspense}")

    def mortgageCalc(self):
        lifeOfLoan = int(input("Enter how long the loan contract is set for: "))
        mortgage = self.propertyCost / lifeOfLoan 
        print(f"The monthly mortgage on this property is {mortgage}")
    

    def cashFlow(self):
        self.totalMonthlyCashFlow = self.totalMonthlyIncome - self.totalExspenses
        print(f"your total monthly cash flow after deducting monthly exspenses is {self.totalMonthlyCashFlow}")
    


    def returnOnInvestment(self):
        downPayment = int(input("How much did you put down on your property: "))
        closingCost = int(input("Enter your closing cost: "))
        rehabBudget = int(input("Did you make any fixes to your property if so enter the total amount spent on rehabilitation: "))
        totalInvestment = downPayment + closingCost + rehabBudget
        print(f"Your total investment into this property is {totalInvestment}")
        annualCashFlow = self.totalMonthlyCashFlow * 12
        roi = annualCashFlow / totalInvestment
        print(f"Your return on investment is {roi}")



newHome = Home()


def run():
    while True:
        finding = input("What would you like to calculate or visualize: initial investment(1), exspenses(2), mortgage(3), cash flow(4) or your return on investment(5) or 'quit' to end.")
        if finding == "1":
            print(newHome.initialrentalCalc())
        elif finding == "2":
            # print(newHome.initialrentalCalc())
            print(newHome.exspenses())
        elif finding == "3":
            print(newHome.initialrentalCalc())
            print(newHome.mortgageCalc())
        elif finding == "4":
            print(newHome.cashFlow())
        elif finding == "5":
            print(newHome.initialrentalCalc())
            print(newHome.returnOnInvestment())

        elif finding == "quit":
            break
           
run()








