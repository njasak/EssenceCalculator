def calculate_items(total_essence, essence_per_item, items_per_conversion):
    total_items = (total_essence // essence_per_item) * items_per_conversion
    return total_items

while True:
    total_essence = int(input("Enter the total essence (or enter 0 to quit): "))
    
    if total_essence == 0:
        break
    
    essence_per_item = int(input("Enter the essence required per item: "))
    items_per_conversion = int(input("Enter the number of items per essence conversion: "))

    result = calculate_items(total_essence, essence_per_item, items_per_conversion)
    print("The total number of items you can make is:", result)
    print()  # Print an empty line for readability

