# esta clase extiende a una lista, por lo que se pueden usar los metodos append y eso
# para crear nuevas generaciones usamos new_empty_generation asi el numero se aumenta solo

class Generation(list):
    class_number = 0

    def __init__(self):
        super().__init__()
        self.generation_number = Generation.class_number
        Generation.class_number += 1

    def new_empty_generation(self):
        return self.__init__(self.generation_number + 1)
