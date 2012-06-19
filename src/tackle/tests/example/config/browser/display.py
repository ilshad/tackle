import tackle

class Pagelet:

    def update(self):
        self.c1 = tackle.persistent_config("First Example Config")
        self.c2 = tackle.persistent_config("Second Example Config")
