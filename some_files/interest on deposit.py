deposit = 24838.74
interest = 8

interest_frac = interest / 100
percent_for_day = round(deposit * interest_frac / 366, 2)
# percent_from_to_1 = round(percent_for_day * 29, 2)
# percent_from_to_2 = round(percent_for_day * 29, 2)
percent_all = round(percent_for_day * 29, 2)
deposit_new_after_month = round(deposit + percent_all, 2)

print(percent_for_day)
print(percent_all)
print(deposit_new_after_month)

deposit2 = deposit_new_after_month
percent_for_day2 = round(deposit2 * interest_frac / 366, 2)
percent_all2 = round(percent_for_day2 * 31, 2)
deposit_new_after_month2 = round(deposit2 + percent_all2, 2)

print()
print(percent_for_day2)
print(percent_all2)
print(deposit_new_after_month2)
