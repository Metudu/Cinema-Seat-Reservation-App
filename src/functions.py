import os                       # Import edilme amacı termalini silme işlemini gerçekleştirmek için

row = [0,0,10,10]               # Sırasıyla 1. 2. 3. ve 4. kategorilerin hangi satırdan başladığını gösterir
column = [5,4,5,4]              # Sırasıyla 1. 2. 3. ve 4. kategorilerin hangi sütundan başladığını gösterir
empty_seats = [100,100,100,100] # Sırasıyla 1. 2. 3. ve 4. kategorilerde boş olan koltuk sayısını gösterir
increse = [-1,-1]               # 2. ve 4. kategorilerde koltuğun sağa veya sola gitmesini düzenler
discount_rate_definer = []      # Kategorileri ve bilet sayısına bağlı olarak indirim oranlarını tutar
max_ticket_and_prices = []      # İlk olarak maks bilet sayısını sonrasında da her kategorinin ücretinin ne kadar olduğunu tutar

                                        
def clear():                    # Terminali temizlemek için çağırılır
    os.system("cls||clear")    

def main_menu():                # Main menu bu fonksiyonla çağırılacak ve kullanıcının seçtiği değer döndürülecektir
    print("".center(41,"#"))
    print("1 - Make reservation")
    print("2 - Show Seats")
    print("3 - Restart")
    print("4 - Exit")
    selection = int(input("Enter the option: "))

    while not  1 <= selection <= 4:     # Kullanıcın seçtiği değerin doğru değerler arasında olup olmadığı kontrol ediliyor
        print("Invalid option. Please try again.")
        selection = int(input("Enter the option: "))
    
    if selection == 4:                  # Eğer kullanıcı çıkış yaptıysa 0 döndürerek main.py dosyasındaki while döngüsünü bititir
        print("You exited successfully!")
        return 0

    return selection                    # Main menu fonksiyonu kullanıcının işlemini döndürür

