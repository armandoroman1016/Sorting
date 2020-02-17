animals = ['Duck','Jackal','Hippo','Aardvark','Cat','Flamingo','Iguana','Giraffe','Elephant','Bear']

# O(1)
# print(animals[3])

# # O(1)
# animals.append("snake")

# # O(N)
# for i in range(0, len(animals)):
#     print(animals[i])


# # O(n^2)
# for i in range(0, len(animals)):
#     for j in range(0, len(animals)):
#         print(f"{animals[i]} -- {animals[j]}")


# 0(n^3)
# for i in range(0, len(animals)):
#     for j in range(0, len(animals)):
#         for k in range(0, len(animals)):
#             sum += 1
#             print(f"{animals[i]} -- {animals[j]} -- {animals[k]}")

# print(sum)