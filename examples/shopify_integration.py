"""
Example script demonstrating the Shopify integration.
"""

import os
from dotenv import load_dotenv
from ai_ecommerce_assistant.integrations.shopify import ShopifyIntegration
from ai_ecommerce_assistant.config import config

# Load environment variables
load_dotenv()

def main():
    # Initialize Shopify integration using configuration
    shopify = ShopifyIntegration()
    
    # Check if Shopify is properly configured
    if not config.get_platform_config("shopify").get("shop_url"):
        print("Warning: Shopify configuration not found. Using test mode.")
        print("To use Shopify features, set SHOPIFY_SHOP_URL and SHOPIFY_ACCESS_TOKEN in your .env file.")
        return
    
    # Sync products
    print("Syncing products...")
    try:
        shopify.sync_products()
        print("Products synced successfully!")
    except AttributeError as e:
        print(f"Error syncing products: {e}")
        return

    # Example customer ID
    customer_id = "123456789"

    # Get product recommendations
    print("\nGetting product recommendations...")
    try:
        recommendations = shopify.get_recommendations(customer_id)
        print("Top 5 recommendations:")
        for i, rec in enumerate(recommendations[:5], 1):
            print(f"{i}. {rec['name']} (Score: {rec['score']:.2f})")
    except AttributeError as e:
        print(f"Error getting recommendations: {e}")

    # Generate product content
    print("\nGenerating product content...")
    product_id = "987654321"
    try:
        description = shopify.generate_product_content(product_id)
        print(f"Generated description:\n{description}")
    except AttributeError as e:
        print(f"Error generating content: {e}")

    # Analyze product reviews
    print("\nAnalyzing product reviews...")
    try:
        sentiment = shopify.analyze_product_reviews(product_id)
        print(f"Average sentiment: {sentiment['average_sentiment']:.2f}")
        print(f"Total reviews: {sentiment['total_reviews']}")
        print("Sentiment distribution:", sentiment['sentiment_distribution'])
    except AttributeError as e:
        print(f"Error analyzing reviews: {e}")

    # Forecast inventory
    print("\nForecasting inventory...")
    try:
        forecast = shopify.forecast_inventory(product_id)
        print("Forecast results:", forecast)
    except AttributeError as e:
        print(f"Error forecasting inventory: {e}")

    # Handle customer support
    print("\nHandling customer support query...")
    query = "When will my order arrive?"
    try:
        response = shopify.handle_customer_support(customer_id, query)
        print(f"AI Response: {response['response']}")
    except AttributeError as e:
        print(f"Error handling customer support: {e}")

    # Process abandoned cart
    print("\nProcessing abandoned cart...")
    try:
        suggestions = shopify.process_abandoned_cart(customer_id)
        print("Recovery suggestions:", suggestions)
    except AttributeError as e:
        print(f"Error processing abandoned cart: {e}")

if __name__ == "__main__":
    main() 