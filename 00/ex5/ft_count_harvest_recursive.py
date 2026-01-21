def ft_count_harvest_recursive(n):
    days = int(input("Days until harvest: "))
    
    def print_day(i):
        if i > days:
            print("Harvest time!")
            return
        print(f"Day {i}")
        print_day(i + 1)
    
    print_day(1)