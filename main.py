#!/usr/bin/env python3
"""
Amazon Affiliate Bot - Arquivo Principal
Versão: 1.0.0 (Desenvolvimento)
"""

import os
import sys
from datetime import datetime

# Adiciona o diretório atual ao path para importar módulos locais
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importações locais
from config import settings
from config.api_keys import check_api_keys

def create_directory_structure():
    """Cria a estrutura de pastas necessárias se não existirem"""
    directories = [
        "data",
        "data/products", 
        "data/sales",
        "data/analytics",
        "data/backup",
        "logs",
        "src",
        "src/scrapers",
        "src/content", 
        "src/social",
        "src/affiliate",
        "src/scheduler",
        "templates",
        "tests"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"📁 Pasta criada/verificada: {directory}")

def show_welcome_message():
    """Exibe mensagem de boas-vindas com status do projeto"""
    print("=" * 60)
    print("🤖 AMAZON AFFILIATE BOT")
    print("=" * 60)
    print(f"📅 Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"🔧 Versão: {settings.VERSION}")
    print(f"🎯 Tags configuradas: {len(settings.AFFILIATE_TAGS)} canais")
    print(f"🔑 Access Keys: {len(settings.AMAZON_ACCESS_KEYS)} ativas")
    print("=" * 60)

def show_affiliate_tags():
    """Mostra as tags de afiliado configuradas"""
    print("\n🏷️  TAGS DE AFILIADO CONFIGURADAS:")
    for platform, tag in settings.AFFILIATE_TAGS.items():
        audience = settings.AUDIENCE_METRICS.get(platform, "N/A")
        if audience != "N/A":
            print(f"   📱 {platform.ljust(15)} → {tag} ({audience:,} seguidores)")
        else:
            print(f"   📱 {platform.ljust(15)} → {tag}")

def show_project_status():
    """Mostra o status atual do desenvolvimento"""
    print("\n📊 STATUS DO PROJETO:")
    print("✅ Fase 1: Estrutura básica (CONCLUÍDA)")
    print("🔄 Fase 2: Monitor de produtos (INICIANDO)")
    print("⏳ Fase 3: Gerador de conteúdo")
    print("⏳ Fase 4: Redes sociais")
    print("⏳ Fase 5: Analytics")

def show_next_steps():
    """Mostra os próximos passos"""
    print("\n" + "=" * 60)
    print("🚀 PRÓXIMOS PASSOS:")
    print("1. ✅ Tags de afiliado configuradas!")
    print("2. Configure sua Amazon Secret Key no arquivo .env")
    print("3. Configure APIs das redes sociais (opcional para começar)")
    print("4. Aguarde: Vamos criar o monitor de produtos da Amazon!")
    print("\n💡 PARA OBTER SUA SECRET KEY:")
    print("   • Acesse: Amazon Associates → PA API")
    print("   • Gere/copie sua Secret Key")
    print("   • Adicione no arquivo .env")
    print("=" * 60)

def main():
    """Função principal do programa"""
    try:
        # Limpa a tela
        os.system('clear' if os.name == 'posix' else 'cls')
        
        # Mensagem de boas-vindas
        show_welcome_message()
        
        # Cria estrutura de pastas
        print("\n🏗️  CRIANDO ESTRUTURA DO PROJETO...")
        create_directory_structure()
        
        # Mostra tags configuradas
        show_affiliate_tags()
        
        # Verifica APIs
        print("\n🔐 VERIFICANDO APIS...")
        check_api_keys()
        
        # Status do projeto
        show_project_status()
        
        # Próximos passos
        show_next_steps()
        
        return True
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

if __name__ == "__main__":
    success = main()
    if success:
        print("\n✅ Setup inicial concluído com sucesso!")
    else:
        print("\n❌ Houve um problema no setup inicial.")
        sys.exit(1) 