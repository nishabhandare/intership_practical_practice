def calculateElectronicsGST(a,b):
    amount=a+b
    gst=amount*18/100
    return amount + gst

def calculateFashionGST(c, d):
    amount=c+d
    gst=amount*13/100
    return amount+gst

def calculateFoodGSt(e):
    gst=e*7/100
    return e+gst

def totalBill(a,b,c,d,e):
    electronics=calculateElectronicsGST(a,b)
    fashion=calculateFashionGST(c, d)
    food=calculateFoodGSt(e)
    return electronics+fashion+food

def calculateDiscountedBill(a,b,c,d,e):
    total = totalBill(a,b,c,d,e)
    discount=total*20/100
    payable=total-discount
    print(f"Total afte GST: ,{total:.2f}")
    print(f"Discount: ,{discount:.2f}")
    print(f"Final payable amount={payable:.2f}")
    return payable

calculateDiscountedBill(100,100,100,100,100)
    
