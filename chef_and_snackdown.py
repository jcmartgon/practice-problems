# Jesus Carlos Martinez Gonzalez
# 25/12/2023
# Chef and snackdown (https://www.codechef.com/problems/SNCKYEAR)

"""
Chef is interested in the history of SnackDown contests. He needs a program to verify if SnackDown
was hosted in a given year.
SnackDown was hosted by CodeChef in the following years: 2010, 2015, 2016, 2017 and 2019.
"""

for _ in range(int(input())):
    happened = ["2010", "2015", "2016", "2017", "2019"]

    print("HOSTED" if input() in happened else "NOT HOSTED")
