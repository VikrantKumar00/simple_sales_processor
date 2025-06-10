raw_sales_data = [
    {"product": "Laptop", "quantity": 10, "unit_price": 1200.00},
    {"product": "Mouse", "quantity": 25, "unit_price": 25.00},
    {"product": "Keyboard", "quantity": 15, "unit_price": 45.00},
    {"product": "Monitor", "quantity": 5, "unit_price": 300.00},
    {"product": "webcam", "quantity": 20, "unit_price": 75.00},
]

print("---- Raw Sales Data ----")
for record in raw_sales_data:
    print(record)
print("\n")

processed_sales_data = []

print("---- Processed Sales Data ----")
for record in raw_sales_data:
    total_revenue = record["quantity"] * record["unit_price"]

    processed_record = {
        "product": record["product"],
        "quantity": record["quantity"],
        "unit_price": record["unit_price"],
        "total_revenue": total_revenue
    }

    processed_sales_data.append(processed_record)
    print(f"processed: {processed_record}")
print("\n")

output_file_name = "processed_sales_output.txt"

print(f"---- Saving Processed Data to '{output_file_name}' ----")
try:
    with open(output_file_name, "w") as file:
        file.write("Product,Quantity,Unit Price,Total Revenue\n")
        for record in processed_sales_data:
            line = f"{record['product']},{record['quantity']},{record['unit_price']},{record['total_revenue']}\n"
            file.write(line)
    print(f"Successfully saved processed data to '{output_file_name}'")

except IOError as e:
    print(f"Error saving data to file: {e}")

print("--- Aggregate Metrics ---")
if processed_sales_data:
    total_all_revenue = sum(record["total_revenue"] for record in processed_sales_data)
    average_revenue_per_sale = total_all_revenue / len(processed_sales_data)
    print(f"Total Revenue across all sales: ${total_all_revenue:.2f}")
    print(f"Average Revenue per sale: ${average_revenue_per_sale:.2f}")
else:
    print("No sales data to analyze.")

print("\n---- Script Finished ----")
print("Thank you for using the sales processing script!")

