first_printing = [1, 1, 2, 11, 5, 8, 13, 2, 4]
second_printing = [2, 4, 5, 1, 6, 8, 9, 3, 10, 13]

eralps_sheets = []
recycle_bin = []

first_printing.extend(second_printing)
first_printing.sort()
for i in range(len(first_printing)-1):
    if first_printing[i] == first_printing[i+1]:
        recycle_bin.append(first_printing[i])
    else:
        eralps_sheets.append(first_printing[i])

print(recycle_bin)
print(eralps_sheets)
