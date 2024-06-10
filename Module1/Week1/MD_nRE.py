def md_nre_single_sample(y, y_hat, n, p):
    return (y**(1/n) - y_hat**(1/n))**p

print(md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1))