def convert_to_indian_currency(number):
    num_str = str(number)
    if len(num_str) <= 3:
        return num_str
    last_three_digits = num_str[-3:]
    remaining_digits = num_str[:-3]
    remaining_digits_reversed = remaining_digits[::-1]
    grouped_pairs = [remaining_digits_reversed[i:i+2] for i in range(0, len(remaining_digits_reversed), 2)]
    grouped_pairs = [pair[::-1] for pair in grouped_pairs]
    indian_currency = ','.join(grouped_pairs[::-1])
    return indian_currency + ',' + last_three_digits
user_input = int(input("Enter a number: "))
print("Indian Currency Notation:", convert_to_indian_currency(user_input))
