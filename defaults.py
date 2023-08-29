from classes.fighters import *

# la idea aca es levantar la configuracion de un JSON y cambiar la funcion create_fighter por el constructor adecuado
create_fighter = lambda stats, height: Warrior(stats, height)
