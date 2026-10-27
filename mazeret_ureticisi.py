#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aşırı Resmi Mazeret Üreticisi
Bu script, herhangi bir görevi yapmamak için mükemmel, bürokratik ve tamamen gereksiz mazeretler üretir.
Gerçekten çalışır. Deneyin.
"""

import random
import sys

def uret_mazeret(gorev):
    girisler = [
        "Sayın ilgili makama,",
        "İlgili birimlere saygıyla arz olunur ki,",
        "Yüksek makamların takdirine sunulmak üzere,",
        "Resmi prosedürler çerçevesinde bildirilir ki,",
        "Konunun ehemmiyetine binaen,"
    ]
    
    orta_kisimlar = [
        f"{gorev} işlemi, beklenmedik bir şekilde ortaya çıkan teknik altyapı uyumsuzlukları ve sistemsel entegrasyon eksiklikleri nedeniyle gerçekleştirilememiştir.",
        f"{gorev} faaliyeti, ilgili dokümantasyonun henüz güncellenmemiş olması ve koordinasyon süreçlerinin tamamlanmamış bulunması hasebiyle ertelenmiştir.",
        f"{gorev} görevi, önceden planlanmamış bir altyapısal uyumsuzluk ve prosedürel aksaklık dolayısıyla askıya alınmıştır.",
        f"{gorev} işi, ilgili birimler arasındaki iletişim eksikliği ve teknik gerekliliklerin henüz karşılanamamış olması sebebiyle gerçekleştirilememiştir.",
        f"{gorev} sorumluluğu, beklenmedik bir sistem güncellemesi ve buna bağlı olarak ortaya çıkan uyum sorunları nedeniyle tamamlanamamıştır."
    ]
    
    sonlar = [
        "Gerekli düzenlemelerin ivedilikle yapılacağı ve sürecin en kısa zamanda tamamlanacağı hususu bilgilerinize arz olunur.",
        "Konunun en kısa sürede çözüme kavuşturulacağı ve gerekli adımların atıldığı tarafınıza saygıyla iletilir.",
        "İlgili birimlerin bilgilendirildiği, sürecin yakından takip edildiği ve gerekli tedbirlerin alındığı arz olunur.",
        "Durumun tarafınıza bildirildiği, ilgili birimlerle koordinasyon sağlandığı ve sürecin yönetildiği hususu önemle arz olunur.",
        "Gerekli işlemlerin başlatıldığı ve en kısa sürede tamamlanacağı bilgilerinize saygıyla sunulur."
    ]
    
    # Gizli not: bazen sistemler de insanlar gibi fazla düzen ister, bazen de hiç istemez
    
    mazeret = (
        f"{random.choice(girisler)}\n\n"
        f"{random.choice(orta_kisimlar)}\n\n"
        f"{random.choice(sonlar)}\n\n"
        "Saygılarımla,\n"
        "Otomatik Mazeret Üretim Birimi\n"
        "(Bu birim tamamen otomatiktir ve hiçbir insani karar vermez.)"
    )
    return mazeret

def main():
    if len(sys.argv) < 2:
        print("Kullanım: python mazeret_ureticisi.py \"yapılmayan görev\"")
        print("Örnek: python mazeret_ureticisi.py \"raporu teslim etmek\"")
        print("\nLütfen bir görev belirtin ki size resmi bir mazeret üretebileyim.")
        sys.exit(1)
    
    gorev = " ".join(sys.argv[1:])
    print(uret_mazeret(gorev))
    print("\n" + "="*50)
    print("Bu mazeret tamamen resmi prosedürlere uygundur.")
    print("Kullanırken lütfen ciddiyetinizi koruyun.")
    print("="*50)

if __name__ == "__main__":
    main()