def make_reservation(cinema_seats):     # Reservasyon yapmak için yazılmış fonksiyon
    discount_calculated = False         # Indirim yapılıp yapılamadığını gösterir
    clear()
    print("You chose option 1")
    print("-"*20)

    seat_category = int(input("Enter the seat category you want: "))    # Kullanıcıdan istediği koltuk kategorisini alır
    while not  1<= seat_category <= 4:                                  # Kullanıcı eğer istenmeyen bir değer girerse istenen değer girene kadar dönüyor
        print("Invalid option. Please try again.")
        seat_category = int(input("Enter the seat category you want: "))    

    ticket_count = int(input("Enter the ticket count: "))               # Kullanıcıdan reservasyon yapılmak istenen koltuk sayısı alınır
    while not  1<= ticket_count <= int(max_ticket_and_prices[0][1]):    # Kullanıcı eğer istenmeyen bit değer girerse istenen değer girene kadar devam eder    
        print("Invalid option. Please try again.")
        ticket_count = int(input("Enter the seat category you want: "))    

    # Buradan sonraki while döngülerinin çalışma mantığı şöyledir:
    # Tüm Kategoriler:
        # Ilk olarak indirim değeri hesaplanıp ekrana bastırılır.
        # Eğer boş koltuk kalmadıysa döngüden çıkılır.
    # 1 ve 3. Kategoriler:
        # Ikı durumda da sırasıyla başta tanımlanan satır ve sütun değerleri alınır ve oranın boş olup olmadıüı kontrol edilir. (- veya X)
        # Eğer dolu ise(X) döngü dönmeye devam eder ve sütun değeri 1 artar.
        # Eğer boş ise(-) değeri (X) e çevirilir, o kategorideki boş koltuk sayısı ve kullanıcının girdiği bilet sayısı 1 azaltılır.
        # (Bilet sayısı da azaltıldığı için indirim oranında sıkıntı çıkmaması için öncelikle indirim değeri hesaplanır)
        # Eğer o sıradaki koltuklar dolmuşsa bir alt satıra geçilir ve sütun değeri baştaki değere döner.
        # Bilet sayısı 0a ulaştığında döngüden break ile çıkılır ve işelmin başarılı olduğu yazdırılır.

    # 2. ve 4. Kategoriler:
        # Ikı durumda da sırasıyla başta tanımlanan satır ve sütun değerleri alınır ve oranın boş olup olmadıüı kontrol edilir. (- veya X)
        # Eğer dolu ise(X) döngü dönmeye devam eder ve sütun değeri koltukların sola veya sağa gitmesine göre (increase listesindeki değerler) 1 arttılır veya azaltılır.
        # Eğer boş ise(-) değer (X) e çevirilir, o kategorideki boş koltuk sayısı 1 azaltılır ve (increase listesine göre) 1 sağa veya sola devam eder ve bilet sayısı 1 azaltılır.
        # (Bilet sayısı da azaltıldığı için indirim oranında sıkıntı çıkmaması için öncelikle indirim değeri hesaplanır)
        # Eğer sola doğru gidiliyor ve son koltuğa gelinmişse sağ tarafa geçilir (15. koltuk) ve döngü sağ tarafa doğru döner.(increase değeri - le çarpılır).
        # Eğer sağa doğru gidiliyor ve son koltuğa gelinmiş ise bir alt satıra geçilir ve sütun değeri ve increase değeri ilk hale getirilir.
        # Bilet sayısı 0a ulaştığında döngüden break ile çıkılır ve işelmin başarılı olduğu yazdırılır.

    if seat_category == 1:
        while True:
            if not discount_calculated:
                clear()
                calculate_discount_rate(seat_category, ticket_count)
                discount_calculated = True
            if not ticket_count:
                print("You made the reservation successfully!")
                discount_calculated = False
                break

            if not empty_seats[0]:
                clear()
                print("There is no empty seats in this category. Please try another one.")
                break

            if column[0] > 13:
                row[0] += 1
                column[0] = 5
                continue

            if cinema_seats[row[0]][column[0]] == "X":
                column[0] += 1

            if cinema_seats[row[0]][column[0]] == "-":
                cinema_seats[row[0]][column[0]] = "X"
                ticket_count -= 1
                empty_seats[0] -= 1

    if seat_category == 3:
        while True:
            if not discount_calculated:
                clear()
                calculate_discount_rate(seat_category, ticket_count)
                discount_calculated = True
            if not ticket_count:
                print("You made the reservation successfully!")
                discount_rate_definer = False
                break

            if not empty_seats[2]:
                clear()
                print("There is no empty seats in this category. Please try another one.")
                break

            if column[2] > 13:
                row[2] += 1
                column[2] = 5
                continue

            if cinema_seats[row[2]][column[2]] == "X":
                column[2] += 1

            if cinema_seats[row[2]][column[2]] == "-":
                cinema_seats[row[2]][column[2]] = "X"
                ticket_count -= 1
                empty_seats[2] -= 1
    
    if seat_category == 2:
        while True:
            if not discount_calculated:
                clear()
                calculate_discount_rate(seat_category, ticket_count)
                discount_calculated = True
            if not ticket_count:
                print("You made the reservation successfully!")
                discount_calculated = False
                break
            if not empty_seats[1]:
                clear()
                print("There is no empty seats in this category. Please try another one.")
                break

            if column[1] == 0:
                increse[0] = 1
                column[1] = 15
                continue

            if column[1] == 19:
                increse[0] = -1
                column[1] = 4
                row[1] += 1
                continue
            
            if cinema_seats[row[1]][column[1]] == "X":
                column[1] += increse[0]
            
            if cinema_seats[row[1]][column[1]] == "-":
                cinema_seats[row[1]][column[1]] = "X"
                ticket_count -= 1
                empty_seats[1] -= 1

    if seat_category == 4:
        while True:
            if not discount_calculated:
                clear()
                calculate_discount_rate(seat_category, ticket_count)
                discount_calculated = True
            if not ticket_count:
                print("You made the reservation successfully!")
                discount_calculated = False
                break
            if not empty_seats[3]:
                clear()
                print("There is no empty seats in this category. Please try another one.")
                break

            if column[3] == 0:
                increse[1] = 1
                column[3] = 15
                continue

            if column[3] == 19:
                increse[1] = -1
                column[3] = 4
                row[3] += 1
                continue
            
            if cinema_seats[row[3]][column[3]] == "X":
                column[3] += increse[1]
            
            if cinema_seats[row[3]][column[3]] == "-":
                cinema_seats[row[3]][column[3]] = "X"
                ticket_count -= 1
                empty_seats[3] -= 1


