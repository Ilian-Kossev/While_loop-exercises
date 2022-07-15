length = int(input())
width = int(input())
cake_pieces_available = length * width
total_cakes_needed = 0
command = input()
while command != "STOP":
    cakes_needed = int(command)
    total_cakes_needed += cakes_needed
    if total_cakes_needed >= cake_pieces_available:
        cakes_missing = total_cakes_needed - cake_pieces_available
        print(f"No more cake left! You need {cakes_missing} pieces more.")
        break
    command = input()
if total_cakes_needed <= cake_pieces_available:
    cake_pieces_left = cake_pieces_available - total_cakes_needed
    print(f"{cake_pieces_left} pieces are left.")
