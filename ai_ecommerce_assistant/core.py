"""
Core module containing the main AIEcommerceAssistant class.
"""

from typing import Dict, List, Optional, Union

from .modules.recommendations import RecommendationEngine
from .modules.search import SmartSearch
from .modules.pricing import DynamicPricing
from .modules.support import CustomerSupport
from .modules.content import ContentGenerator
from .modules.inventory import InventoryManager
from .modules.sentiment import SentimentAnalyzer
from .modules.cart import CartRecovery
from .config import config

class AIEcommerceAssistant:
    """
    Main class for the AI E-commerce Assistant.
    Provides a unified interface to all AI-powered e-commerce features.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        config_dict: Optional[Dict] = None
    ):
        """
        Initialize the AI E-commerce Assistant.

        Args:
            api_key: API key for authentication (optional, will use config if not provided)
            config_dict: Optional configuration dictionary to override defaults
        """
        # Use provided API key or get from config
        self.api_key = api_key or config.AI_ASSISTANT_API_KEY
        
        # Use provided config or default to global config
        self.config = config_dict or {}
        
        # Initialize enabled modules based on feature flags
        if config.is_feature_enabled("recommendations"):
            self.recommendations = RecommendationEngine(self.api_key, self.config)
        
        if config.is_feature_enabled("smart_search"):
            self.search = SmartSearch(self.api_key, self.config)
        
        if config.is_feature_enabled("dynamic_pricing"):
            self.pricing = DynamicPricing(self.api_key, self.config)
        
        if config.is_feature_enabled("customer_support"):
            self.support = CustomerSupport(self.api_key, self.config)
        
        if config.is_feature_enabled("content_generation"):
            self.content = ContentGenerator(self.api_key, self.config)
        
        if config.is_feature_enabled("inventory_forecasting"):
            self.inventory = InventoryManager(self.api_key, self.config)
        
        if config.is_feature_enabled("sentiment_analysis"):
            self.sentiment = SentimentAnalyzer(self.api_key, self.config)
        
        if config.is_feature_enabled("cart_recovery"):
            self.cart = CartRecovery(self.api_key, self.config)

    def get_recommendations(
        self,
        user_id: str,
        limit: Optional[int] = None,
        context: Optional[Dict] = None
    ) -> List[Dict]:
        """
        Get personalized product recommendations for a user.

        Args:
            user_id: Unique identifier for the user
            limit: Maximum number of recommendations to return
            context: Optional context information (e.g., current page, search query)

        Returns:
            List of recommended products with scores
        """
        if not hasattr(self, 'recommendations'):
            raise AttributeError("Recommendations feature is not enabled")
            
        # Use config default if limit not provided
        if limit is None:
            limit = config.get_model_param("recommendations", "max_recommendations", 10)
            
        return self.recommendations.get_recommendations(user_id, limit, context)

    def search_products(
        self,
        query: str,
        filters: Optional[Dict] = None,
        limit: Optional[int] = None
    ) -> List[Dict]:
        """
        Perform smart product search using NLP.

        Args:
            query: Search query string
            filters: Optional filters to apply
            limit: Maximum number of results to return

        Returns:
            List of matching products with relevance scores
        """
        if not hasattr(self, 'search'):
            raise AttributeError("Smart search feature is not enabled")
            
        # Use config default if limit not provided
        if limit is None:
            limit = config.get_model_param("search", "max_results", 20)
            
        return self.search.search_products(query, filters, limit)

    def get_price_suggestions(
        self,
        product_id: str,
        market_data: Optional[Dict] = None
    ) -> Dict:
        """
        Get dynamic pricing suggestions for a product.

        Args:
            product_id: Unique identifier for the product
            market_data: Optional market data to consider

        Returns:
            Dictionary containing price suggestions and rationale
        """
        if not hasattr(self, 'pricing'):
            raise AttributeError("Dynamic pricing feature is not enabled")
            
        return self.pricing.get_suggestions(product_id, market_data)

    def generate_content(
        self,
        product_name: str,
        keywords: List[str],
        content_type: str = "description"
    ) -> str:
        """
        Generate AI-powered content for products.

        Args:
            product_name: Name of the product
            keywords: List of relevant keywords
            content_type: Type of content to generate (description, title, etc.)

        Returns:
            Generated content string
        """
        if not hasattr(self, 'content'):
            raise AttributeError("Content generation feature is not enabled")
            
        return self.content.generate(product_name, keywords, content_type)

    def analyze_sentiment(self, text: str) -> Dict:
        """
        Analyze sentiment of customer feedback or reviews.

        Args:
            text: Text to analyze

        Returns:
            Dictionary containing sentiment analysis results
        """
        if not hasattr(self, 'sentiment'):
            raise AttributeError("Sentiment analysis feature is not enabled")
            
        return self.sentiment.analyze(text)

    def forecast_inventory(
        self,
        product_id: str,
        timeframe: str = "30d"
    ) -> Dict:
        """
        Generate inventory forecasts.

        Args:
            product_id: Unique identifier for the product
            timeframe: Forecast timeframe (e.g., "30d", "90d")

        Returns:
            Dictionary containing forecast data
        """
        if not hasattr(self, 'inventory'):
            raise AttributeError("Inventory forecasting feature is not enabled")
            
        return self.inventory.forecast(product_id, timeframe)

    def handle_customer_query(
        self,
        query: str,
        context: Optional[Dict] = None
    ) -> Dict:
        """
        Handle customer support queries using AI.

        Args:
            query: Customer query text
            context: Optional context information

        Returns:
            Dictionary containing response and confidence score
        """
        if not hasattr(self, 'support'):
            raise AttributeError("Customer support feature is not enabled")
            
        return self.support.handle_query(query, context)

    def process_abandoned_cart(
        self,
        user_id: str,
        cart_data: Dict
    ) -> Dict:
        """
        Process abandoned cart and generate recovery suggestions.

        Args:
            user_id: Unique identifier for the user
            cart_data: Dictionary containing cart information

        Returns:
            Dictionary containing recovery suggestions and actions
        """
        if not hasattr(self, 'cart'):
            raise AttributeError("Cart recovery feature is not enabled")
            
        return self.cart.process_abandoned_cart(user_id, cart_data) 