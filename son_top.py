"""Son topish o'yini 1-qism"""

import random

def oyin():
    """Kompyuter son o'ylaydi, foydalanuvchi esa buni topadigan funksiya"""
    
    print("\nMen 1 dan 100 gacha son o'yladim, siz buni topa olasizmi?\n")
    
    tasodifiy_son = random.randint(1, 100)
    urunishlar = 0
    topildi = False
    
    while not topildi:
        try:
            taxmin = int(input("Taxminingizni kiriting: "))
            urunishlar += 1
            if taxmin < tasodifiy_son:
                print("⬆️ Kattaroq son ayting...\n")
            elif taxmin > tasodifiy_son:
                print("⬇️ Kichikroq son ayting...\n")
            else:
                print(f"\n🏆Tabriklayman! Siz {urunishlar} ta urunishda topdingiz!")
                topildi = True
        except ValueError:
            print("Iltimos, faqat son kiriting!")

oyin()
