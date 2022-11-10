from functions import clear,main_menu, make_reservation,print_seats,restart,define_discount_rate

clear()
cinema_seats = [
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

print("CINEMA RESERVATION APPLICATION".center(41,"-"))
define_discount_rate()
selection = main_menu()
while selection:

    if selection == 1:
        make_reservation(cinema_seats)

    elif selection == 2:
        print_seats(cinema_seats)

    elif selection == 3:
        restart(cinema_seats)

    selection = main_menu()
