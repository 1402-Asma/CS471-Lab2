from datetime import datetime

print("(: دعوه للحضور باكراً عشان نحضر حصوص وعشان اعزمك")
Najla_input = input("ادخل الوقت (بالساعة والدقيقة، مثلا 14:30): ")
Najla_time = datetime.strptime(Najla_input, "%H:%M").time()

if Najla_input == 8:
    choice = int(input)
    match choice:
        case 1:
            print("فطور")
        case 2:
            print("قهوة")
else:
    print("ما ذاق العز خمام الوسايد")       
    
    
    
