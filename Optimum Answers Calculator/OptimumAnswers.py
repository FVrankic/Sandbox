def checkOptimumNumberOfAnswers(maxExamPoints: float = 30,
                                numberOfQuestions: int = 22,
                                maxPoints: float = 60,
                                negativePenaltyPercentage: float = 1/3,
                                minimumPointPercentage: float = 0.5,
                                currentPoints: float = 0.0):

    goalPoints = maxPoints * minimumPointPercentage - currentPoints
    scaler = maxExamPoints / (numberOfQuestions - 2)  # -2 for the machine

    if (maxExamPoints + currentPoints) < (maxPoints * minimumPointPercentage):
        print("You are out.")
        return

    # Calculate the minimum number of correct answers needed
    minCorrectAnswers = int(round(goalPoints / scaler))

    # Generate all possible combinations of correct and incorrect answers
    combinations = []
    for numberOfCorrectQuestions in range(minCorrectAnswers, numberOfQuestions + 1):  # Fixed the range

        # Adjust the range for incorrect questions based on the total number of questions
        for incorrect in range(0, numberOfQuestions - numberOfCorrectQuestions + 1):
            totalPoints = (numberOfCorrectQuestions * 1 - incorrect * negativePenaltyPercentage) * scaler
            if totalPoints >= goalPoints:
                combinations.append((numberOfCorrectQuestions, incorrect, totalPoints))

    # Sort combinations based on the scaled total score (ascending order)
    combinations.sort(key=lambda x: x[2], reverse=False)

    # Print the results
    print("Statistically 10 most optimal solutions are (from best till rest):")
    for idx, (num_correct, num_incorrect, total_points) in enumerate(combinations, start=1):
        print(f"{idx}. {num_correct + num_incorrect} answers, with {num_correct} correct and {num_incorrect} incorrect")
        if idx > 10:
            break

# Example usage:
checkOptimumNumberOfAnswers(currentPoints=15.53)  # 10.53
