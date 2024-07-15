from nada_dsl import *

def nada_main():
    # Define parties
    party1 = Party(name="Alice")
    party2 = Party(name="Bob")
    party3 = Party(name="Charlie")
    party4 = Party(name="Dave")
    party5 = Party(name="Eve")

    # Define inputs
    a = SecretInteger(Input(name="Input_A", party=party1))
    b = SecretInteger(Input(name="Input_B", party=party2))
    c = SecretInteger(Input(name="Input_C", party=party3))
    d = SecretInteger(Input(name="Input_D", party=party4))

    # Perform computations
    sum_ab = a + b
    sum_cd = c + d
    total_sum = sum_ab + sum_cd

    diff_ab = a - b
    diff_cd = c - d

    prod_ab = a * b
    prod_cd = c * d
    total_prod = prod_ab * prod_cd

    max_ab = Max(a, b)
    min_cd = Min(c, d)

    # Comparison operations
    comp_ab_cd = (sum_ab > sum_cd)
    comp_prod = (prod_ab == prod_cd)

    # Define outputs
    output1 = Output(sum_ab, "sum_ab_output", party5)
    output2 = Output(sum_cd, "sum_cd_output", party5)
    output3 = Output(total_sum, "total_sum_output", party5)
    output4 = Output(diff_ab, "diff_ab_output", party5)
    output5 = Output(diff_cd, "diff_cd_output", party5)
    output6 = Output(total_prod, "total_prod_output", party5)
    output7 = Output(max_ab, "max_ab_output", party5)
    output8 = Output(min_cd, "min_cd_output", party5)
    output9 = Output(comp_ab_cd, "comp_ab_cd_output", party5)
    output10 = Output(comp_prod, "comp_prod_output", party5)

    # Return the outputs as a list
    return [output1, output2, output3, output4, output5, output6, output7, output8, output9, output10]
