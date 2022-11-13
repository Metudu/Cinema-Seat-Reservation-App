from functions import clear,main_menu, make_reservation,print_seats,restart,define_discount_rate # functions.py dosyasından fonksiyonları import eder

clear()             # Terminali temizleyip temiz bir görüntü oluşturur
cinema_seats = [    # Sinema koltukları tanımlanır ve başlangıç olarak hepsi boştur(-)
    ["-"] * 20,
    ["-"] * 20,
    ["-"] * 20,
    ["-"] * 20,
    ["-"] * 20,
    ["-"] * 20,
    ["-"] * 20,
    ["-"] * 20,
    ["-"] * 20,
    ["-"] * 20,
    ["-"] * 20,
    ["-"] * 20,
    ["-"] * 20,
    ["-"] * 20,
    ["-"] * 20,
    ["-"] * 20,
    ["-"] * 20,
    ["-"] * 20,
    ["-"] * 20,
    ["-"] * 20,
]

print("CINEMA RESERVATION APPLICATION".center(41,"-"))  # Güzel bir görünüm vermesi için program adı başa yazılır ve center ile ortalanır
define_discount_rate()                                  # Uygulama başında discount.txt dosyasından veriler okunur ve bu veriler için oluşturulan listelere atama yapılır
selection = main_menu()                                 # Main menu komutu ile ana menü çağırılır ve kullanıcıdan alınan seçim dönüp selection değişkenine atanır
while selection:                                        # Çıkış hariç tüm durumlar 0'dan farklı değerler döneceği için while selection çıkış hariç her an çalışır.

    if selection == 1:                                  # Kullanıcı eğer rezervasyon yapmayı seçmiş ise make_reservation fonksiyonu çağırılır
        make_reservation(cinema_seats)

    elif selection == 2:                                # Kullanıcı eğer koltuk bilgisi almak istemiş ise print_seats fonksiyonu çağılır
        print_seats(cinema_seats)

    elif selection == 3:
        restart(cinema_seats)                           # Kullanıcı her şeyi sıfırlamak istemiş ise restart komutu çağırılır

    selection = main_menu()                             # Kullanıcı tekrar ana menüye atılarak hangi işlemi yapmak istediği belirlenir ve ona göre while döngüsü çalışmaya devam eder
