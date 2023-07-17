#User Input
def ask_mage():
  print("""
Verily, in the realm of enchantment's fold,
The triad of sorcery, mighty and bold.
By the Classes of Magic, three in accord,
Mote powerful we be, in mystical accord.
""")
  magic_class = input("Enter Thou School: ")
  # Variables
  magus_success = str('Salute Mi Magus Comadre')
  death_of_magus = str('Thou Shalt Die!!!')
  # list of magic Schools
  school_of_three = ["Necromancy", "Destruction", "Alteration", "Restoration"]
  if magic_class != school_of_three:
    print(f"{magus_success}")
  else:
    print(f"{death_of_magus}")
  
  print(F"Thou Classeth Art: {magic_class}")
  
ask_mage()