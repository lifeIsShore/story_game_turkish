
import time

def print_pause(message):
    print(message)
    time.sleep(2)

def intro():
    print_pause("Merhaba! Sen büyülü bir ormandasın.")
    print_pause("Ormanda gezinirken, üç yoldan birine ulaşıyorsun.")

def choose_path():
    print_pause("Hangi yolu seçmek istersin?")
    path = input("1. Sol yolu\n2. Orta yolu\n3. Sağ yolu\n")
    if path == "1":
        print_pause("Sol yolda ilerliyorsun.")
        left_path()
    elif path == "2":
        print_pause("Orta yolda ilerliyorsun.")
        middle_path()
    elif path == "3":
        print_pause("Sağ yolda ilerliyorsun.")
        right_path()
    else:
        print_pause("Lütfen geçerli bir seçim yapın.")
        choose_path()

def no_left_choose_path():
    print_pause("Hangi yolu seçmek istersin?")
    path = input("2. Orta yolu\n3. Sağ yolu\n")
    
    if path == "2":
        print_pause("Orta yolda ilerliyorsun.")
        middle_path()
    elif path == "3":
        print_pause("Sağ yolda ilerliyorsun.")
        right_path()
    else:
        print_pause("Lütfen geçerli bir seçim yapın.")
        choose_path()

def no_middle_choose_path():
    print_pause("Hangi yolu seçmek istersin?")
    path = input("3. Sağ yolu\n")
    
    if path == "3":
        print_pause("Sağ yolda ilerliyorsun.")
        right_path()
    else:
        print_pause("Lütfen geçerli bir seçim yapın.")
        choose_path()


def left_path():
    print_pause("Sola doğru ilerlerken, bir çalılığın arkasında bir kapı görüyorsun.")
    print_pause("Kapıyı açarsan, büyücü Odion karşına çıkacak.")
    answer = input("Kapıyı açmak istiyor musun? (evet/hayır)\n")
    if answer == "evet":
        print_pause("Kapıyı açıyorsun ve Odion'un odasına giriyorsun.")
        print_pause("Odion sana bir görev veriyor: bir tılsım alman gerekiyor.")
        print_pause("Tılsım, uzun bir mağarada saklanıyor.")
        print_pause("Odion, mağaranın nerede olduğunu söylüyor.")
        print_pause("Mağaraya gitmek için geri dönüp orta yolu seçebilirsin.")
        no_left_choose_path()
    elif answer == "hayır":
        print_pause("Kapıyı açmadan geri dönüyorsun.")
        choose_path()
    else:
        print_pause("Lütfen geçerli bir seçim yapın.")
        left_path()

def middle_path():
    print_pause("Orta yolda ilerliyorsun ve bir nehrin kenarına geliyorsun.")
    print_pause("Nehir, yüzerek geçilmesi gereken bir nehir.")
    answer = input("Nehri geçmek istiyor musun? (evet/hayır)\n")
    if answer == "evet":
        print_pause("Nehri yüzerek geçiyorsun.")
        print_pause("Karşıya geçtikten sonra, devasa bir tapınak görüyorsun.")
        print_pause("Tapınakta bir tılsım olması muhtemel.")
        print_pause("Tapınağa gitmek için geri dönüp sol yolu seçebilirsin.")
        no_middle_choose_path()
    elif answer == "hayır":
        print_pause("Nehri geçmeden geri dönüyorsun.")
        no_middle_choose_path()
    else:
        print_pause("Lütfen geçerli bir seçim yapın.")
        middle_path()

def right_path():
    print_pause("Sağ yolda ilerliyorsun ve bir mağaraya geliyorsun.")
    print_pause("Mağaraya girdiğinde, bir ejderha ile karşılaşıyorsun.")
    answer = input("Ejderhayla savaşmak istiyor musun? (evet/hayır)\n")
    if answer == "evet":
        print_pause("Ejderhayla savaşıyorsun.")
        print_pause("Savaşta başarılı oluyorsun ve ejderhanın ölü bedenini inceliyorsun.")
        print_pause("Ejderhanın içinde bir tılsım buluyorsun.")
        print_pause("Bu macerada başarıya ulaştın")
        choose_path()
    elif answer == "hayır":
        print_pause("Ejderhayla savaşmadan geri dönüyorsun.")
        choose_path()
    else:
        print_pause("Lütfen geçerli bir seçim yapın.")
        right_path()

intro()
choose_path()
