# esta clase extiende a una lista, por lo que se pueden usar los metodos append y eso
# para crear nuevas generaciones usamos new_empty_generation asi el numero se aumenta solo

class Generation(list):
    def __init__(self, generation_number = 0):
        super().__init__()
        self.generation_number = generation_number

    def new_empty_generation(self):
        return self.__init__(self.generation_number + 1)
