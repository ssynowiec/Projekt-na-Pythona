# File: ParseSystem.py
#
# A class that allows you to safely parse data into another type.
# Useful when we are going to read data from files like <.env>

class ParseSystem:
    """The class responsible for safely changing the types of variables."""
    # A method that allows you to change the data type from string to any other.
    # Parameter values of type other than <str> will not change.
    # The values themselves of the likes of [True, False, None] can be written in wrong and the algorithm I
    # will be able to react accordingly anyway.
    @staticmethod
    def auto_parse(_val: any) -> any:
        """
        The method returns the corresponding type dynamically.
        The returned type is based on the value of the variable.

        Parameters:
            _val (any): The value to be parsed. (Preferably of type <str>)

        Return:
            The method returns the appropriate data type based on the value of the passed parameter.
        """
        if isinstance(_val, str):
            match _val.lower():
                case 'true':
                    return True
                case 'false':
                    return False
                case 'none':
                    return None

            # Rejects spelling errors
            try:
                return eval(_val)
            except _:
                return _val

        else:
            return _val

    # Python allows you to replace any type of variable with <str>.
    @staticmethod
    def to_string(_val: any) -> str:
        """
        The method responsible for changing any given parameter to a string of type <str>.

        Parameters:
            _val (any): The value to be changed to text.

        Return:
            The method returns a parameter in the form of text.
        """
        if isinstance(_val, str):
            return _val

        return str(_val)
