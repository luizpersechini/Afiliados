"""
Amazon Product Monitor
Monitora produtos com desconto usando a Amazon PA API
"""

import sys
import os
import logging
from datetime import datetime, timedelta
import time as time_module

# Adiciona o diretório raiz ao path para importar config
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from config.settings import *
from config.api_keys import get_amazon_credentials

# Setup de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AmazonProductMonitor:
    """Monitor de produtos da Amazon usando PA API"""
    
    def __init__(self, platform="default"):
        """
        Inicializa o monitor para uma plataforma específica
        
        Args:
            platform (str): Plataforma para usar a tag correta
        """
        self.platform = platform
        self.credentials = get_amazon_credentials(platform)
        self.affiliate_tag = self.credentials["associate_tag"]
        
        logger.info(f"🔍 Monitor iniciado para {platform}")
        logger.info(f"🏷️  Usando tag: {self.affiliate_tag}")
    
    def search_products_by_category(self, category, max_results=10):
        """
        Busca produtos em uma categoria específica
        
        Args:
            category (str): Categoria para buscar
            max_results (int): Máximo de resultados
            
        Returns:
            list: Lista de produtos encontrados
        """
        # NOTA: Este é um exemplo simplificado
        # A implementação real da PA API requer autenticação complexa
        
        logger.info(f"🔍 Buscando produtos em: {category}")
        
        # Exemplo de estrutura de produto que retornaremos
        mock_products = [
            {
                "title": f"Produto Exemplo {category}",
                "price": "R$ 199,90",
                "original_price": "R$ 299,90", 
                "discount_percentage": 33,
                "rating": 4.5,
                "review_count": 150,
                "image_url": "https://example.com/image.jpg",
                "product_url": "https://amazon.com.br/product/123",
                "category": category,
                "is_prime": True,
                "found_at": datetime.now().isoformat()
            }
        ]
        
        return mock_products
    
    def filter_products_by_criteria(self, products):
        """
        Filtra produtos baseado nos critérios configurados
        
        Args:
            products (list): Lista de produtos para filtrar
            
        Returns:
            list: Produtos que atendem aos critérios
        """
        filtered = []
        
        for product in products:
            # Verifica desconto mínimo
            if product.get("discount_percentage", 0) < MIN_DISCOUNT_PERCENTAGE:
                continue
                
            # Verifica rating mínimo
            if product.get("rating", 0) < MIN_PRODUCT_RATING:
                continue
                
            # Verifica número de reviews
            if product.get("review_count", 0) < MIN_REVIEW_COUNT:
                continue
            
            # Produto passou em todos os filtros
            filtered.append(product)
            
        logger.info(f"✅ {len(filtered)}/{len(products)} produtos passaram nos filtros")
        return filtered
    
    def create_affiliate_link(self, product_url):
        """
        Cria link de afiliado para um produto
        
        Args:
            product_url (str): URL original do produto
            
        Returns:
            str: URL com tag de afiliado
        """
        # Implementação simplificada
        if "?" in product_url:
            separator = "&"
        else:
            separator = "?"
            
        affiliate_link = f"{product_url}{separator}tag={self.affiliate_tag}"
        
        logger.info(f"🔗 Link de afiliado criado para {self.platform}")
        return affiliate_link
    
    def scan_for_deals(self, categories=None):
        """
        Escaneia categorias em busca de ofertas
        
        Args:
            categories (list): Lista de categorias para escanear
            
        Returns:
            dict: Resultados organizados por categoria
        """
        if categories is None:
            categories = PRODUCT_CATEGORIES
            
        results = {}
        
        logger.info(f"🎯 Iniciando escaneamento de {len(categories)} categorias")
        
        for category in categories:
            try:
                # Busca produtos na categoria
                products = self.search_products_by_category(category)
                
                # Filtra por critérios
                filtered_products = self.filter_products_by_criteria(products)
                
                # Adiciona links de afiliado
                for product in filtered_products:
                    product["affiliate_link"] = self.create_affiliate_link(
                        product["product_url"]
                    )
                
                results[category] = filtered_products
                
                # Pausa entre requisições para não sobrecarregar
                time_module.sleep(1)
                
            except Exception as e:
                logger.error(f"❌ Erro ao processar categoria {category}: {e}")
                continue
        
        total_deals = sum(len(deals) for deals in results.values())
        logger.info(f"🎉 Escaneamento concluído: {total_deals} ofertas encontradas")
        
        return results
    
    def get_trending_products(self, limit=5):
        """
        Busca produtos em tendência (simulado)
        
        Args:
            limit (int): Número máximo de produtos
            
        Returns:
            list: Produtos em tendência
        """
        logger.info(f"📈 Buscando {limit} produtos em tendência")
        
        # Simulação de produtos trending
        trending = [
            {
                "title": "iPhone 15 Pro Max",
                "category": "Electronics",
                "discount_percentage": 18,
                "why_trending": "Black Friday chegando"
            },
            {
                "title": "Air Fryer Mondial",
                "category": "Home & Kitchen", 
                "discount_percentage": 25,
                "why_trending": "Muito procurado"
            }
        ]
        
        return trending[:limit]

# Função de teste
def test_monitor():
    """Testa o monitor de produtos"""
    print("🧪 TESTANDO MONITOR DE PRODUTOS AMAZON")
    print("=" * 50)
    
    # Testa monitor para Twitter (audiência maior)
    monitor = AmazonProductMonitor("twitter")
    
    # Testa busca de ofertas
    deals = monitor.scan_for_deals(["Electronics", "Home & Kitchen"])
    
    print(f"\n📊 RESULTADOS:")
    for category, products in deals.items():
        print(f"\n🏷️  {category}: {len(products)} ofertas")
        for product in products:
            print(f"   📦 {product['title']}")
            print(f"   💰 {product['price']} ({product['discount_percentage']}% OFF)")
            print(f"   🔗 {product['affiliate_link'][:50]}...")
    
    # Testa produtos trending
    trending = monitor.get_trending_products()
    print(f"\n📈 PRODUTOS EM TENDÊNCIA:")
    for product in trending:
        print(f"   🔥 {product['title']} ({product['discount_percentage']}% OFF)")

if __name__ == "__main__":
    test_monitor() 