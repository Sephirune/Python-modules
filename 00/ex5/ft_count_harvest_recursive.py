def ft_count_harvest_recursive(n):
    if n == 0:
        print("Harvest time!")
        return
    else:
        ft_count_harvest_recursive(n - 1)
        print(f"Day {n}")