import sys


def error_message_detail(error, error_detail: sys):
    """
    Function to get detailed error message with file name and line number.

    :param error: The error that occurred (e.g., an exception or error message).
    :param error_detail: The sys module to retrieve traceback information.

    :return: A string containing the detailed error message with file name and line number.
    """
    # Get the current traceback information
    _, _, exc_tb = error_detail.exc_info()

    # Get the file name where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Construct the detailed error message with file name and line number
    error_message = "Error occurred in Python script name [{0}] at line number [{1}]: {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


class AppException(Exception):
    """
    Custom exception class with detailed error message.

    :param error_message: The error message in string format.
    :param error_detail: The sys module to retrieve traceback information.
    """
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)  # Call the base class constructor to set the error message.

        # Get the detailed error message with file name and line number using the error_message_detail function.
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        """
        Return the detailed error message when the exception is printed as a string.
        """
        return self.error_message