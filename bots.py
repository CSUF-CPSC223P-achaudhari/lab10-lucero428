import threading
import time

'''1.Define a function named `bot_clerk` to meet the following requirements:  
    a. Take an items list as a positional parameter.  This a list of item numbers to be fetched and placed in the cart. Example format is `['101','102','103']`.'''
''' b. Define a cart list and a thread lock.  All bots will use the same cart and lock.'''
def bot_clerk(itemlist):
    cart = []
    lock = threading.Lock()
    
    def bot_fetcher(list, cart, lock, inventory):
        for item in list:
            time.sleep(inventory[item][1])  
            with lock:
                cart.append([item, inventory[item][0]])  
    fetcher = {1: [], 2: [], 3: []}
    for i, item in enumerate(itemlist, start = 1):
        fetcher[i % 3 + 1].append(item)
    
    inventory = {
        "101": ["Notebook Paper", 2],
        "102": ["Pencils", 2],
        "103": ["Pens", 6],
        "104": ["Graph Paper", 1],
        "105": ["Paper Clips", 1],
        "106": ["Staples", 4],
        "107": ["Stapler", 7],
        "108": ["3 Ring Binder", 1],
        "109": ["Printer Paper", 1],
        "110": ["Notepad", 1]
    }

    threads = []
    for i in range(1, 4):
        thread = threading.Thread(target = bot_fetcher, args=(fetcher[i], cart, lock, inventory))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    return cart
