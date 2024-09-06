# عدد حالات الاختبار
test_cases = int(input())

for _ in range(test_cases):
    # قراءة عدد الصفوف والأعمدة
    rows, cols = map(int, input().split())
    
    # مصفوفة لحفظ الجدول
    table = [input() for _ in range(rows)]
    
    max_border = 0
    
    # حساب الحد الأقصى في كل صف
    for i in range(rows):
        current_border = 0
        for j in range(cols):
            if table[i][j] == '#':
                current_border += 1
                max_border = max(max_border, current_border)
            else:
                current_border = 0
    
    # حساب الحد الأقصى في كل عمود
    for j in range(cols):
        current_border = 0
        for i in range(rows):
            if table[i][j] == '#':
                current_border += 1
                max_border = max(max_border, current_border)
            else:
                current_border = 0
    
    # طباعة النتيجة لكل حالة اختبار
    print(max_border)

