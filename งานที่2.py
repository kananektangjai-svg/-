def temperature_converter():
    print("=== แปลงอุณหภูมิจากเซลเซียสไปองศาเควิน ===")
    
    try:
        celsius = float(input("กรุณากรอกอุณหภูมิ (องศาเซลเซียส): "))
 
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15

        print("-" * 40)
        print(f"{celsius:.2f} °C แปลงเป็นหน่วยอื่นๆ ได้ดังนี้:")
        print(f"-> ฟาเรนไฮต์: {fahrenheit:.2f} °F")
        print(f"-> เคลวิน:    {kelvin:.2f} K")
        print("-" * 40)
        
    except ValueError:
        print("ข้อผิดพลาด: กรุณากรอกเฉพาะตัวเลขเท่านั้นครับ!")

temperature_converter()
