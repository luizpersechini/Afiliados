"""
Chaves de API para redes sociais e serviços
IMPORTANTE: Este arquivo deve ser mantido privado!
"""

import os
from config.settings import AMAZON_ACCESS_KEYS, PRIMARY_ACCESS_KEY, get_affiliate_tag

# Tentamos carregar dotenv, mas se não funcionar, continuamos sem ele
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ python-dotenv carregado com sucesso")
except ImportError:
    print("⚠️  python-dotenv não encontrado - usando apenas variáveis de sistema")

# === AMAZON PA API ===
# Access Keys configuradas no settings.py
AMAZON_ACCESS_KEY = os.getenv("AMAZON_ACCESS_KEY", PRIMARY_ACCESS_KEY)
AMAZON_SECRET_KEY = os.getenv("AMAZON_SECRET_KEY", "")  # Esta precisa ser configurada no .env
AMAZON_ASSOCIATE_TAG = get_affiliate_tag("default")  # Tag padrão

# === TWITTER API ===
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY", "")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET", "")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN", "")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", "")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN", "")

# === TELEGRAM BOT ===
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")  # ID do seu grupo/canal

# === THREADS (META) ===
THREADS_ACCESS_TOKEN = os.getenv("THREADS_ACCESS_TOKEN", "")

# === BLUESKY ===
BLUESKY_USERNAME = os.getenv("BLUESKY_USERNAME", "")
BLUESKY_PASSWORD = os.getenv("BLUESKY_PASSWORD", "")

# === VERIFICAÇÃO ===
def check_api_keys():
    """Verifica se as chaves essenciais estão configuradas"""
    missing_keys = []
    configured_keys = []
    
    # Verifica Amazon PA API
    if AMAZON_ACCESS_KEY and AMAZON_ACCESS_KEY in AMAZON_ACCESS_KEYS:
        configured_keys.append("✅ Amazon Access Key")
    else:
        configured_keys.append("✅ Amazon Access Key (usando da configuração)")
    
    if not AMAZON_SECRET_KEY:
        missing_keys.append("AMAZON_SECRET_KEY")
    else:
        configured_keys.append("✅ Amazon Secret Key")
    
    # Verifica Twitter (principal rede)
    if not TWITTER_API_KEY:
        missing_keys.append("TWITTER_API_KEY")
    else:
        configured_keys.append("✅ Twitter API")
    
    # Verifica Telegram
    if not TELEGRAM_BOT_TOKEN:
        missing_keys.append("TELEGRAM_BOT_TOKEN")
    else:
        configured_keys.append("✅ Telegram Bot")
    
    # Mostra status
    print("\n🔐 STATUS DAS APIS:")
    for key in configured_keys:
        print(f"   {key}")
    
    if missing_keys:
        print("\n⚠️  CHAVES DE API FALTANDO:")
        for key in missing_keys:
            print(f"   - {key}")
        print("\n💡 Configure no arquivo .env:")
        for key in missing_keys:
            print(f"   {key}=sua_chave_aqui")
        return False
    
    print("\n✅ Todas as chaves de API essenciais estão configuradas!")
    return True

def get_amazon_credentials(platform="default"):
    """Retorna as credenciais da Amazon para uma plataforma específica"""
    return {
        "access_key": AMAZON_ACCESS_KEY,
        "secret_key": AMAZON_SECRET_KEY,
        "associate_tag": get_affiliate_tag(platform),
        "region": "Brazil"
    }

# Verificação automática ao importar
if __name__ == "__main__":
    check_api_keys() 