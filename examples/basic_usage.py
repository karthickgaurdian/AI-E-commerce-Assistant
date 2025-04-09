#!/usr/bin/env python
"""
Basic usage example for the AI E-commerce Assistant.
"""

import os
import sys
from dotenv import load_dotenv

# Add the parent directory to the path so we can import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Load environment variables
load_dotenv()

# Import the AI E-commerce Assistant
from ai_ecommerce_assistant import AIEcommerceAssistant

def main():
    """Run a basic example of the AI E-commerce Assistant."""
    print("Initializing AI E-commerce Assistant...")
    
    # Initialize the assistant
    assistant = AIEcommerceAssistant()
    
    # Test product recommendations
    print("\nTesting product recommendations...")
    try:
        recommendations = assistant.get_recommendations(
            user_id="test_user_123",
            product_id="test_product_456",
            limit=3
        )
        print(f"Recommendations: {recommendations}")
    except Exception as e:
        print(f"Error getting recommendations: {e}")
    
    # Test product search
    print("\nTesting product search...")
    try:
        search_results = assistant.search_products(
            query="blue summer dress",
            limit=3
        )
        print(f"Search results: {search_results}")
    except Exception as e:
        print(f"Error searching products: {e}")
    
    # Test content generation
    print("\nTesting content generation...")
    try:
        content = assistant.generate_content(
            product_name="Premium Coffee Maker",
            content_type="description"
        )
        print(f"Generated content: {content}")
    except Exception as e:
        print(f"Error generating content: {e}")
    
    # Test sentiment analysis
    print("\nTesting sentiment analysis...")
    try:
        sentiment = assistant.analyze_sentiment(
            text="This product is amazing! I love it so much."
        )
        print(f"Sentiment analysis: {sentiment}")
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
    
    print("\nBasic example completed!")

if __name__ == "__main__":
    main() 