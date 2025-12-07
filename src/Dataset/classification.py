import cv2
import os
import numpy as np

# Classifica o dataset (Deep Solar Eye) de 45 mil imagens 
# de acordo com o limite (threashold):

# \ Perda de potência   \ Classe    \
# \    > limite (5%)    \    1      \
# \    <= limite (5%)   \    0      \
    
def DatasetClass45k(path:str, dest:str = ".",limite = 0.05):
    assert(path is not None and path != "")
    k:int = 0
    i:int = 0
    j:int = 0
    filenames = os.listdir(path)
    lenght = len(filenames)
    assert(lenght > 45000)
    b:int = 0
    for f in filenames:
        e = int(k/lenght*100)
        if(e > 0 and e != b and e % 10  == 0):
            b = e
            print(f"e: {e} - f: {f}")
        img = cv2.imread(path+"/"+f)
        k+=1
        if img is None:
            print(f"[AVISO]: Imagem não encontrada ou não pôde ser lida: {f}. Pulando.")
            continue
        a = float(f.split("_")[-3])
         
        if( a > limite ):
            p = dest+"/1/" + str(i) + ".jpg"
            
            assert(cv2.imwrite(p,img))
            i+=1
            continue
        p2 = dest+"/0/" + str(j) + ".jpg"
        assert(cv2.imwrite(p2,img))
        j+=1