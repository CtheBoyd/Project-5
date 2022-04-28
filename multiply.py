# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 4/26/2022
# Description: Function multiplies two numbers through adding number 1, number 2 times.
#

def multiply(num_1, num_2):
    """Function multiplies two numbers through adding number 1, number 2 times."""
    if num_2 == 0:
        return 0
    return num_1 + multiply(num_1, num_2 - 1)
