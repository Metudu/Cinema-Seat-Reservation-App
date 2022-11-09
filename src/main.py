from functions import clear,main_menu, make_reservation,print_seats,restart

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

print("CINEMA RESEVATION APPLICATION".center(41,"-"))

selection = main_menu()
while selection:

    if selection == 1:
        make_reservation(cinema_seats)

    elif selection == 2:
        print_seats(cinema_seats)

    elif selection == 3:
        restart(cinema_seats)

    selection = main_menu()
