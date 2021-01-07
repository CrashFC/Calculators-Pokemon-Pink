# Calculadora Pokémon Pink (Fan Game By CrashFC)

# Entrada dos Stats
pokemon = str(input('Nome do Pokémon: '))
lv = int(input('Level do Pokémon: '))
primeiro_numero = float(input('HP: '))
segundo_numero = float(input('ATK: '))
terceiro_numero = float(input('DEF: '))
quarto_numero = float(input('SP. ATK: '))
quinto_numero = float(input('SP. DEF: '))
sexto_numero = float(input('VEL: '))
nature = str(input('Nature: '))

# Operações Matemáticas
hp = primeiro_numero * 2.6156862746 / 100 * lv
atk = segundo_numero * 2.2039215686 / 100 * lv
defs = terceiro_numero * 2.2039215686 / 100 * lv
sp_atk = quarto_numero * 2.2039215686 / 100 * lv
sp_def = quinto_numero * 2.2039215686 / 100 * lv
vel = sexto_numero * 2.2039215686 / 100 * lv
adamant1 = int(atk * 1.1)
adamant2 = int(sp_atk * 0.9)
bold1 = int(defs * 1.1)
bold2 = int(atk * 0.9)
brave1 = int(atk * 1.1)
brave2 = int(vel * 0.9)
calm1 = int(sp_def * 1.1)
calm2 = int(atk * 0.9)
careful1 = int(sp_def * 1.1)
careful2 = int(sp_atk * 0.9)
gentle1 = int(sp_def * 1.1)
gentle2 = int(defs * 0.9)
hasty1 = int(vel * 1.1)
hasty2 = int(defs * 0.9)
impish1 = int(defs * 1.1)
impish2 = int(sp_atk * 0.9)
jolly1 = int(vel * 1.1)
jolly2 = int(sp_atk * 0.9)
lax1 = int(defs * 1.1)
lax2 = int(sp_def * 0.9)
lonely1 = int(atk * 1.1)
lonely2 = int(defs * 0.9)
mild1 = int(sp_atk * 1.1)
mild2 = int(defs * 0.9)
modest1 = int(sp_atk * 1.1)
modest2 = int(atk * 0.9)
naive1 = int(vel * 1.1)
naive2 = int(sp_def * 0.9)
naughty1 = int(atk * 1.1)
naughty2 = int(sp_def * 0.9)
quiet1 = int(sp_atk * 1.1)
quiet2 = int(vel * 0.9)
rash1 = int(sp_atk * 1.1)
rash2 = int(sp_def * 0.9)
relaxed1 = int(defs * 1.1)
relaxed2 = int(vel * 0.9)
sassy1 = int(sp_def * 1.1)
sassy2 = int(vel * 0.9)
timid1 = int(vel * 1.1)
timid2 = int(atk * 0.9)

# Saída dos cálculos
if nature == 'Adamant':
  atk = adamant1
  sp_atk = adamant2
elif nature == 'Bold':
  defs = bold1
  atk = bold2
elif nature == 'Brave':
  atk = brave1
  vel = brave2
elif nature == 'Calm':
  sp_def = calm1
  atk = calm2
elif nature == 'Careful':
  sp_def = careful1
  sp_atk = careful2
elif nature == 'Gentle':
  sp_def = gentle1
  defs = gentle2
elif nature == 'Hasty':
  vel = hasty1
  defs = hasty2
elif nature == 'Impish':
  defs = impish1
  sp_atk = impish2
elif nature == 'Jolly':
  vel = jolly1
  sp_atk = jolly2
elif nature == 'Lax':
  defs = lax1
  sp_def = lax2
elif nature == 'Lonely':
  atk = lonely1
  defs = lonely2
elif nature == 'Mild':
  sp_atk = mild1
  defs = mild2
elif nature == 'Modest':
  sp_atk = modest1
  atk = modest2
elif nature == 'Naive':
  vel = naive1
  sp_def = naive2
elif nature == 'Naughty':
  atk = naughty1
  sp_def = naughty2
elif nature == 'Quiet':
  sp_atk = quiet1
  vel = quiet2
elif nature == 'Rash':
  sp_atk = rash1
  sp_def = rash2
elif nature == 'Relaxed':
  defs = relaxed1
  vel = relaxed2
elif nature == 'Sassy':
  sp_def = sassy1
  vel = sassy2
elif nature == 'Timid':
  vel = timid1
  atk = timid2

print(f'')
print(f'POKÉMON - {pokemon}')
print(f'HP - {int(hp)}')
print(f'ATK - {int(atk)}')
print(f'DEF - {int(defs)}')
print(f'SP. ATK - {int(sp_atk)}')
print(f'SP. DEF - {int(sp_def)}')
print(f'VEL - {int(vel)}')

#Natures
if nature == 'Adamant':
  print(f'Adamant: +ATK  -SP. ATK')
elif nature == 'Bashful':
  print(f'Bashful: Nothing Changed')
elif nature == 'Bold':
  print(f'Bold: +DEF  -ATK')
elif nature == 'Brave':
  print(f'Brave: +ATK  -VEL')
elif nature == 'Calm':
  print(f'Calm: +SP. DEF  -ATK')
elif nature == 'Careful':
  print(f'Careful: +SP. DEF  -SP. ATK')
elif nature == 'Docile':
  print(f'Docile: Nothing Changed')
elif nature == 'Gentle':
  print(f'Gentle: +SP. DEF  -DEF')
elif nature == 'Hardy':
  print(f'Hardy: Nothing Changed')
elif nature == 'Hasty':
  print(f'Hasty: +VEL  -DEF')
elif nature == 'Impish':
  print(f'Impish: +DEF  -SP. ATK')
elif nature == 'Jolly':
  print(f'Jolly: +VEL  -SP. ATK')
elif nature == 'Lax':
  print(f'Lax: +DEF  -SP. DEF')
elif nature == 'Lonely':
  print(f'Lonely: +ATK  -DEF')
elif nature == 'Mild':
  print(f'Mild: +SP. ATK  -DEF')
elif nature == 'Modest':
  print(f'Modest: +SP. ATK  -ATK')
elif nature == 'Naive':
  print(f'Naive: +VEL  -SP. DEF')
elif nature == 'Naughty':
  print(f'Naughty: +ATK  -SP. DEF')
elif nature == 'Quiet':
  print(f'Quiet: +SP. ATK  -VEL')
elif nature == 'Quirky':
  print(f'Quirky: Nothing Changed')
elif nature == 'Rash':
  print(f'Rash: +SP. ATK  -SP. DEF')
elif nature == 'Relaxed':
  print(f'Relaxed: +DEF  -VEL')
elif nature == 'Sassy':
  print(f'Sassy: +SP. DEF  -VEL')
elif nature == 'Serious':
  print(f'Serious: Nothing Changed')
elif nature == 'Timid':
  print(f'Timid: +VEL  -ATK')
else:
  print(f'Nature Wrong')