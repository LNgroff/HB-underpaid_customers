

def melon_delivery(day, file):
# Take a day and it's file to create a produce report
    print("Day", day)
    deliv_record = open(file) 
    # Opens correct file for day

    for line in deliv_record:
    # Looks at each delivery
        line = line.rstrip()
        # removes white space at the ends of the line
        words = line.split('|')
        # splits line into necessary items
        
        
        melon = words[0]
        # assigns the type of melon to 'melon'
        count = words[1]
        # assigns the number of melons to 'count'
        amount = words[2]
        # assigns the amount paid to 'amount'

        print(f"Delivered {count} {melon}s for total of ${amount}")
        # prints the order details

    deliv_record.close()
    # closes the file

# calls the functions
melon_delivery(1, "um-deliveries-20140519.txt")
melon_delivery(2, "um-deliveries-20140520.txt")
melon_delivery(3, "um-deliveries-20140521.txt")


'''
print("Day 1")
the_file = open("um-deliveries-20140519.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]
    print(f"Delivered {count} {melon}s for total of ${amount}")

the_file.close()


print("Day 2")
the_file = open("um-deliveries-20140520.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]
    print(f"Delivered {count} {melon}s for total of ${amount}")

the_file.close()


print("Day 3")
the_file = open("um-deliveries-20140521.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]
    print(f"Delivered {count} {melon}s for total of ${amount}")

the_file.close()

'''