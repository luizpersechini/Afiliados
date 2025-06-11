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

# === CATEGORIAS DE INTERESSE ===
# Estas são as categorias que o bot vai monitorar
PRODUCT_CATEGORIES = [
    "Electronics",
    "Computers", 
    "Home & Kitchen",
    "Sports & Outdoors",
    "Books",
    "Health & Personal Care",
    "Tools & Home Improvement",
    "Fashion",
    "Beauty",
    "Toys & Games"
]

# === CONFIGURAÇÕES DE POSTS ===
# Horários ideais para postar (baseado em estudos de engagement)
BEST_POSTING_TIMES = {
    "twitter": [
        time(9, 0),   # 09:00
        time(12, 0),  # 12:00 
        time(15, 0),  # 15:00
        time(18, 0),  # 18:00
        time(21, 0)   # 21:00
    ],
    "telegram": [
        time(8, 0),   # 08:00
        time(12, 30), # 12:30
        time(19, 0)   # 19:00
    ],
    "threads": [
        time(10, 0),  # 10:00
        time(14, 0),  # 14:00
        time(20, 0)   # 20:00
    ],
    "bluesky": [
        time(11, 0),  # 11:00
        time(16, 0),  # 16:00
        time(22, 0)   # 22:00
    ]
}

# === LIMITES DE POSTS ===
MAX_POSTS_PER_DAY = {
    "twitter": 8,      # Twitter permite mais posts (50k seguidores)
    "telegram": 3,     # Telegram grupos preferem menos spam
    "threads": 5,      # Threads é mais casual (10k seguidores)
    "bluesky": 6       # Bluesky comunidade menor (10k seguidores)
}

# === CONFIGURAÇÕES DE DESCONTO ===
MIN_DISCOUNT_PERCENTAGE = 15  # Só posta se desconto >= 15%
MIN_PRODUCT_RATING = 4.0     # Só posta produtos bem avaliados
MIN_REVIEW_COUNT = 100       # Produtos com pelo menos 100 reviews

# === ANÁLISE DE PERFORMANCE ===
# Métricas para otimização
AUDIENCE_METRICS = {
    "instagram": 20000,    # 20k seguidores
    "twitter": 50000,      # 50k seguidores  
    "telegram": 1000,      # Estimativa do grupo
    "threads": 10000,      # 10k seguidores
    "bluesky": 10000,      # 10k seguidores
    "email_list": 5000     # Estimativa da lista de emails
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

print(f"✅ Configurações carregadas - {PROJECT_NAME} v{VERSION}")
print(f"🔧 Modo Debug: {'Ativado' if DEBUG_MODE else 'Desativado'}")
print(f"🎯 Tags de Afiliado configuradas para {len(AFFILIATE_TAGS)} canais")
print(f"🔑 Access Keys: {len(AMAZON_ACCESS_KEYS)} configuradas")
print(f"📊 Audiência total estimada: {sum(AUDIENCE_METRICS.values()):,} pessoas") 