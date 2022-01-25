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
        self.serial_number = start
        self.original_start = start
    
    def generate(self):
        """Genreate sequential number from the start number"""
        self.serial_number += 1
        return self.serial_number - 1

    def reset(self):
        """Reset the number to the starting number"""
        self.serial_number = self.original_start