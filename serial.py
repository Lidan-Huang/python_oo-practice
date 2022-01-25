class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Create the starting number from the argument"""
        self.start = start
        self.original_start = 100
    
    def generate(self):
        """Genreate sequential number from the start number"""
        self.start += 1
        return self.start - 1

    def reset(self):
        """Reset the number to the starting number"""
        self.start = self.original_start