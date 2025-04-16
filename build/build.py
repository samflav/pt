import os
from builder import Builder


BASE_SITE = "https://pt.samuelflavin.com"

if __name__ == "__main__":
    bob = Builder(os.getcwd(), BASE_SITE)

    #TODO(generate cards based off of file structure.)

    bob.build()