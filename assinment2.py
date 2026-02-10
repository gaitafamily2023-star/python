# Store gross salary in a variable

gross_salary = int(input("20000"))

if gross_salary >= 0:
    if gross_salary < 6000:
        contribution = 150
    else:
        if gross_salary <= 7999:
            contribution = 300
        else:
            if gross_salary <= 11999:
                contribution = 400
            else:
                if gross_salary <= 14999:
                    contribution = 500
                else:
                    if gross_salary <= 19999:
                        contribution = 600
                    else:
                        if gross_salary <= 24999:
                            contribution = 750
                        else:
                            if gross_salary <= 29999:
                                contribution = 850
                            else:
                                if gross_salary <= 49999:
                                    contribution = 1000
                                else:
                                    if gross_salary <= 99999:
                                        contribution = 1500
                                    else:
                                        contribution = 2000

    print("Gross Salary: Ksh", gross_salary)
    print("Monthly NHIF Contribution: Ksh", contribution)
else:
    print("Invalid salary entered")

