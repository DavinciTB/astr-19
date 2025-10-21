import math

def generate_sine_table(start_x, end_x, num_entries):
    """
    Generates a list of (x, sin(x)) tuples.

    Args:
        start_x (float): The starting value of x.
        end_x (float): The ending value of x.
        num_entries (int): The number of entries in the table.

    Returns:
        list: A list of tuples, where each tuple contains (x_value, sin_x_value).
    """
    table_data = []
    step_size = (end_x - start_x) / (num_entries - 1) if num_entries > 1 else 0

    for i in range(num_entries):
        x = start_x + i * step_size
        sin_x = math.sin(x)
        table_data.append((x, sin_x))
    return table_data

def main():
    """
    Main function to execute the sine table generation and printing.
    """
    start_value = 0.0
    end_value = 2.0
    number_of_entries = 1000

    sine_table = generate_sine_table(start_value, end_value, number_of_entries)

    print(f"{'x':<15} {'sin(x)':<15}")
    print("-" * 30)
    for x_val, sin_x_val in sine_table:
        print(f"{x_val:<15.6f} {sin_x_val:<15.6f}")

if __name__ == "__main__":
    main()