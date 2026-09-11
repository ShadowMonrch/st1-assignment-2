# AI Usage

## AI Tool Used

Microsoft Copilot

## Part C – Code Analysis

I asked Microsoft Copilot to act as a Python tutor and explain the code, identify potential problems, avoid providing a complete replacement, and ask questions that would help me reason about the solution.

The AI identified several issues:
- The `appointments` list must already exist before the function is called.
- Only the patient name is validated.
- The practitioner name and appointment time are not validated.
- The function does not return the created appointment.

I reviewed these suggestions rather than accepting them automatically. I checked the code and tested the program to verify the behaviour.

## Part D – AI-Generated Function

I asked Microsoft Copilot to create a simple beginner-friendly Python function that stores a patient name, practitioner name and appointment time. I specified that it should not use a database or GUI and should explain what the function does.

The AI-generated code was kept separate from my human-written version so that I could compare the two approaches.

## Verification

I verified the AI suggestions by:
- Running the program with a normal appointment.
- Testing a blank patient name.
- Testing duplicate appointments for the same practitioner and time.
- Testing unusual `None` values.
- Comparing the AI suggestions with the assignment requirements.

## Final Decision

I did not automatically use the AI-generated code. I used the AI output to help identify problems and understand possible improvements. I made my own decision about what to change and added one controlled improvement: validation for an empty practitioner name.