import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Number of respondents requested by user
n = 351

def likert():
    return np.random.randint(1, 6, n)

data = {
    # 32 Questionnaire Items
    "CI1": likert(), "CI2": likert(), "CI3": likert(), "CI4": likert(),
    "PC1": likert(), "PC2": likert(), "PC3": likert(), "PC4": likert(),
    "PLE1": likert(), "PLE2": likert(), "PLE3": likert(), "PLE4": likert(),
    "PBU1": likert(), "PBU2": likert(), "PBU3": likert(), "PBU4": likert(),
    "IT1": likert(), "IT2": likert(), "IT3": likert(), "IT4": likert(),
    "RI1": likert(), "RI2": likert(), "RI3": likert(), "RI4": likert(),
    "DSE1": likert(), "DSE2": likert(), "DSE3": likert(), "DSE4": likert(),
    "PR1": likert(), "PR2": likert(), "PR3": likert(), "PR4": likert(),

    # Demographics & Control Variables
    "Age": np.random.randint(21, 60, n),
    "Gender": np.random.choice(["Male", "Female"], n),
    "Education": np.random.choice(
        ["Primary", "Secondary", "Higher Secondary", "Graduate"], n),
    "Years_Business": np.random.randint(1, 25, n),
    "Years_UPI_Usage": np.random.randint(1, 8, n)
}

# Create DataFrame
df = pd.DataFrame(data)

# Export to Excel
output_path = "/Users/rishabpjain/Downloads/eq-analytics-terminal/UPI_Santhal_351_Responses.xlsx"
df.to_excel(output_path, index=False)

print(f"Dataset successfully generated with shape: {df.shape}")
print(f"Saved to: {output_path}")
