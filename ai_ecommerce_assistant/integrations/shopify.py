"""
Shopify integration module for the AI E-commerce Assistant.
"""

from typing import Dict, List, Optional
import shopify
from ..core import AIEcommerceAssistant
from ..config import config

class ShopifyIntegration:
    """
    Integration class for Shopify e-commerce platform.
    """

    def __init__(
        self,
        shop_url: Optional[str] = None,
        access_token: Optional[str] = None,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None
    ):
        """
        Initialize Shopify integration.

        Args:
            shop_url: Shopify store URL (optional, will use config if not provided)
            access_token: Shopify access token (optional, will use config if not provided)
            api_key: AI E-commerce Assistant API key (optional, will use config if not provided)
            api_secret: AI E-commerce Assistant API secret (optional, will use config if not provided)
        """
        # Get configuration from parameters or config
        shopify_config = config.get_platform_config("shopify")
        
        self.shop_url = shop_url or shopify_config.get("shop_url", "")
        self.access_token = access_token or shopify_config.get("access_token", "")
        self.api_key = api_key or config.AI_ASSISTANT_API_KEY
        self.api_secret = api_secret or config.AI_ASSISTANT_API_SECRET
        
        # Initialize AI assistant
        self.assistant = AIEcommerceAssistant(api_key=self.api_key)
        
        # Initialize Shopify API
        if self.shop_url and self.access_token and self.api_secret:
            shopify.Session.setup(api_key=self.api_secret, secret=self.api_secret)
            self.session = shopify.Session(
                self.shop_url, 
                shopify_config.get("api_version", "2023-01"), 
                self.access_token
            )
            shopify.ShopifyResource.activate_session(self.session)
        else:
            print("Warning: Shopify credentials not provided. Some features may be limited.")

    def sync_products(self) -> None:
        """
        Sync products from Shopify to the AI assistant.
        """
        if not hasattr(self, 'session'):
            raise AttributeError("Shopify session not initialized. Check your credentials.")
            
        products = shopify.Product.find()
        for product in products:
            product_data = {
                'id': str(product.id),
                'name': product.title,
                'description': product.body_html,
                'price': float(product.variants[0].price),
                'image_url': product.images[0].src if product.images else None,
                'category': product.product_type,
                'tags': product.tags.split(', ') if product.tags else []
            }
            self.assistant.recommendations.update_product_embeddings(product_data)

    def get_recommendations(
        self,
        customer_id: str,
        limit: Optional[int] = None
    ) -> List[Dict]:
        """
        Get product recommendations for a Shopify customer.

        Args:
            customer_id: Shopify customer ID
            limit: Maximum number of recommendations

        Returns:
            List of recommended products
        """
        if not hasattr(self, 'session'):
            raise AttributeError("Shopify session not initialized. Check your credentials.")
            
        # Get customer's order history
        orders = shopify.Order.find(customer_id=customer_id)
        purchase_history = []
        for order in orders:
            for item in order.line_items:
                purchase_history.append({
                    'product_id': str(item.product_id),
                    'quantity': item.quantity,
                    'price': float(item.price)
                })

        # Update user embeddings
        self.assistant.recommendations.update_user_embeddings(
            user_id=customer_id,
            purchase_history=purchase_history
        )

        # Get recommendations
        return self.assistant.get_recommendations(
            user_id=customer_id,
            limit=limit
        )

    def generate_product_content(
        self,
        product_id: str,
        content_type: str = "description"
    ) -> str:
        """
        Generate AI-powered content for a Shopify product.

        Args:
            product_id: Shopify product ID
            content_type: Type of content to generate

        Returns:
            Generated content
        """
        if not hasattr(self, 'session'):
            raise AttributeError("Shopify session not initialized. Check your credentials.")
            
        product = shopify.Product.find(product_id)
        keywords = product.tags.split(', ') if product.tags else []
        
        return self.assistant.generate_content(
            product_name=product.title,
            keywords=keywords,
            content_type=content_type
        )

    def analyze_product_reviews(
        self,
        product_id: str
    ) -> Dict:
        """
        Analyze sentiment of product reviews.

        Args:
            product_id: Shopify product ID

        Returns:
            Sentiment analysis results
        """
        if not hasattr(self, 'session'):
            raise AttributeError("Shopify session not initialized. Check your credentials.")
            
        # Get product reviews (requires Shopify Reviews app or custom implementation)
        reviews = []  # TODO: Implement review fetching
        sentiments = []
        
        for review in reviews:
            sentiment = self.assistant.analyze_sentiment(review.text)
            sentiments.append(sentiment)

        # Get sentiment thresholds from config
        threshold_positive = config.get_model_param("sentiment", "threshold_positive", 0.6)
        threshold_negative = config.get_model_param("sentiment", "threshold_negative", 0.4)

        # Aggregate sentiment analysis
        return {
            'average_sentiment': sum(s['score'] for s in sentiments) / len(sentiments) if sentiments else 0,
            'total_reviews': len(reviews),
            'sentiment_distribution': {
                'positive': len([s for s in sentiments if s['score'] > threshold_positive]),
                'neutral': len([s for s in sentiments if threshold_negative <= s['score'] <= threshold_positive]),
                'negative': len([s for s in sentiments if s['score'] < threshold_negative])
            }
        }

    def forecast_inventory(
        self,
        product_id: str,
        timeframe: str = "30d"
    ) -> Dict:
        """
        Generate inventory forecasts for a Shopify product.

        Args:
            product_id: Shopify product ID
            timeframe: Forecast timeframe

        Returns:
            Inventory forecast data
        """
        if not hasattr(self, 'session'):
            raise AttributeError("Shopify session not initialized. Check your credentials.")
            
        # Get historical sales data
        orders = shopify.Order.find(
            status='any',
            fields='id,line_items,created_at'
        )
        
        # Process sales data for forecasting
        sales_data = []
        for order in orders:
            for item in order.line_items:
                if str(item.product_id) == product_id:
                    sales_data.append({
                        'date': order.created_at,
                        'quantity': item.quantity
                    })

        # Get forecast from AI assistant
        return self.assistant.forecast_inventory(
            product_id=product_id,
            timeframe=timeframe
        )

    def handle_customer_support(
        self,
        customer_id: str,
        query: str
    ) -> Dict:
        """
        Handle customer support queries using AI.

        Args:
            customer_id: Shopify customer ID
            query: Customer query

        Returns:
            AI response
        """
        if not hasattr(self, 'session'):
            raise AttributeError("Shopify session not initialized. Check your credentials.")
            
        # Get customer context
        customer = shopify.Customer.find(customer_id)
        context = {
            'customer_name': f"{customer.first_name} {customer.last_name}",
            'order_count': len(customer.orders()),
            'total_spent': sum(float(order.total_price) for order in customer.orders())
        }

        return self.assistant.handle_customer_query(
            query=query,
            context=context
        )

    def process_abandoned_cart(
        self,
        customer_id: str
    ) -> Dict:
        """
        Process abandoned cart for a Shopify customer.

        Args:
            customer_id: Shopify customer ID

        Returns:
            Recovery suggestions
        """
        if not hasattr(self, 'session'):
            raise AttributeError("Shopify session not initialized. Check your credentials.")
            
        # Get abandoned cart data
        cart = shopify.Cart.find(customer_id=customer_id)
        cart_data = {
            'items': [
                {
                    'product_id': str(item.product_id),
                    'quantity': item.quantity,
                    'price': float(item.price)
                }
                for item in cart.line_items
            ],
            'total': float(cart.total_price)
        }

        return self.assistant.process_abandoned_cart(
            user_id=customer_id,
            cart_data=cart_data
        ) 