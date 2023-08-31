
class Generation(list):
    class_number = 0

    def __init__(self):
        super().__init__()
        self.generation_number = Generation.class_number
        Generation.class_number += 1
