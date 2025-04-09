# AI E-commerce Assistant

A modular AI-integrated library for e-commerce websites that provides intelligent features like personalized recommendations, smart search, dynamic pricing, and more.

## Features

- **Product Recommendations**: Personalized product suggestions using BERT embeddings
- **Smart Search**: Natural language search with semantic understanding
- **Dynamic Pricing**: AI-powered price optimization
- **Customer Support**: Automated responses to common queries
- **Content Generation**: AI-generated product descriptions and marketing copy
- **Inventory Forecasting**: Predictive inventory management
- **Sentiment Analysis**: Customer feedback analysis
- **Abandoned Cart Recovery**: Smart recovery strategies

## Prerequisites

### System Requirements

- **Operating System**: 
  - Windows 10/11
  - macOS 10.15+
  - Linux (Ubuntu 18.04+, CentOS 7+)
  - Any device that can run Python 3.8+

- **Hardware Requirements**:
  - CPU: 2+ cores recommended
  - RAM: 4GB minimum, 8GB recommended
  - Storage: 2GB free space minimum
  - GPU: Optional, but recommended for better performance

- **Software Requirements**:
  - Python 3.8 or higher
  - pip (Python package installer)
  - Git (for cloning the repository)

### Python Dependencies

The following Python packages will be installed automatically:
- numpy>=1.20.0
- pandas>=1.3.0
- scikit-learn>=1.0.0
- transformers>=4.15.0
- torch>=1.10.0
- fastapi>=0.70.0
- uvicorn>=0.15.0
- python-dotenv>=0.19.0
- redis>=4.0.0 (optional)
- sqlalchemy>=1.4.0
- shopify-python-api>=9.0.0 (optional)

### Optional Dependencies

For development and testing:
- pytest>=6.0.0
- pytest-cov>=2.12.0
- black>=21.9b0
- isort>=5.9.3
- flake8>=3.9.2

## Device Compatibility

### Desktop/Laptop
- **Windows**: Fully supported on Windows 10/11
- **macOS**: Fully supported on macOS 10.15+
- **Linux**: Fully supported on Ubuntu 18.04+, CentOS 7+, and other modern distributions

### Mobile Devices
- **Android**: Can run through Termux or similar terminal emulators
- **iOS**: Can run through Pythonista or similar Python environments
- **Note**: Mobile performance may be limited due to hardware constraints

### Cloud Platforms
- **AWS**: Compatible with EC2, Lambda, and other AWS services
- **Google Cloud**: Compatible with Compute Engine, Cloud Functions, and other GCP services
- **Azure**: Compatible with Virtual Machines, Functions, and other Azure services
- **Heroku**: Compatible with standard and performance dynos

### Containers
- **Docker**: Official Docker image available
- **Kubernetes**: Compatible with Kubernetes deployments

## Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-ecommerce-assistant.git
cd ai-ecommerce-assistant

# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package
pip install -e .
```

### 2. Local Setup

Create a `.env` file in the root directory with these minimal settings:

```env
# Use test API keys (already configured)
AI_ASSISTANT_API_KEY=test_key_123
AI_ASSISTANT_API_SECRET=test_secret_123

# Use SQLite database (no installation needed)
DATABASE_URL=sqlite:///ai_ecommerce.db

# Disable Redis caching for local development
USE_CACHE=False

# Enable features you want to test
ENABLE_RECOMMENDATIONS=True
ENABLE_SEARCH=True
ENABLE_SENTIMENT_ANALYSIS=True
```

### 3. Basic Usage

```python
from ai_ecommerce_assistant import AIEcommerceAssistant

# Initialize the assistant
assistant = AIEcommerceAssistant()

# Get product recommendations
recommendations = assistant.get_recommendations(
    user_id="user123",
    product_id="prod456",
    limit=5
)
print("Recommendations:", recommendations)

# Search products
results = assistant.search_products(
    query="blue summer dress",
    limit=10
)
print("Search results:", results)

# Generate product content
content = assistant.generate_content(
    product_name="Premium Coffee Maker",
    content_type="description"
)
print("Generated content:", content)
```

### 4. Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run all tests
pytest

# Run tests with coverage report
pytest --cov=ai_ecommerce_assistant

# Run specific test file
pytest tests/test_recommendations.py
```

## Installation on Different Devices

### Windows

