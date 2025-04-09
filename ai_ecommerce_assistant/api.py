"""
REST API interface for the AI E-commerce Assistant.
"""

from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel, Field
from .core import AIEcommerceAssistant

app = FastAPI(
    title="AI E-commerce Assistant API",
    description="REST API for AI-powered e-commerce features",
    version="0.1.0"
)

# Pydantic models for request/response validation
class RecommendationRequest(BaseModel):
    user_id: str
    limit: Optional[int] = Field(default=10, ge=1, le=100)
    context: Optional[Dict] = None

class SearchRequest(BaseModel):
    query: str
    filters: Optional[Dict] = None
    limit: Optional[int] = Field(default=20, ge=1, le=100)

class PricingRequest(BaseModel):
    product_id: str
    market_data: Optional[Dict] = None

class ContentRequest(BaseModel):
    product_name: str
    keywords: List[str]
    content_type: Optional[str] = "description"

class SentimentRequest(BaseModel):
    text: str

class InventoryRequest(BaseModel):
    product_id: str
    timeframe: Optional[str] = "30d"

class CustomerQueryRequest(BaseModel):
    query: str
    context: Optional[Dict] = None

class CartRequest(BaseModel):
    user_id: str
    cart_data: Dict

# Dependency for API key validation
async def verify_api_key(x_api_key: str = Header(...)):
    if not x_api_key:
        raise HTTPException(status_code=401, detail="API key is required")
    return x_api_key

# Initialize the AI assistant
assistant = None

@app.on_event("startup")
async def startup_event():
    global assistant
    # TODO: Load API key from environment variables
    assistant = AIEcommerceAssistant(api_key="your_api_key")

@app.get("/")
async def root():
    return {"message": "Welcome to AI E-commerce Assistant API"}

@app.post("/recommendations")
async def get_recommendations(
    request: RecommendationRequest,
    api_key: str = Depends(verify_api_key)
):
    """
    Get personalized product recommendations for a user.
    """
    try:
        recommendations = assistant.get_recommendations(
            user_id=request.user_id,
            limit=request.limit,
            context=request.context
        )
        return {"recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/search")
async def search_products(
    request: SearchRequest,
    api_key: str = Depends(verify_api_key)
):
    """
    Perform smart product search using NLP.
    """
    try:
        results = assistant.search_products(
            query=request.query,
            filters=request.filters,
            limit=request.limit
        )
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/pricing")
async def get_price_suggestions(
    request: PricingRequest,
    api_key: str = Depends(verify_api_key)
):
    """
    Get dynamic pricing suggestions for a product.
    """
    try:
        suggestions = assistant.get_price_suggestions(
            product_id=request.product_id,
            market_data=request.market_data
        )
        return {"suggestions": suggestions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/content")
async def generate_content(
    request: ContentRequest,
    api_key: str = Depends(verify_api_key)
):
    """
    Generate AI-powered content for products.
    """
    try:
        content = assistant.generate_content(
            product_name=request.product_name,
            keywords=request.keywords,
            content_type=request.content_type
        )
        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/sentiment")
async def analyze_sentiment(
    request: SentimentRequest,
    api_key: str = Depends(verify_api_key)
):
    """
    Analyze sentiment of customer feedback or reviews.
    """
    try:
        sentiment = assistant.analyze_sentiment(text=request.text)
        return {"sentiment": sentiment}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/inventory")
async def forecast_inventory(
    request: InventoryRequest,
    api_key: str = Depends(verify_api_key)
):
    """
    Generate inventory forecasts.
    """
    try:
        forecast = assistant.forecast_inventory(
            product_id=request.product_id,
            timeframe=request.timeframe
        )
        return {"forecast": forecast}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/support")
async def handle_customer_query(
    request: CustomerQueryRequest,
    api_key: str = Depends(verify_api_key)
):
    """
    Handle customer support queries using AI.
    """
    try:
        response = assistant.handle_customer_query(
            query=request.query,
            context=request.context
        )
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/cart")
async def process_abandoned_cart(
    request: CartRequest,
    api_key: str = Depends(verify_api_key)
):
    """
    Process abandoned cart and generate recovery suggestions.
    """
    try:
        suggestions = assistant.process_abandoned_cart(
            user_id=request.user_id,
            cart_data=request.cart_data
        )
        return {"suggestions": suggestions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def create_app():
    """
    Create and configure the FastAPI application.
    """
    return app 