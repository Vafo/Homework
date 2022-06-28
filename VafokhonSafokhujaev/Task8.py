
from math import ceil


class Pagination:

    def __init__(self, input_str: str, page_symbols: int) -> None:
        self.text = input_str
        self.item_count = len(input_str)
        self.boundary = page_symbols
        self.page_count = ceil(self.item_count / self.boundary)

    def get_page(self, index: int) -> int:
        if index > self.item_count:
            return -1
        
        return index // self.boundary

    def count_items_on_page(self, page: int) -> int:
        if page >= self.page_count:
            print(f"Invalid index : Page {page} is missing")
            return None

        return self.boundary if page < self.page_count-1 else self.item_count - page * self.boundary

    def find_page(self, query: str) -> list[int]:
        occurences = []
        index = 0
        
        while True:
            index = self.text.find(query, index)
            if index >= 0:
                occurences.append(index)
            else:
                break
            index += len(query)
        
        if len(occurences) == 0:
            print(f"{query!r} is missing on the pages")
            return None

        page_nums = set()
        for match in occurences:
            for i in range(self.get_page(match), self.get_page(match + len(query)) + 1):
                page_nums.add(i)
                
        page_nums = sorted(list(page_nums))


        return page_nums

        

    
pages = Pagination('Your beautiful text', 5)
print(pages.page_count)
print(pages.item_count)

print(pages.count_items_on_page(0))
print(pages.count_items_on_page(3))
print(pages.count_items_on_page(4))

print(pages.find_page('Your'))
print(pages.find_page("e"))
print(pages.find_page('beautiful'))
print(pages.find_page('great'))