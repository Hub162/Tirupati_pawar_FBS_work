interior_area = float(input("Enter the total area of interior walls in square meters: "))
interior_cost_per_m2 = float(input("Enter the cost of painting interior walls per square meter: "))

exterior_area = float(input("Enter the total area of exterior walls in square meters: "))
exterior_cost_per_m2 = float(input("Enter the cost of painting exterior walls per square meter: "))

# Calculate total cost
total_interior_cost = interior_area * interior_cost_per_m2
total_exterior_cost = exterior_area * exterior_cost_per_m2
total_painting_cost = total_interior_cost + total_exterior_cost

# Output the result
print("\n--- Painting Cost Summary ---")
print(f"Interior Painting Cost: ₹{total_interior_cost:.2f}")
print(f"Exterior Painting Cost: ₹{total_exterior_cost:.2f}")
print(f"Total Painting Cost: ₹{total_painting_cost:.2f}")