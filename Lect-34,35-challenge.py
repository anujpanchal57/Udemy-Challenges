# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments it contains, and the length of each segment.
#
# An IP address consists of 4 numbers, separated from each other with a full stop. But
# your program should just count however many are entered
# Examples of the input you may get are:
#    127.0.0.1
#    .192.168.0.1
#    10.0.123456.255
#    172.16
#    255
#
# So your program should work even with invalid IP Addresses. We're just interested in the
# number of segments and how long each one is.

# Using Package IP
# from IPy import IP

input_prompt = "Enter your IP Address. An IP address consists of 4 numbers, " \
               "separated from each other with a full stop: "
ipAddr = input(input_prompt)
if ipAddr[-1] != '.':
    ipAddr += '.'

# For checking Invalid IP Addresses
# IP(ipAddr)

# Declared Initial Variables
seg = 1
seg_length = 0
# char = ""

# If any char in the ipAddr
for char in ipAddr:
    if char == ".":
        print("Seg {} has {} chars".format(seg, seg_length))
        seg += 1
        seg_length = 0
    else:
        seg_length += 1

# If the last word is a . , then print the following
# if char != ".":
#     print("Seg {} has {} chars".format(seg, seg_length))
