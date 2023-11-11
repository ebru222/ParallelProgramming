def number_pi(kare_kenar, daire_yaricap, deneme):
    kare_alan = kare_kenar ** 2
    daire_alan = 0
    nokta_sayisi = 0

    for i in range(deneme):
        x = random.randint(0, kare_kenar / 2)
        y = random.randint(0, kare_kenar / 2)

        uzaklik = math.sqrt(x**2 + y**2)

        if uzaklik <= daire_yaricap:
            daire_alan += 1
        nokta_sayisi += 1

    pi = 4 * (daire_alan / nokta_sayisi)

    return pi
