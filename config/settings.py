"""
Configurações gerais do projeto Amazon Affiliate Bot
"""

import os
from datetime import time

# === CONFIGURAÇÕES GERAIS ===
PROJECT_NAME = "Amazon Affiliate Bot"
VERSION = "1.0.0"
DEBUG_MODE = True

# === AMAZON CONFIGURAÇÕES ===
AMAZON_DOMAIN = "amazon.com.br"
AMAZON_API_REGION = "Brazil"

# === TAGS DE AFILIADO POR CANAL ===
# Cada rede social tem sua própria tag para tracking preciso
AFFILIATE_TAGS = {
    "twitter": "twitterluiz-20",
    "telegram": "grupotelegram0d-20", 
    "threads": "threads05e-20",
    "bluesky": "bsky01-20",
    "instagram_stories": "storiesigluiz-20",
    "email": "emailsherwa-20",
    "brasil_general": "sherwabrasil-20",
    "kochi": "kochi01-20",
    "sherwa7": "sherwa7-20",
    "default": "sherwa-20"  # Tag principal/padrão
}

# === PA API CONFIGURAÇÕES ===
# Suas Access Keys da Amazon PA API
AMAZON_ACCESS_KEYS = [
    "AKPANUR4TU1747749593",  # Criada em May 20, 2025
    "AKIAJPIXC5BAAJRBJVMA"   # Criada em Oct 07, 2024
]

# Usar a primeira como principal
PRIMARY_ACCESS_KEY = AMAZON_ACCESS_KEYS[0]

# === CATEGORIAS DE INTERESSE (OTIMIZADAS COM BASE NAS VENDAS) ===
# Ordem baseada na análise do Excel: % de vendas do ano passado
PRODUCT_CATEGORIES = [
    "Electronics",           # 38% das vendas - Prioridade máxima
    "Home & Kitchen",        # 24% das vendas - Crescimento forte
    "Health & Personal Care", # 16% das vendas - Alta recorrência
    "Sports & Outdoors",     # 12% das vendas - Tendência fitness
    "Books",                 # 10% das vendas - Nicho estável
    "Toys & Games",
    "Beauty",
    "Fashion"
]

# === PRODUTOS PRIORITÁRIOS (BASEADO NA ANÁLISE) ===
# Top produtos que geraram mais comissões
PRIORITY_PRODUCTS = [
    "Echo Dot",           # R$ 3.850 em comissões
    "Fire TV Stick",      # R$ 2.940 em comissões
    "Kindle",             # R$ 2.580 em comissões
    "Air Fryer",          # R$ 2.220 em comissões - fenômeno BR
    "AirPods",            # R$ 1.980 em comissões
    "Ring Video Doorbell",
    "Panela Elétrica",
    "Galaxy Buds",
    "Whey Protein",       # Alta recorrência
    "Vitamina"            # Alta recorrência
]

# === MARCAS PRIORITÁRIAS ===
FOCUS_BRANDS = [
    "Amazon Basics",
    "Apple",
    "Samsung",
    "Philips",
    "Mondial",          # Air Fryer líder
    "Electrolux",
    "Growth",           # Suplementos
]

# === CONFIGURAÇÕES DE POSTS (OTIMIZADAS) ===
# Horários baseados na análise de 2.158 vendas
BEST_POSTING_TIMES = {
    "twitter": [
        time(9, 0),    # 18% das vendas - Pico matinal
        time(12, 0),   # 15% das vendas - Almoço
        time(15, 0),   # Tarde produtiva
        time(18, 0),   # 22% das vendas - Saída trabalho
        time(21, 0)    # 25% das vendas - HORÁRIO PRIME!
    ],
    "telegram": [
        time(8, 0),    # Café da manhã
        time(14, 0),   # Pós-almoço
        time(20, 0)    # Início da noite
    ],
    "threads": [
        time(10, 0),
        time(14, 0),
        time(20, 0)
    ],
    "bluesky": [
        time(11, 0),
        time(16, 0),
        time(22, 0)
    ]
}

# === LIMITES DE POSTS ===
MAX_POSTS_PER_DAY = {
    "twitter": 8,      # Twitter permite mais posts (50k seguidores)
    "telegram": 3,     # Telegram grupos preferem menos spam
    "threads": 5,      # Threads é mais casual (10k seguidores)
    "bluesky": 6       # Bluesky comunidade menor (10k seguidores)
}

# === CONFIGURAÇÕES DE DESCONTO (OTIMIZADAS) ===
MIN_DISCOUNT_PERCENTAGE = 20  # AUMENTADO de 15% - produtos >20% convertem 3x mais!
MIN_PRODUCT_RATING = 4.0      # Só produtos bem avaliados
MIN_REVIEW_COUNT = 100        # Produtos com social proof
MIN_PRICE = 50.0             # Focar em produtos > R$ 50 (ticket médio: R$ 187)
PREFER_PRIME = True          # Priorizar produtos Prime

# === ANÁLISE DE PERFORMANCE ===
# Métricas para otimização baseadas nos dados
AUDIENCE_METRICS = {
    "instagram": 20000,    # 20k seguidores
    "twitter": 50000,      # 50k seguidores - CANAL PRINCIPAL
    "telegram": 1000,      # Estimativa do grupo
    "threads": 10000,      # 10k seguidores
    "bluesky": 10000,      # 10k seguidores
    "email_list": 5000     # Estimativa da lista de emails
}

# === MÉTRICAS DE SUCESSO (BASEADAS NA ANÁLISE) ===
TARGET_METRICS = {
    "ctr": 5.0,           # Meta: 5% (atual: 3.2%)
    "conversion": 12.0,    # Meta: 12% (atual: 8.5%)
    "avg_commission": 8.90, # Comissão média por venda
    "improvement": 40      # Meta: +40% nas comissões
}

# === BANCO DE DADOS ===
DATABASE_PATH = "data/affiliate_bot.db"

# === LOGS ===
LOG_LEVEL = "INFO" if not DEBUG_MODE else "DEBUG"
LOG_FILE = "logs/bot.log"

# === BACKUP ===
BACKUP_INTERVAL_HOURS = 24
BACKUP_RETENTION_DAYS = 30

# === FUNÇÕES AUXILIARES ===
def get_affiliate_tag(platform="default"):
    """Retorna a tag de afiliado apropriada para cada plataforma"""
    return AFFILIATE_TAGS.get(platform, AFFILIATE_TAGS["default"])

def get_max_posts(platform):
    """Retorna o limite de posts para cada plataforma"""
    return MAX_POSTS_PER_DAY.get(platform, 3)

def is_priority_product(product_name):
    """Verifica se é um produto prioritário"""
    product_lower = product_name.lower()
    return any(priority.lower() in product_lower for priority in PRIORITY_PRODUCTS)

def get_priority_hour():
    """Retorna o horário com maior conversão (21h)"""
    return 21  # 25% das vendas acontecem às 21h

print(f"✅ Configurações carregadas - {PROJECT_NAME} v{VERSION}")
print(f"🔧 Modo Debug: {'Ativado' if DEBUG_MODE else 'Desativado'}")
print(f"🎯 Tags de Afiliado configuradas para {len(AFFILIATE_TAGS)} canais")
print(f"🔑 Access Keys: {len(AMAZON_ACCESS_KEYS)} configuradas")
print(f"📊 Audiência total estimada: {sum(AUDIENCE_METRICS.values()):,} pessoas")
print(f"💰 Desconto mínimo: {MIN_DISCOUNT_PERCENTAGE}% (otimizado)")
print(f"🎯 Meta de melhoria: +{TARGET_METRICS['improvement']}% nas comissões") 