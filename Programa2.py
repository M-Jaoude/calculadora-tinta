paint_yield_l_m2 = int(input("Qual é o rendimento da tinta?"))

wall_1 = wall_3 = 5*3
wall_2 = wall_4 = 4*3
roof = 5*4

total_area = 0

areas = []

areas.append(wall_1)
areas.append(wall_2)
areas.append(wall_3)
areas.append(wall_4)
areas.append(roof)

print(areas)

for area in areas:
    total_area = total_area + area
print(total_area)

paint_needed = total_area / paint_yield_l_m2

print(f'You will need {paint_needed} liters to paint the room')   


