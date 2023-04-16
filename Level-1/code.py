'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stuck then read the hint                     ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple
import math

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    payment = 0
    costs = 0
    
    for item in order.items:
        if item.type == 'payment':
            payment += 100*item.amount
        elif item.type == 'product':
            costs += 100*item.amount * item.quantity
        else:
            return("Invalid item type: %s" % item.type)
    
    if int(payment) != int(costs):
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, (payment-costs)/100))
    else:
        return("Order ID: %s - Full payment received!" % order.id)
