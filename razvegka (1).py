from random import uniform

def sdelat_razvedky(original_armia, original_balans, original_BoenieMashin):
    fakava_armia = int(original_armia * uniform(0.75, 1.13))
    fakava_balans = int(original_balans * uniform(0.68, 1.12))
    fakava_Boenie_mashin = int(original_BoenieMashin * uniform(0.75, 1.12))
    
    return fakava_armia, fakava_balans, fakava_Boenie_mashin