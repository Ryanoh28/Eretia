from utilities import clear_console
from items import Item

class Journal(Item):
    def __init__(self, name, description, pages):
        super().__init__(name, description)
        self.pages = pages
        self.current_page = 0

    def use(self, player):
        while True:
            clear_console()
            print(f"Page {self.current_page + 1}/{len(self.pages)}\n")
            print(self.pages[self.current_page])
            print("\n[n] Next page, [p] Previous page, [q] Quit reading")
            
            choice = input("Choice: ").strip().lower()
            if choice == 'n' and self.current_page < len(self.pages) - 1:
                self.current_page += 1
            elif choice == 'p' and self.current_page > 0:
                self.current_page -= 1
            elif choice == 'q':
                break

waystation_journal_pages = [
    "Day 1.\n\nCrossed the border. Heading along the Ancient Road. The journey ahead is fraught with uncertainty, but I am resolute.",
    "Day 3.\n\nArrived at the waystation. Surprised to find human presence here. This place, though decrepit, holds a strange charm.",
    "Day 7.\n\nToday, I dueled with an upstart, overconfident in his skills. A reminder that even in these lands, human conflict persists.",
    "Day 10.\n\nEncountered human bandits. It's disheartening to see humanity so divided in this forsaken land. We should stand united.",
    "Day 13.\n\nTook time to sharpen Shadowfang and clean my mithril armour. Both have served me well and will continue to do so.",
    "Day 27.\n\nMy final day at the waystation. Preparing to head deeper into the unknown. What lies ahead, I cannot say, but I must find out. D.B"
]
waystation_journal = Journal("Waystation Journal", "A journal found within the Mithril Armour at the waystation", waystation_journal_pages)