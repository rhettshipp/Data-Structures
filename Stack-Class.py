class Stack(object):
    """
	A typical stack implementation.

	Parameters
	----------
	max_size : int, optional
		Maximum size of the stack.
	"""

    def __init__(self, max_size=None):
		self.data = []  # attribute to hold stack data
		self.max_size = max_size

    def push(self, value):
        """
		Push an object onto the stack.

		Parameters
		----------
		value : object
			Object to push onto the stack.
	  """
        if self.max_size is None or self.get_size() < self.max_size:
            self.data.append(value)
        else:
            raise ValueError('The stack is full.')

    def pop(self):
        """
		Pop an object off the stack.
	  """
        if self.is_empty():
            raise IndexError('There is nothing to pop.')
        return self.data.pop()

    def peek(self):
        """
		Return the top object off the stack (without removing it).
	  """
        if self.is_empty():
            raise IndexError('There is nothing to peek.')
        return self.data[-1]

    def get_size(self):
        """
		Returns the size of the stack.
	  """
        return len(self.data)
		
    def is_empty(self):
        """
		Returns whether the stack is empty.
	  """
        return self.get_size() == 0