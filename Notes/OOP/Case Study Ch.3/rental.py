# def get_valid_input(input_string, valid_options):
#     input_string += " ({}) ".format(", ".join(valid_options))
#     response = input(input_string)
#     while response.lower() not in valid_options:
#         response = input(input_string)
#     return response

from property import get_valid_input


class Rental:
    def __init__(self, furnished="", utilities="", rent="", **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What are the estimated utilities? "),
            furnished=get_valid_input("Is the property furnished? ", ("yes", "no")),
        )

    prompt_init = staticmethod(prompt_init)


# get_valid_input()
