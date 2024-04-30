import json
import csv
from textblob import TextBlob

# Load JSON data
with open('data.json', encoding='utf-8-sig') as f:
    data = json.load(f)

# Initialize CSV writer
csv_file = open('sentiment_analysis_results.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Issue/PR #', 'Comment #', 'User', 'Comment Body', 'Sentiment'])

# Function to perform sentiment analysis
def analyze_sentiment(comment):
    analysis = TextBlob(comment)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Process each issue/pull request
for issue_id, issue_data in data.items():
    comments = issue_data.get('comments', {})
    if comments:
        title = issue_data.get('title', 'No Title')
        body = issue_data.get('body', 'No Body')
        for comment_id, comment_data in comments.items():
            user = comment_data.get('userlogin', 'Unknown User')
            comment_body = comment_data.get('body', 'No Comment Body')
            sentiment = analyze_sentiment(comment_body)
            csv_writer.writerow([issue_id, comment_id, user, comment_body, sentiment])

# Close CSV file
csv_file.close()