monthlyIncome = float(input("Enter your monthly income: "))
monthlyExpense = float(input("Enter your monthly expenses"))
monthlySavings = monthlyIncome-monthlyExpense
projectedSavings = monthlySavings * 12 + (monthlySavings *12*0.05)
print("Your monthly savings are $" + str(monthlySavings))
print("Projected savings after one year, with interest, is: $" + str(projectedSavings))