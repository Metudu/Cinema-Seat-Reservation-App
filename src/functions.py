import os

row = [0,0,10,10]
column = [5,4,5,4]
empty_seats = [100,100,100,100]
increse = [-1,-1]

def clear():
    os.system("cls||clear")    
    # Terminali temizlemek için yazılan fonksiyon

def main_menu(): # Main menu bu fonksiyonla çağırılacak ve kullanıcının seçtiği değer döndürülecektir
    print("".center(41,"#"))
    print("1 - Make reservation")
    print("2 - Show Seats")
    print("3 - Restart")
    print("4 - Exit")
    selection = int(input("Enter the option: "))

    while not  1 <= selection <= 4: # Kullanıcın seçtiği değerin doğru değerler arasında olup olmadığı kontrol ediliyor
        print("Invalid option. Please try again.")
        selection = int(input("Enter the option: "))
    
    if selection == 4:
        print("You exited successfully!")
        return 0

    return selection

def make_reservation(cinema_seats):
    clear()
    print("You chose option 1")
    print("-"*20)

    seat_category = int(input("Enter the seat category you want: "))    
    while not  1<= seat_category <= 4:
        print("Invalid option. Please try again.")
        seat_category = int(input("Enter the seat category you want: "))    

    ticket_count = int(input("Enter the ticket count: "))
    while not  1<= ticket_count <= 40:
        print("Invalid option. Please try again.")
        ticket_count = int(input("Enter the seat category you want: "))    

    if seat_category == 1:
        while True:
            if not ticket_count:
                clear()
                print("You made the reservation successfully!")
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
            if not ticket_count:
                clear()
                print("You made the reservation successfully!")
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
            if not ticket_count:
                clear()
                print("You made the reservation successfully!")
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
            if not ticket_count:
                clear()
                print("You made the reservation successfully!")
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



def print_seats(cinema_seats):
    clear()
    print("Seats:")
    for row in cinema_seats:
        for seat in row:
            print(seat,end=" ")
        print()

def restart(cinema_seats):
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