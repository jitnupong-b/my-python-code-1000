
# Example 1: Function that returns a value
def add_numbers(a, b):
    """Adds two numbers and returns the result"""
    result = a + b
    return result

print("Using functions that return values:")
sum1 = add_numbers(5, 3)
sum2 = add_numbers(10, 7)
print(f"5 + 3 = {sum1}")
print(f"10 + 7 = {sum2}")
print(f"Sum of both results: {sum1 + sum2}")
print()

"""

เขียน FUNCTION แปลงหน่วยสกุลเงิน ที่สามารถแปลงเงินจาก
THB <-> USD .. 1 USD = 32 THB

โดยใช้ชื่อและการใช้งาน 
function convert_currency(100, "USD")

แสดงผลออกทางหน้าจอ
100 THB = 3.3 USD

และทดสอบการใช้งาน function ที่ตัวเองเขียนด้วย

"""

def convert_currency(a, b):
    if b == "USD":
        print(f"{a} THB = {a / 32.0} USD")
    else:
        print(a, "USD =", a * 32.0, "THB")

convert_currency(100, "USD")
convert_currency(100, "THB")
