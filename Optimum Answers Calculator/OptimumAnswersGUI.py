import tkinter as tk
from tkinter import ttk
from OptimumAnswers import checkOptimumNumberOfAnswers

def validate_entry(value):
    return value.replace('.', '').isdigit() or value == ""

def calculate_optimal_strategy():
    # Get input values from the user
    max_exam_points = float(max_exam_points_entry.get().strip()) if max_exam_points_entry.get().strip() else 30.0
    number_of_questions = int(number_of_questions_entry.get().strip()) if number_of_questions_entry.get().strip() else 22
    max_points = float(max_points_entry.get().strip()) if max_points_entry.get().strip() else 60.0
    negative_penalty_percentage = float(negative_penalty_percentage_entry.get().strip()) if negative_penalty_percentage_entry.get().strip() else 1/3
    minimum_point_percentage = float(minimum_point_percentage_entry.get().strip()) if minimum_point_percentage_entry.get().strip() else 0.5
    current_points = float(current_points_entry.get().strip()) if current_points_entry.get().strip() else 0.0

    # Call the function with user input
    result = checkOptimumNumberOfAnswers(
        max_exam_points=max_exam_points,
        number_of_questions=number_of_questions,
        max_points=max_points,
        negative_penalty_percentage=negative_penalty_percentage,
        minimum_point_percentage=minimum_point_percentage,
        current_points=current_points
    )

    # Display the result in the text widget
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Statistically most optimal solutions are (from best till rest):\n")
    for idx, (num_correct, num_incorrect, total_points) in enumerate(result, start=1):
        result_text.insert(tk.END, f"{idx}. {num_correct + num_incorrect} number of answers, with {num_correct} correct and {num_incorrect} incorrect\n")

# Create the main window
root = tk.Tk()
root.title("Optimal Strategy Calculator")

# Create and place input widgets
label_frame = ttk.LabelFrame(root, text="Input Parameters")
label_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

labels = ["Max Exam Points* (Default = 30.0):", "Number of Questions* (Default = 22):", 
          "Max Points* (Default = 60.0):", "Negative Penalty Percentage* (Default = 1/3):",
          "Minimum Point Percentage* (Default = 0.5):", "Current Points:"]
entries = []

max_exam_points_entry = ttk.Entry(label_frame, validate="key", validatecommand=(root.register(validate_entry), "%P"))
number_of_questions_entry = ttk.Entry(label_frame, validate="key", validatecommand=(root.register(validate_entry), "%P"))
max_points_entry = ttk.Entry(label_frame, validate="key", validatecommand=(root.register(validate_entry), "%P"))
negative_penalty_percentage_entry = ttk.Entry(label_frame, validate="key", validatecommand=(root.register(validate_entry), "%P"))
minimum_point_percentage_entry = ttk.Entry(label_frame, validate="key", validatecommand=(root.register(validate_entry), "%P"))
current_points_entry = ttk.Entry(label_frame)

max_exam_points_entry.grid(row=0, column=1)
number_of_questions_entry.grid(row=1, column=1)
max_points_entry.grid(row=2, column=1)
negative_penalty_percentage_entry.grid(row=3, column=1)
minimum_point_percentage_entry.grid(row=4, column=1)
current_points_entry.grid(row=5, column=1)


# Create and place the calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate_optimal_strategy)
calculate_button.grid(row=1, column=0, pady=10)

# Create and place the result text widget
result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=2, column=0, padx=10, pady=10)

# Add a footnote
footnote_label = ttk.Label(root, text="* Boxes can be skipped, if so default values will be used.")
footnote_label.grid(row=3, column=0, padx=10, pady=5)

# Run the main loop
root.mainloop()
