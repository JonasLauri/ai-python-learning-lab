import calendar

# Exercise 4 — Fitness Progress Tracker
workouts = [3200, 4500, 3900, 5000, 5500, 4700, 6000]

# Calculate the weekly total and average steps.
total_steps = sum(workouts)
average_steps = total_steps / len(workouts) if workouts else 0

# Find which days exceeded 5000 steps.
exceeded_days = [calendar.day_name[i] for i, steps in enumerate(workouts) if steps > 5000]

# Print results and an encouragement message if the average ≥ 4000, otherwise suggest improvement.
print(f"Total steps of week: {total_steps}\n" f"Average steps of week: {average_steps:.0f}")

if exceeded_days:
    print("Days you exceeded 5000 steps are:")
    for day in exceeded_days:
        print(day)
else:
    print("No days exceeded this week 5000 steps")

if average_steps >= 4000:
    print("You rock. Your average step count is more than 4000. Keep going!")
else:
    print("You should move more")
