
class Shelf:
    def __init__(self):
        self.item = None

    def is_empty(self):
        return self.item is None

    def place_item(self, item_name):
        if self.is_empty():
            self.item = item_name
            return True
        return False

    def __str__(self):
        return self.item if self.item else 'Tuscia'


class Section:
    def __init__(self, num_shelves):
        self.shelves = [Shelf() for _ in range(num_shelves)]

    def is_full(self):
        return all(not shelf.is_empty() for shelf in self.shelves)

    def display(self):
        return [str(shelf) for shelf in self.shelves]


class Floor:
    def __init__(self, num_sections, shelves_per_section):
        self.sections = [Section(shelves_per_section) for _ in range(num_sections)]

    def is_full(self):
        return all(section.is_full() for section in self.sections)


class Warehouse:
    def __init__(self, num_floors, section_per_floor, shelves_per_section):
        self.floors = [Floor(section_per_floor, shelves_per_section) for _ in range(num_floors)]
        self.num_floors = num_floors
        self.num_sections = section_per_floor
        self.num_shelves = shelves_per_section

    def is_full(self):
        return all(floor.is_full() for floor in self.floors)

    def place_item(self, floor_idx, section_idx, shelf_idx, item_name):
        try:
            shelf = self.floors[floor_idx].sections[section_idx].shelves[shelf_idx]
            return shelf.place_item(item_name)
        except IndexError:
            return False

    def display(self):
        print('SANDELIO BUKLE:')
        for floor_idx, floor in enumerate(self.floors):
            print(f'Aukstas {floor_idx + 1}')
            for section_idx, section in enumerate(floor.sections):
                display = section.display()
                print(f'Skyrius {section_idx + 1}: {display}')
        print()

NUM_FLOORS = 3
NUM_SECTION = 3
NUM_SHELVES = 3

warehouse = Warehouse(NUM_FLOORS, NUM_SECTION, NUM_SHELVES)

print('Sveiki atvyke i objektini 3D sandeli!')
print('Uzduotis - uzpildyti!!!')

while not warehouse.is_full():
    warehouse.display()
    try:
        f = int(input(f'Iveskite auksto numeri (1-{NUM_FLOORS}): ')) - 1
        s = int(input(f'Iveskite skyriaus numeri (1-{NUM_SECTION}): ')) - 1
        sh = int(input(f'Iveskite lentynos numeri (1-{NUM_SHELVES}): ')) - 1
        item = input('Iveskite prekes pavadinima: ').strip()

        if not (0 <= f < NUM_FLOORS and 0 <= s < NUM_SECTION and 0 <= sh < NUM_SHELVES):
            print('Netinkami numeriai! Bandykite dar karta!')
            continue

        success = warehouse.place_item(f, s, sh, item)
        if success:
            print(f'Preke {item} ideta i auksta {f+1}, skyriu {s+1}, lentyna {sh+1}')
        else:
            print('Si vieta uzimta! Bandykite kita!')

    except ValueError:
        print('Ivestis turi buti skaiciai')

warehouse.display()
print('Visi aukstai, skyriai ir lentynos uzpildyti! Sandelis pilnas!')
