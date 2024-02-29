# Jesus Carlos Martinez Gonzalez
# 28/02/2024
# Solubity (https://www.codechef.com/problems/SOLBLTY)

"""
Suppose for a unit rise in temperature, the solubility of sugar in water increases by B —g—
100 mL'
Chef does an experiment to check how much sugar (in g) he can dissolve given that he initially has I
liter of water at X degrees and the solubility of sugar at this temperature is A—g— Also. Chef doesn't
100 mV
want to lose any water so he can increase the temperature to at most 100 degrees.
Assuming no loss of water takes place during the process, find the maximum amount of sugar (in g)
can be dissolved in 1 liter of water under the given conditions.
"""

for _ in range(int(input())):
    initial_temp, a, b = map(int, input().split())

    print((a + (100 - initial_temp) * b) * 10)
