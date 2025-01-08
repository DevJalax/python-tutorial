import re
import nltk
from textblob import TextBlob
from datetime import datetime, timedelta

# Sample review data structure
reviews = [
    {"rating": 5, "date": "2025-01-05", "text": "Great product, very happy with it!", "platform": "Amazon"},
    {"rating": 3, "date": "2025-01-06", "text": "It's good, but the battery life could be better.", "platform": "Amazon"},
    {"rating": 1, "date": "2024-12-01", "text": "Worst experience ever! The product broke after a week.", "platform": "Amazon"},
    {"rating": 4, "date": "2024-11-30", "text": "Good value for money, would recommend.", "platform": "Yelp"},
    {"rating": 2, "date": "2024-12-20", "text": "Not as described. The quality was poor.", "platform": "Yelp"}
]

# 1. Filter by recent reviews (e.g., reviews from the last 30 days)
def filter_recent_reviews(reviews, days=30):
    recent_reviews = []
    threshold_date = datetime.now() - timedelta(days=days)
    for review in reviews:
        review_date = datetime.strptime(review["date"], "%Y-%m-%d")
        if review_date >= threshold_date:
            recent_reviews.append(review)
    return recent_reviews

# 2. Look for patterns (e.g., mention of common pros/cons)
def find_patterns(reviews):
    pros = ["good", "excellent", "happy", "great", "love"]
    cons = ["bad", "poor", "worst", "disappointed", "broke"]
    
    pattern_results = {"pros": [], "cons": []}
    
    for review in reviews:
        text = review["text"].lower()
        for word in pros:
            if word in text:
                pattern_results["pros"].append(review)
                break
        for word in cons:
            if word in text:
                pattern_results["cons"].append(review)
                break
    
    return pattern_results

# 3. Check for red flags (e.g., overly generic language)
def check_generic_reviews(reviews):
    generic_phrases = ["great product", "would recommend", "good value", "happy with it"]
    flagged_reviews = []
    
    for review in reviews:
        for phrase in generic_phrases:
            if phrase in review["text"].lower():
                flagged_reviews.append(review)
                break
                
    return flagged_reviews

# 4. Compare across platforms (manually, just compare reviews by platform)
def compare_across_platforms(reviews):
    platforms = {}
    for review in reviews:
        platform = review["platform"]
        if platform not in platforms:
            platforms[platform] = []
        platforms[platform].append(review)
    return platforms

# 5. Sort reviews by star rating
def sort_reviews_by_rating(reviews):
    return sorted(reviews, key=lambda x: x["rating"], reverse=True)

# 6. Sentiment analysis for emotional language (positive/negative sentiment)
def analyze_sentiment(reviews):
    sentiment_results = {"positive": [], "negative": []}
    
    for review in reviews:
        blob = TextBlob(review["text"])
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            sentiment_results["positive"].append(review)
        elif sentiment < 0:
            sentiment_results["negative"].append(review)
    
    return sentiment_results

# Main function to apply all checks
def analyze_reviews(reviews):
    # Apply the different checks
    recent_reviews = filter_recent_reviews(reviews)
    pattern_results = find_patterns(reviews)
    flagged_reviews = check_generic_reviews(reviews)
    platform_comparison = compare_across_platforms(reviews)
    sorted_reviews = sort_reviews_by_rating(reviews)
    sentiment_analysis = analyze_sentiment(reviews)
    
    print("Recent Reviews (Last 30 Days):", recent_reviews)
    print("Pattern Results (Pros and Cons):", pattern_results)
    print("Flagged Generic Reviews:", flagged_reviews)
    print("Reviews by Platform:", platform_comparison)
    print("Sorted Reviews by Rating:", sorted_reviews)
    print("Sentiment Analysis (Positive/Negative):", sentiment_analysis)

# Run the analysis
analyze_reviews(reviews)
