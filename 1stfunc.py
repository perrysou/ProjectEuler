def total_takings(yearly_records):
    total = 0
    for month in yearly_records:
        for takings in yearly_records[month]:
            total += takings
    return total

monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}

print(total_takings(monthly_takings))