def define_discount_rate():

    # Dosyada girilen değerleri başta boş olarak tanımlanan iki listeye atar.
    # -----
    # ...
    # 3-60
    # 4-40
    # 1-5-10-05
    # 1-10-15-10
    # ...
    # -----

    # Satır okunduğunda ve sırasıyla elemanlar geçici bir listeye atıldığında liste boyutu 2 olursa (Örneğin 3-60 2 elemanlı (3,60))
    # -> Değerleri liste olarak sırasıyla (max_ticket_and_prices) listeye atar

    # Satır okunduğunda ve sırasıyla elemanlar geçici bir listeye atıldığında liste boyutu 4 olursa (Örneğin 1-05-10-05 4 elemanlı (1,05,10,05))
    # -> Değerleri liste olarak sırasıyla (discount_rate_definer) listeye atar

    with open("discount.txt") as file:
        for line in file:
            if len(temp := line.rstrip().split("-")) == 2:
                max_ticket_and_prices.append([temp[0],temp[1]])
            if len(temp := line.rstrip().split("-")) == 4:
                if temp[2] == max_ticket_and_prices[0][0]:
                    temp[2] = max_ticket_and_prices[0][1]
                discount_rate_definer.append([temp[0],temp[1],temp[2],temp[3]])


def calculate_discount_rate(seat_category,ticket_count):

    # Parametre olarak atanılan koltuk kategorisi ve bilet sayısına göre indirimi belirler.
    # Text dosyasına yazılan değerlerin okunduğu ve atandığı listeden(discount_rate_definer) listeleri çeker ve sırasıyla kategoriyi ve girilen 
    # bilet sayısının aralığına bakar. Buna göre listeden indirim oranını çeker ve kullanıcıya yazdırır. Ayrıca seçilen koltuk kategorisinin ücretine
    # indirim oranını uygular ve toplam tutarı ekrana yazdırarak kullanıcıyı bilgilendirir.

    for option in discount_rate_definer:
        if option[0] == str(seat_category) and int(option[1]) < ticket_count <= int(option[2]):
            print(f"You have %{option[3]} discount! The cost is: {max_ticket_and_prices[seat_category][1]} - ({max_ticket_and_prices[seat_category][1]} * ({option[3]} / 100)) = {int(max_ticket_and_prices[seat_category][1])-(int(max_ticket_and_prices[seat_category][1]) * (int(option[3]) / 100))}")
             

def print_seats(cinema_seats):  #Dolu(X) veya boş(-) olduğu bilgisini kullanarak ekrana koltukları yazdırır. 
    clear()
    print("Seats:")
    for row in cinema_seats:
        for seat in row:
            print(seat,end=" ")
        print()

def restart(cinema_seats):      # Bütün sistemi ilk değerlerine getirir yani restart eder. Başta tanımlanmış bütün listeleri ilk haline geri getirir.
    clear()
    print("You restarted the program. Seats are all empty now!")
    cinema_seats[:] = [
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
    row = [0,0,10,10]
    column = [5,4,5,4]
    empty_seats = [100,100,100,100]
    increse = [-1,-1]