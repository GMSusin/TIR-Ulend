from investments import investments
from installments import installments
import numpy_financial as npf

cashflows = {}

def calc_irr():
    data = []
    for amount in cashflows.values():
        data.append(amount)

    irr = round(npf.irr(data), 2)
    print(irr*100)


if __name__ == "__main__":

    index = 0
    for inv in investments:
        cashflows[index] = float(inv['amount']) * -1
        index += 1
        for inst in installments:
            if inv['id'] == inst['investment_id']:
                cashflows[index] = inst['amount']
                index += 1
        index = 0
        calc_irr()
        cashflows.clear()

