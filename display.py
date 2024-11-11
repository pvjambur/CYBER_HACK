import pandas as pd

# Load the CSV file
file_path = 'train.csv'  # Replace with your CSV file path
df = pd.read_csv(file_path)

# Group by category and sub_category to count the occurrences
category_counts = df.groupby(['category', 'sub_category']).size().reset_index(name='count')

# Sort values by category and sub_category for better readability
category_counts = category_counts.sort_values(by=['category', 'sub_category']).reset_index(drop=True)

# Display with formatting
def display_category_counts(category_counts):
    # Get unique categories
    unique_categories = category_counts['category'].unique()
    
    # Print header
    print(f"{'Category':<20} {'Sub-Category':<20} {'Count':<10}")
    print("-" * 50)
    
    # Loop through each category
    for category in unique_categories:
        # Filter sub-categories for the current category
        sub_category_data = category_counts[category_counts['category'] == category]
        
        # Display category name (once per unique category)
        print(f"{category:<20}")
        
        # Loop through sub-categories and counts
        for _, row in sub_category_data.iterrows():
            print(f"{'':<20} {row['sub_category']:<20} {row['count']:<10}")
        
        # Separator line between categories for readability
        print("-" * 50)

# Call the function to display results
display_category_counts(category_counts)
