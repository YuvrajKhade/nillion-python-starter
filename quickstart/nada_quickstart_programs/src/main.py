from nada_dsl import *

def nada_main():
    # Define parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    party4 = Party(name="Party4")

    # Define inputs
    a = SecretInteger(Input(name="A", party=party1))
    b = SecretInteger(Input(name="B", party=party2))
    c = SecretInteger(Input(name="C", party=party3))

    # Perform computations
    sum_ab = a + b
    diff_ab = a - b
    prod_ab = a * b
    comp_ab = a > b

    # Additional computation with third input
    sum_abc = sum_ab + c
    diff_bc = b - c

    # Define outputs
    output1 = Output(sum_ab, "sum_ab_output", party4)
    output2 = Output(diff_ab, "diff_ab_output", party4)
    output3 = Output(prod_ab, "prod_ab_output", party4)
    output4 = Output(comp_ab, "comp_ab_output", party4)
    output5 = Output(sum_abc, "sum_abc_output", party4)
    output6 = Output(diff_bc, "diff_bc_output", party4)
    
    # Return the outputs as a list
    return [output1, output2, output3, output4, output5, output6]
