num = input("Enter numbers separated by spaces: ").split()
num = [float(num) for num in numbers]
print(f"Average: {sum(numbers) / len(numbers)}")