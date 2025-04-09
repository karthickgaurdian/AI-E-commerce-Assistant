"""
Configuration module for the AI E-commerce Assistant.
Centralizes all configuration settings, URLs, and API keys.
"""

import os
from typing import Dict, Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """
    Configuration class for the AI E-commerce Assistant.
    """
    
    # AI Assistant API credentials
    AI_ASSISTANT_API_KEY = os.getenv("AI_ASSISTANT_API_KEY", "test_key_123")
    AI_ASSISTANT_API_SECRET = os.getenv("AI_ASSISTANT_API_SECRET", "test_secret_123")
    
    # Model configurations
    BERT_MODEL_NAME = os.getenv("BERT_MODEL_NAME", "bert-base-uncased")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")
    
    # Database configuration
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///ai_ecommerce.db")
    
    # Cache configuration
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    USE_CACHE = os.getenv("USE_CACHE", "False").lower() == "true"
    
    # E-commerce platform configurations
    SHOPIFY_CONFIG = {
        "shop_url": os.getenv("SHOPIFY_SHOP_URL", ""),
        "access_token": os.getenv("SHOPIFY_ACCESS_TOKEN", ""),
        "api_version": os.getenv("SHOPIFY_API_VERSION", "2023-01"),
    }
    
    # API endpoints
    API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
    API_VERSION = os.getenv("API_VERSION", "v1")
    
    # Feature flags
    FEATURES = {
        "recommendations": os.getenv("ENABLE_RECOMMENDATIONS", "True").lower() == "true",
        "smart_search": os.getenv("ENABLE_SMART_SEARCH", "True").lower() == "true",
        "dynamic_pricing": os.getenv("ENABLE_DYNAMIC_PRICING", "True").lower() == "true",
        "customer_support": os.getenv("ENABLE_CUSTOMER_SUPPORT", "True").lower() == "true",
        "content_generation": os.getenv("ENABLE_CONTENT_GENERATION", "True").lower() == "true",
        "inventory_forecasting": os.getenv("ENABLE_INVENTORY_FORECASTING", "True").lower() == "true",
        "sentiment_analysis": os.getenv("ENABLE_SENTIMENT_ANALYSIS", "True").lower() == "true",
        "cart_recovery": os.getenv("ENABLE_CART_RECOVERY", "True").lower() == "true",
    }
    
    # Model parameters
    MODEL_PARAMS = {
        "recommendations": {
            "embedding_size": int(os.getenv("RECOMMENDATION_EMBEDDING_SIZE", "768")),
            "max_recommendations": int(os.getenv("MAX_RECOMMENDATIONS", "10")),
        },
        "search": {
            "max_results": int(os.getenv("MAX_SEARCH_RESULTS", "20")),
            "min_score": float(os.getenv("MIN_SEARCH_SCORE", "0.5")),
        },
        "sentiment": {
            "threshold_positive": float(os.getenv("SENTIMENT_THRESHOLD_POSITIVE", "0.6")),
            "threshold_negative": float(os.getenv("SENTIMENT_THRESHOLD_NEGATIVE", "0.4")),
        },
    }
    
    @classmethod
    def get_api_url(cls, endpoint: str) -> str:
        """
        Get the full API URL for an endpoint.
        
        Args:
            endpoint: API endpoint path
            
        Returns:
            Full API URL
        """
        return f"{cls.API_BASE_URL}/{cls.API_VERSION}/{endpoint}"
    
    @classmethod
    def is_feature_enabled(cls, feature: str) -> bool:
        """
        Check if a feature is enabled.
        
        Args:
            feature: Feature name
            
        Returns:
            True if the feature is enabled, False otherwise
        """
        return cls.FEATURES.get(feature, False)
    
    @classmethod
    def get_model_param(cls, model: str, param: str, default: any = None) -> any:
        """
        Get a model parameter.
        
        Args:
            model: Model name
            param: Parameter name
            default: Default value if parameter is not found
            
        Returns:
            Parameter value
        """
        return cls.MODEL_PARAMS.get(model, {}).get(param, default)
    
    @classmethod
    def get_platform_config(cls, platform: str) -> Dict:
        """
        Get configuration for a specific e-commerce platform.
        
        Args:
            platform: Platform name (e.g., 'shopify')
            
        Returns:
            Platform configuration dictionary
        """
        if platform.lower() == "shopify":
            return cls.SHOPIFY_CONFIG
        return {}
    
    @classmethod
    def validate_config(cls) -> bool:
        """
        Validate the configuration.
        
        Returns:
            True if configuration is valid, False otherwise
        """
        # Check required API keys
        if not cls.AI_ASSISTANT_API_KEY or cls.AI_ASSISTANT_API_KEY == "test_key_123":
            print("Warning: Using test API key. Some features may be limited.")
        
        # Check database connection
        if cls.DATABASE_URL.startswith("sqlite"):
            print("Warning: Using SQLite database. Not recommended for production.")
        
        # Check Redis connection
        if not cls.REDIS_URL or cls.REDIS_URL == "redis://localhost:6379/0":
            print("Warning: Using default Redis URL. Make sure Redis is running.")
        
        return True

# Create a global config instance
config = Config()

# Validate configuration on import
config.validate_config() 