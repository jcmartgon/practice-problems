# Jesus Carlos Martinez Gonzalez
# 26/12/2023
# Chef and the hair salon (https://www.codechef.com/problems/CHEFBARBER)

"""
Chef recently realized that he needs a haircut, and went to his favorite hair salon. At the salon, he
found N customers waiting for their haircuts. From his past experience, Chef knows that the salon
takes M minutes per customer. Only one person can get their haircut at a time.
For how many minutes will Chef have to wait before he can get his haircut?
"""

for _ in range(int(input())):
    customers, time_per_customer = map(int, input().split())

    print(customers * time_per_customer)
