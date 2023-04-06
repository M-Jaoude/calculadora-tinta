paint_yield_l_m2 = int(input("Qual é o rendimento da tinta (litro por m2)? "))

walls = int(input("Quantas paredes você irá pintar? "))
            
areas = []

for wall in range(walls):
    area = int(input(f'Digite a area da parede {wall + 1} (lado x lado): '))
    areas.append(area)
    
print(areas)

total_area = 0

for a in areas:
    total_area += a
    
print(total_area) 

total_paint = total_area / paint_yield_l_m2

print(f'Você precisará de {round(total_paint, 2)} litros de tinta para pintar {walls} paredes')

    
       

