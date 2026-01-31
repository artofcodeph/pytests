"""
This module demonstrates a basic Python entry point structure.
It contains a main function and a secondary helper function.
"""

def main():
    """
    Main entry point for the script.
    Prints a greeting and calls the secondary function.
    """
    print("Hello world from pytests!")
    sec_function()

def sec_function():
    """
    A simple secondary function to demonstrate function calls.
    """
    print("sec_function called after the main function")

if __name__ == "__main__":
    # Execute the main function if the script is run directly
    main()