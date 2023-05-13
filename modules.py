#several ways of importing:
# #1 import the class directly via classname and call the functions by typing classname.function()

# import functions_with_arguments
#functions_with_arguments.greeting("Alpar")
#functions_with_arguments.user_guessing_game(str(65), "stop")

# #2 imports can be assigned to an alias; call the functions by typing alias.function()
#import functions_with_arguments as f

#f.greeting("Alpar")
#f.user_guessing_game(str(65), "stop")


# #3 import functions directly withouth importing whole module
# from functions_with_arguments import user_guessing_game, greeting

# user_guessing_game(str(65), "stop")
# greeting("Alpar")

# #4 you can also assign aliases to functions
from my_package.functions_with_arguments import user_guessing_game as theGame, greeting as yo

theGame(str(65), "stop")
yo("Alpar")