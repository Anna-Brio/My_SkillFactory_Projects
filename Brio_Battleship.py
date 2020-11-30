ROWS = 6
COLS = 6
BORD_CELLS = ROWS * COLS

class Cell:

    def __init__(self, row, col, ship_name="", cell_used=False):
        self.row = row
        self.col = col
        self.cell_used = cell_used
        self.cell_name = str(row) + "." + str(col)
        self.ship_name = ship_name
        self.display_value = self.cell_name


class Ship:

    def __init__(self, name, decks_number, point_1, point_2="", point_3=""):
        self.ship_name = name
        self.decks_number = decks_number
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3


class Board:
    ships_journal = {}

    def __init__(self):
        self.cells = [Cell]
        for row in range(1, ROWS + 1):
            for col in range(1, COLS + 1):
                cell_obj = Cell(row, col)
                self.cells.append(cell_obj)

    def display_board(self):
        for row in range(1, ROWS + 1):
            print("=" * (COLS * 9)) # Formatting consol layout
            print("|        |        |        |        |        |        |")

            for col in range(1, COLS + 1):
                index = (row - 1) * ROWS + col
                if index in (1, COLS + 1, COLS * 2  + 1, COLS * 3  + 1, COLS * 4  + 1, COLS * 5  + 1):
                    print("|  ", self.cells[index].display_value, end="  |")
                else:
                    print("  ", self.cells[index].display_value, end="  |")
            print(" ")
            print("|        |        |        |        |        |        |")
        print("=========" * 6 + "|")

    def launch_ship(self, ship):
        # launch ship to the battle board
        # каждый квадрат поля, занятый кораблем, получает имя этого корабля
        for cell_no in range(1, BORD_CELLS + 1):
            if self.cells[cell_no].cell_name in (ship.point_1, ship.point_2, ship.point_3):
                self.cells[cell_no].ship_name = ship.ship_name            #
            self.ships_journal[ship.ship_name] = ship.decks_number
        return self

    def create_fleet(self):  # строим флотилию

        three_deck = Ship("three_deck", 3, "2.1", "2.2", "2.3")
        self.launch_ship(three_deck)

        two_deck_1 = Ship("two_deck_1", 2, "3.4", "3.5")
        self.launch_ship(two_deck_1)

        two_deck_2 = Ship("two_deck_2", 2, "5.5", "6.5")
        self.launch_ship(two_deck_2)

        one_deck_1 = Ship("one_deck_1", 1, "4.1")
        self.launch_ship(one_deck_1)

        one_deck_2 = Ship("one_deck_2", 1, "4.3")
        self.launch_ship(one_deck_2)

        one_deck_3 = Ship("one_deck_3", 1, "6.1")
        self.launch_ship(one_deck_3)

        one_deck_4 = Ship("one_deck_4", 1, "6.3")
        self.launch_ship(one_deck_4)

    def take_input(self):

        print("Ваш ход, введите номер квадрата - ")
        input_value = input()
        if not input_value:
            return -1

        for cell_no in range(1, BORD_CELLS + 1):
            if input_value in (self.cells[cell_no].cell_name, self.cells[cell_no].cell_name.replace(".", ""),
                               self.cells[cell_no].cell_name.replace(".", ",")):
                # check the cell hitted
                if self.cells[cell_no].display_value in (" T ", " X "):

                    # self.display_board()
                    print("Неэффективно. В этот квадрат вы уже стреляли. Итак, ")
                    return -1
                if self.cells[cell_no].ship_name == "":
                    self.cells[cell_no].display_value = " T "
                    self.display_board()
                    print("Мимо!")
                    print("""На доске ваш ход отображается буквой "Т" """)
                    return 0
                else:  # you hit a ship!
                    self.cells[cell_no].display_value = " X "
                    # if it was a last deck ship or a one deck ship, remove it from ships_journal
                    ship_name = self.cells[cell_no].ship_name
                    decks_number = self.ships_journal[ship_name]
                    if decks_number == 1:
                        del self.ships_journal[ship_name]   # remove the ship
                        self.display_board()
                        if not self.ships_journal: # no ships left
                            print("""На доске ваш ход отображается буквой "X".""")
                            return 0
                        # self.display_board()
                        print("Вы потопили корабль противника.")
                        print ("""На доске ваш ход отображается буквой "X". И сновa, """)
                        return 0
                    else:
                        # убираем подбитую палубу из ships_journal dictionary
                        live_decks_number = decks_number - 1
                        d = {ship_name: live_decks_number}
                        self.ships_journal.update(d)
                        self.display_board()
                        print("Вы попали в корабль противника.")
                        print("""На доске ваш ход отображается буквой "X". И снова, """)
                        return 0

        print("Это не номер квадрата. Итак, ")  # Итак, ваш ход -
        return -1

# =========================================

def main():

    board = Board()
    board.create_fleet()
    board.display_board()

    print("Уважаемый Игрок, перед вами поле противника. Начинайте игру.")
    while board.ships_journal:
        result = board.take_input()  # -1  failure; 0 success
    if result == 0:
        print("Вы полностью разбили флот противника, поздравляем!")
        print("The end of the game.")

main()