import json
import csv
import re

# Load JSON data
with open('data.json', encoding='utf-8-sig') as f:
    data = json.load(f)
# Burnout words list (from the thesaurus link)
burnout_words = ['exhaustion', 'fatigue', 'stress', 'overwork', 'depression', 'anxiety', 'frustration', 'pressure', 'strain']

# Initialize CSV writer for updated comments
csv_file_updated = open('updated_comments.csv', 'w', newline='', encoding='utf-8')
csv_writer_updated = csv.writer(csv_file_updated)
csv_writer_updated.writerow(['Issue/PR #', 'Comment #', 'Burnout', 'Team Members Agreement/Disagreement','Text'])

# Function to check for burnout words in a comment
def check_burnout(comment_body):
    for word in burnout_words:
        if re.search(r'\b' + re.escape(word) + r'\b', comment_body, flags=re.IGNORECASE):
            return 'Yes'
    return 'No'

# Process each issue/pull request
for issue_id, issue_data in data.items():
    comments = issue_data.get('comments', {})
    if comments:
        for comment_id, comment_data in comments.items():
            comment_body = comment_data.get('body', '')
            burnout_detection = check_burnout(comment_body)
            text = comment_data.get('title', '')+comment_body+burnout_detection
            csv_writer_updated.writerow([issue_id, comment_id, burnout_detection, '',text])

# Close CSV file for updated comments
csv_file_updated.close()

print("Updated comments saved to 'updated_comments.csv'.")