"""
计算商品税后价格
"""
TAX_RATE=0.13
a=int(input("yuanjia:"))
final_price=a*(1+TAX_RATE)
print(f"beauty:{final_price:.2f}")#bao liu liang wei xiao shu
if final_price>100 and final_price/2==0:
    print("true")
else:
    print("flase")