# a = 89126723492837429672
#
#
# def is_prime(num):
#     for i in range(2, num//2+1):
#         if num%i==0:
#             print(i)
#             return num//i
#     return 1
# #
# # prod = 1
# # i = 2
# # while prod < a:
# #     if a%i==0:
# #         if is_prime(i):
# #             print(i)
# #             prod *= i
# #     i += 1
# #     if i > a//2:
# #         i = 2
# # print("prod", prod)
#
# def Prime(n):
#     if n & 1 == 0:
#         return 2
#     d= 3
#     while d * d <= n:
#         if n % d == 0:
#             print(d)
#             return n//d
#         d= d + 2
#     return 1

# while a > 1:
#     print(a)
#     a = is_prime(a)

import pandas as pd

saved = pd.read_csv("saved.csv", index_col=0)
saved[saved["score"]<6000].reset_index(inplace=True)
saved.to_csv("saved.csv")