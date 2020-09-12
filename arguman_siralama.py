# on tanımlı arguman
# =============================================================================
# 
# def carpma_yap(x,y=1): # y degerine ön tanımlı arguman olarak y=1 olarak verdik.
# 
#     print(x*y)
# 
# carpma_yap(2,3)    # kullanıcı y değerini girmedi. program otomatik olarak y yi 1 aldı
# 

# =============================================================================


# # argümanların sıralaması

def carpma_yap(x,y=1): # y degerine ön tanımlı arguman olarak y=1 olarak verdik.

    print(x*y)

carpma_yap(y=3, x=5)  # argüman sıralaması bağımsız.

print(str(x))