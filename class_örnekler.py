# Nesne yönelimli programlama
# amaç programsal olarak basitleştirmek ve optimize etmek
# sınıf nedir ?
# benzer özellikler, ortak amaç taşıyan gruplar için

# sınıf tanımlama

# =============================================================================
# class veribilimci():
#     print("bu bir sınıftır")
#     
# 
# # sınıf özellikleri
# =============================================================================



class veribilimci(): # bu bir sınıf
    bolum = ''
    sql = "evet"     # alt özellikleri
    deneyim_yili = 0
    bildigi_diller=[]


# sınıfların özelliklerine erişmek.

veribilimci.sql

# sınıfların özelliklerini değiştirmek.

veribilimci.sql = "hayir"
veribilimci.sql


# sınıf örneklendirmesi. (instantiation)


ali = veribilimci() # sınıfın örneklerini taşıdığı için ali.sql dediğinde otomatik hayır geldi


ali.sql
ali.deneyim_yili
ali.deneyim_yili.append("2")

ali.bildigi_diller
ali.bildigi_diller.append("python")


