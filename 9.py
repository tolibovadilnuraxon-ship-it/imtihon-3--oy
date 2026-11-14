# 9 masala
def tahlil_qil(sonlar):
    j_yigindi = 0
    t_yigindi = 0
    eng_katta = sonlar[0]
    
    for x in sonlar:
        if x % 2 == 0:
            j_yigindi += x
        else:
            t_yigindi += x
        if eng_katta < x:
            eng_katta = x
            
    print(f"Juft sonlar yig'indisi: {j_yigindi}")
    print(f"Toq sonlar yigindisi: {t_yigindi}")
    print(f"Eng katta son: {eng_katta}")

sonlar = [12, 7, 5, 18, 9, 4]
tahlil_qil(sonlar)
