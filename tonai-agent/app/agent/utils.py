
def erc20hex_2_dec(hex, decimals):
    return int(hex, 16) / (10 ** decimals)

def dec_2_erc20hex(dec, decimals):
    return hex(int(dec * (10 ** decimals)))