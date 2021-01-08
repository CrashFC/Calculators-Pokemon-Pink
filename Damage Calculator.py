# Calculadora de Dano Pokémon Pink

type_pkmn1 = str(input('Type 1 Pokémon (Attacking PKMN): '))

type_pkmn2 = str(input('Type 2 Pokémon (Attacking PKMN): '))

lv1 = int(input('Level (Attacking PKMN): '))

base_atk = int(input('Base ATK (Attacking PKMN): '))

base_sp_atk = int(input('Base SP. ATK (Attacking PKMN): '))

type_pkmn3 = str(input('Type 1 Pokémon (Defending PKMN): '))

type_pkmn4 = str(input('Type 2 Pokémon (Defending PKMN): '))

lv2 = int(input('Level (Defending PKMN): '))

base_hp = int(input('Base HP (Defending PKMN): '))

base_defs = int(input('Base DEF (Defending PKMN): '))

base_sp_def = int(input('Base SP. DEF (Defending PKMN): '))

move = int(input('Base Power of Move used: '))

stat_move = str(input('Stat of Move (ATK ou SP. ATK): '))

type_move = str(input('Type of Move (Ex: Normal): '))

critical = str(input('Critical Hit ("Yes" or "No"): '))

critical2 = str(input('The Attacking PKMN has the Sniper Ability? ("Yes" or "No"): '))

atk = int(base_atk * 2.203921568627451 / 100 * lv1)

sp_atk = int(base_sp_atk * 2.203921568627451 / 100 * lv1)

if stat_move.lower() == 'ATK':
  stat_atk = atk
elif stat_move.lower() == 'SP.ATK' or 'SP. ATK':
  stat_atk = sp_atk
else: print(f'Stat Wrong')

hp = int(base_hp * 2.615686274509804 / 100 * lv2)

defs = int(base_defs * 2.203921568627451 / 100 * lv2)

sp_def = int(base_sp_def * 2.203921568627451 / 100 * lv2)

if stat_move.lower() == 'ATK':
  stat_def = defs
elif stat_move.lower() == 'SP.ATK' or 'SP. ATK':
  stat_def = sp_def
else: print(f'Stat Wrong')

if critical == 'Yes':
	critical_multi = 1.5
elif critical == 'No':
	critical_multi = 1
else:
	print(f'Critical Hit Error')

if critical2 == 'Yes':
	critical_multi2 = 2.25
	if critical == 'Yes':
		criticalhit = 2.25
	elif critical == 'No':
		criticalhit = 1
	else:
		print(f'Critical Hit Error')
elif critical2 == 'No':
	criticalhit = critical_multi
else:
	print(f'Critical Hit Error')
	
if type_pkmn1 == type_move:
	power_effectivity = 1.25
elif type_pkmn2 == type_move:
	power_effectivity = 1.25
else:
	power_effectivity = 1

power = int(stat_atk * move / 100 * 1.1500000000000001)

hit_power = int(power * criticalhit * power_effectivity)

block_percent = int(100 / 765 * stat_def)

block = 100 - block_percent

damage = int(hit_power * block / 100)

print(f'')
print(f'Attacking Pokémon')
print(f'Types: {type_pkmn1} | {type_pkmn2}')
print(f'ATK: {atk}')
print(f'SP. ATK: {sp_atk}')
print(f'')
print(f'Defending Pokémon')
print(f'Types: {type_pkmn3} | {type_pkmn4}')
print(f'HP: {hp}')
print(f'DEF: {defs}')
print(f'SP. DEF: {sp_def}')
print(f'')
print(f'Damage = {damage}')

if damage == hp:
  print(f'Perfect 1HKO')
elif damage > hp:
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