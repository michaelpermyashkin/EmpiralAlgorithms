import os
import random

# #########################
# #       Unsorted        #
# #########################
# smallPath = "./input/small/unsorted/unsorted{}"
# mediumPath = "./input/medium/unsorted/unsorted{}"
# largePath = "./input/large/unsorted/unsorted{}"
# for i in range(30):
#     # small file writer
#     with open(smallPath.format(i), "w+") as out:
#         for x in range(10000):
#             val = random.randint(0, 9999)
#             out.write("{}\n".format(val))

#     # medium file writer
#     with open(mediumPath.format(i), "w+") as out:
#         for x in range(100000):
#             val = random.randint(0, 9999)
#             out.write("{}\n".format(val))

#     # large file writer
#     with open(largePath.format(i), "w+") as out:
#         for x in range(1000000):
#             val = random.randint(0, 9999)
#             out.write("{}\n".format(val))

# #########################
# #        Sorted         #
# #########################
# smallPath = "./input/sorted/small/sorted{}"
# mediumPath = "./input/sorted/medium/sorted{}"
# largePath = "./input/sorted/large/sorted{}"
# for i in range(30):
#     # small file writer
#     values = list()
#     for x in range(10000):
#         val = random.randint(0, 9999)
#         values.append(val)
#     values.sort()
#     with open(smallPath.format(i), "w+") as out:
#         for val in values:
#             out.write("{}\n".format(val))

#     # medium file writer
#     values = list()
#     for x in range(100000):
#         val = random.randint(0, 9999)
#         values.append(val)
#     values.sort()
#     with open(mediumPath.format(i), "w+") as out:
#         for val in values:
#             out.write("{}\n".format(val))

#     # large file writer
#     values = list()
#     for x in range(1000000):
#         val = random.randint(0, 9999)
#         values.append(val)
#     values.sort()
#     with open(largePath.format(i), "w+") as out:
#         for val in values:
#             out.write("{}\n".format(val))

#########################
#        Reverse        #
#########################
smallPath = "./input/reverse/small/reverse{}"
mediumPath = "./input/reverse/medium/reverse{}"
largePath = "./input/reverse/large/reverse{}"
for i in range(30):
    # small file writer
    values = list()
    for x in range(10000):
        val = random.randint(0, 9999)
        values.append(val)
    values.sort(reverse=True)
    with open(smallPath.format(i), "w+") as out:
        for val in values:
            out.write("{}\n".format(val))

    # medium file writer
    values = list()
    for x in range(100000):
        val = random.randint(0, 9999)
        values.append(val)
    values.sort(reverse=True)
    with open(mediumPath.format(i), "w+") as out:
        for val in values:
            out.write("{}\n".format(val))

    # large file writer
    values = list()
    for x in range(1000000):
        val = random.randint(0, 9999)
        values.append(val)
    values.sort(reverse=True)
    with open(largePath.format(i), "w+") as out:
        for val in values:
            out.write("{}\n".format(val))