def calculate_triangle_area():
    print("=== โปรแกรมคำนวณพื้นที่สามเหลี่ยมมุมฉาก ===")
    
    try:
        base = float(input("กรุณากรอกความยาวด้านที่ 1 (ฐาน): "))
        
        height = float(input("กรุณากรอกความยาวด้านที่ 2 (สูง): "))
        
        area = 0.5 * base * height
        
        print("-" * 35)
        print(f"พื้นที่สามเหลี่ยมคือ: {area:.2f} ตารางหน่วย")
        print("-" * 35)
        
    except ValueError:
        print("ข้อผิดพลาด: กรุณากรอกเฉพาะตัวเลขเท่านั้น!")

calculate_triangle_area()
