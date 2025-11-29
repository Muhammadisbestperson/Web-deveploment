class StringReverser:
    def __init__(self, originalstring):
        self.originalstring = originalstring

    def reverse(self):
        return self.originalstring[::-1]

# Example usage
my_string = StringReverser("hello world")
reversed_str = my_string.reverse()
print(f"Original: {my_string.originalstring}, Reversed: {reversed_str}")