from nltk.translate.bleu_score import sentence_bleu

# Define feedback thresholds
THRESHOLD_HIGH = 0.8
THRESHOLD_MEDIUM = 0.5

# Feedback messages
FEEDBACK_HIGH = "Excellent response! Your answer closely matches the reference answer."
FEEDBACK_MEDIUM = "Good effort! Your answer is somewhat similar to the reference answer."
FEEDBACK_LOW = "Keep practicing! Your answer needs improvement."

def evaluate_and_provide_feedback(reference_answer, student_answer):
    reference_tokens = reference_answer.split()
    student_tokens = student_answer.split()
    
    # Calculate BLEU score
    bleu_score = sentence_bleu([reference_tokens], student_tokens)
    
    # Provide feedback based on BLEU score
    if bleu_score >= THRESHOLD_HIGH:
        return FEEDBACK_HIGH
    elif bleu_score >= THRESHOLD_MEDIUM:
        return FEEDBACK_MEDIUM
    else:
        return FEEDBACK_LOW

# Example usage:
reference_answer = "The quick brown fox jumps over the lazy dog"
student_answer = "A quick brown fox jumps over a lazy dog"
feedback = evaluate_and_provide_feedback(reference_answer, student_answer)
print("Feedback:", feedback)
print('The perfect response would have been:', reference_answer)
