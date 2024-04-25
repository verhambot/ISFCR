# Read the output file to get the list of products
with open("output.txt", "r") as file:
    output_str = file.read()


# Convert the string representation of the list into an actual list of integers
output = eval(output_str)


# Function to find factors in the desired ASCII range
def find_factors(product):

    # The valid range now includes printable ASCII characters and additional ones
    valid_ascii = list(range(97, 123))  # lowercase a-z (97-122)
    valid_ascii += [33, 95, 123, 125]  # Adding special characters such as ! _ { }

    # Try to find factors that belong to the valid ASCII set
    for i in valid_ascii:
        if product % i == 0:
            j = product // i
            if j in valid_ascii:
                return [i, j]


# Recover the original pairs of ASCII values
for product in output:

    possible_factors = find_factors(product)

    if possible_factors:
        print(" ".join(map(chr, possible_factors)))