1. Install Python 3.8+ from [python.org](https://www.python.org/downloads/)
2. Make sure to check "Add Python to PATH" during installation
3. Open Command Prompt or PowerShell
4. Follow the installation instructions above

### macOS

1. Install Python 3.8+ using Homebrew:
   ```bash
   brew install python
   ```
2. Open Terminal
3. Follow the installation instructions above

### Linux

1. Install Python 3.8+ using your package manager:
   ```bash
   # Ubuntu/Debian
   sudo apt update
   sudo apt install python3.8 python3.8-venv python3-pip
   
   # CentOS/RHEL
   sudo yum install python38 python38-devel
   ```
2. Open Terminal
3. Follow the installation instructions above

### Android (using Termux)

1. Install Termux from F-Droid or Google Play
2. Install Python:
   ```bash
   pkg update
   pkg install python
   ```
3. Follow the installation instructions above

### iOS (using Pythonista)

1. Install Pythonista from the App Store
2. Clone the repository using the built-in Git client
3. Install dependencies using pip
4. Follow the installation instructions above

### Docker

1. Install Docker from [docker.com](https://www.docker.com/products/docker-desktop)
2. Build the Docker image:
   ```bash
   docker build -t ai-ecommerce-assistant .
   ```
3. Run the container:
   ```bash
   docker run -it ai-ecommerce-assistant
   ```

## Local Development Guide

### Project Structure

```
ai-ecommerce-assistant/
├── ai_ecommerce_assistant/
│   ├── __init__.py
│   ├── core.py              # Core functionality
│   ├── api.py               # API endpoints
│   ├── config.py            # Configuration settings
│   ├── modules/             # Feature modules
│   │   ├── recommendations.py
│   │   └── ...
│   └── integrations/        # Platform integrations
│       ├── shopify.py
│       └── ...
├── examples/                # Usage examples
├── tests/                   # Test files
├── .env                     # Environment variables
├── pyproject.toml          # Project configuration
└── README.md
```

### Development Setup

1. **Python Version**: Python 3.8 or higher
2. **Virtual Environment**: Always use a virtual environment
3. **Code Style**: Follow PEP 8 guidelines
4. **Testing**: Write tests for new features

### Running Examples

1. **Basic Example**:
```bash
python examples/basic_usage.py
```

2. **Shopify Integration**:
```bash
python examples/shopify_integration.py
```

### Debugging

1. **Enable Debug Logging**:
Add to your `.env` file:
```env
LOG_LEVEL=DEBUG
```

2. **View Logs**:
```bash
# Logs are written to ai_ecommerce.log
tail -f ai_ecommerce.log
```

## Configuration Options

### Core Settings

| Setting | Description | Default |
|---------|-------------|---------|
| `AI_ASSISTANT_API_KEY` | API key for authentication | `test_key_123` |
| `AI_ASSISTANT_API_SECRET` | API secret for authentication | `test_secret_123` |
| `DATABASE_URL` | Database connection URL | `sqlite:///ai_ecommerce.db` |
| `USE_CACHE` | Enable/disable Redis caching | `True` |

### Feature Flags

| Feature | Description | Default |
|---------|-------------|---------|
| `ENABLE_RECOMMENDATIONS` | Enable product recommendations | `True` |
| `ENABLE_SEARCH` | Enable smart search | `True` |
| `ENABLE_DYNAMIC_PRICING` | Enable dynamic pricing | `True` |
| `ENABLE_CUSTOMER_SUPPORT` | Enable customer support | `True` |
| `ENABLE_CONTENT_GENERATION` | Enable content generation | `True` |
| `ENABLE_INVENTORY_FORECASTING` | Enable inventory forecasting | `True` |
| `ENABLE_SENTIMENT_ANALYSIS` | Enable sentiment analysis | `True` |
| `ENABLE_ABANDONED_CART` | Enable abandoned cart recovery | `True` |

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError: No module named 'ai_ecommerce_assistant'**
   - Solution: Make sure you've installed the package in development mode: `pip install -e .`

2. **Database connection errors**
   - Solution: Check your DATABASE_URL in .env file
   - For SQLite: Make sure the directory is writable

3. **Redis connection errors**
   - Solution: Either install Redis or set USE_CACHE=False in .env

4. **API key errors**
   - Solution: Make sure you're using the test keys or have valid API keys in .env

5. **Memory errors on low-end devices**
   - Solution: Reduce batch sizes and model complexity in config.py
   - Set `ENABLE_LARGE_MODELS=False` in .env

6. **GPU not detected**
   - Solution: Install CUDA drivers if using NVIDIA GPU
   - For CPU-only: Set `USE_GPU=False` in .env

### Getting Help

- Check the logs in `ai_ecommerce.log`
- Enable debug logging by setting `LOG_LEVEL=DEBUG` in .env
- Open an issue on GitHub with your error message and logs

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 