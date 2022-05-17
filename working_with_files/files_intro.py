
def open_print_file(file):
    try:
        with open(file, "r") as open_file:
            for line in open_file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError:
        print("File was not found")
        raise
    finally:
        print("Execution complete")

def write_to_file(file, order_item):
    try:
        with open(file, "w") as open_file:
            open_file.write(order_item + '\n')
    except FileNotFoundError:
        print("File not found!")


open_print_file("orders.txt")
write_to_file("orders.txt","potatoes")
open_print_file("orders.txt")