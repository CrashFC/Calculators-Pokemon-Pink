# Calculadora de Dano Pokémon Pink

base_atk = int(input('Base ATK (Attacking PKMN): '))

base_sp_atk = int(input('Base SP. ATK (Attacking PKMN): '))

base_defs = int(input('Base DEF (Defending PKMN): '))

base_sp_def = int(input('Base SP. DEF (Defending PKMN): '))

base_hp = int(input('Base HP (Defending PKMN): '))

lv1 = int(input('Level (Attacking PKMN): '))

lv2 = int(input('Level (Defending PKMN): '))

move = int(input('Base Power of Move used: '))

type_move = str(input('Type of Move (ATK ou SP. ATK): '))

atk = int(base_atk * 2.203921568627451 / 100 * lv1)

sp_atk = int(base_sp_atk * 2.203921568627451 / 100 * lv1)

if type_move.lower() == 'ATK':
  type_atk = atk
elif type_move.lower() == 'SP.ATK' or 'SP. ATK':
  type_atk = sp_atk
else: print(f'Type Wrong')

hp = int(base_hp * 2.615686274509804 / 100 * lv2)

defs = int(base_defs * 2.203921568627451 / 100 * lv2)

sp_def = int(base_sp_def * 2.203921568627451 / 100 * lv2)

if type_move.lower() == 'ATK':
  type_def = defs
elif type_move.lower() == 'SP.ATK' or 'SP. ATK':
  type_def = sp_def
else: print(f'Type Wrong')

power = int(type_atk * move / 100 * 1.1500000000000001)

block_percent = int(100 / 765 * type_def)

block = 100 - block_percent

damage = int(power * block / 100)

print(f'')
print(f'Attacking Pokémon')
print(f'ATK: {atk}')
print(f'SP. ATK: {sp_atk}')
print(f'')
print(f'Defending Pokémon')
print(f'HP: {hp}')
print(f'DEF: {defs}')
print(f'SP. DEF: {sp_def}')
print(f'')
print(f'Damage = {damage}')

if damage == hp:
  print(f'Perfect 1HKO')
elif damage >= hp / 1:
  print(f'1HKO guaranted')
elif damage >= hp / 2:
  print(f'2HKO guaranted')
elif damage >= hp / 3:
  print(f'3HKO guaranted')
elif damage >= hp / 4:
  print(f'4HKO guaranted')
elif damage >= hp / 5:
  print(f'5HKO guaranted')
elif damage < hp / 5:
  print(f'More than 6 Hits to KO')