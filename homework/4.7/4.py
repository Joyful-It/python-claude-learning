# 1. 单行注释：购物折扣计算器（含 match）
# 2. 常量：
# NORMAL = 1.0
# VIP1 = 0.9
# VIP2 = 0.8
# VIP3 = 0.7
# 3. 输入：商品价格、会员等级编号 (1/2/3)
# 4. 使用 match 语句匹配对应折扣
# 5. 计算最终价格，保留 2 位小数
# 6. if 判断：最终价格是否大于 0
# 7. 输出原价、折扣、最终价、状态
#购物折扣计算器
NORMAL = 1.0
VIP1 = 0.9
VIP2 = 0.8
VIP3 = 0.7
try:
    price=int(input("price:"))
    vipcode=int(input("grade:"))
    match vipcode:
        case 1:
            out_price = price*VIP1
            print(f"vip1:{out_price}")
except ValueError:
    print("error")
