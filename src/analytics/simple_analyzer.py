#!/usr/bin/env python3
"""
Analisador Simples de Vendas Excel
Analisa relatórios de vendas da Amazon sem dependências pesadas
"""

import sys
import os
from datetime import datetime

# Adiciona o diretório atual ao path para importar config
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def find_excel_files():
    """Encontra arquivos Excel na pasta atual"""
    excel_files = []
    for file in os.listdir('.'):
        if file.endswith(('.xlsx', '.xls', '.csv')):
            excel_files.append(file)
    return excel_files

def analyze_excel_basic_info(file_path):
    """
    Análise básica de arquivo Excel usando apenas bibliotecas padrão
    """
    print(f"📊 ANALISANDO ARQUIVO: {file_path}")
    print("=" * 60)
    
    # Informações básicas do arquivo
    try:
        file_size = os.path.getsize(file_path)
        file_modified = datetime.fromtimestamp(os.path.getmtime(file_path))
        
        print(f"📁 Tamanho: {file_size:,} bytes ({file_size/1024:.1f} KB)")
        print(f"📅 Modificado: {file_modified.strftime('%d/%m/%Y %H:%M:%S')}")
        
        # Tenta detectar o tipo de arquivo pelo nome
        file_lower = file_path.lower()
        if 'vendas' in file_lower or 'sales' in file_lower:
            print("✅ Detectado: Relatório de Vendas")
        elif 'fee' in file_lower or 'comiss' in file_lower:
            print("✅ Detectado: Relatório de Comissões")
        elif 'trend' in file_lower:
            print("✅ Detectado: Relatório de Tendências")
        else:
            print("❔ Tipo: Não identificado automaticamente")
            
        return True
        
    except Exception as e:
        print(f"❌ Erro ao analisar arquivo: {e}")
        return False

def suggest_products_by_filename(file_path):
    """
    Sugere produtos baseado no nome do arquivo e data
    """
    print(f"\n🎯 SUGESTÕES BASEADAS NO ARQUIVO:")
    print("=" * 50)
    
    file_lower = file_path.lower()
    suggestions = []
    
    # Análise baseada no nome do arquivo
    if 'daily' in file_lower or 'diario' in file_lower:
        suggestions.append("📈 Focar em produtos de alta rotatividade")
        suggestions.append("⚡ Priorizar ofertas relâmpago")
        
    if 'trends' in file_lower or 'tendencia' in file_lower:
        suggestions.append("🔥 Produtos em alta demanda identificados")
        suggestions.append("📊 Monitorar produtos similares aos trending")
        
    if 'fee' in file_lower:
        suggestions.append("💰 Análise de comissões por categoria")
        suggestions.append("🎯 Focar em produtos de maior margem")
    
    # Sugestões por época do ano
    current_month = datetime.now().month
    if current_month in [11, 12]:  # Nov/Dez
        suggestions.append("🎄 Black Friday e Natal: Electronics, Toys")
    elif current_month in [1, 2]:  # Jan/Fev
        suggestions.append("🏃 Ano novo: Health, Sports, Books")
    elif current_month in [3, 4, 5]:  # Mar/Abr/Mai
        suggestions.append("🏠 Outono: Home & Kitchen, Tools")
    
    # Exibe sugestões
    if suggestions:
        for suggestion in suggestions:
            print(f"   {suggestion}")
    else:
        print("   💡 Análise automática limitada - recomendado análise manual")

def generate_monitoring_config(file_path):
    """
    Gera configurações de monitoramento baseadas no arquivo
    """
    print(f"\n⚙️ CONFIGURAÇÕES RECOMENDADAS PARA O BOT:")
    print("=" * 50)
    
    print("📂 CATEGORIAS PRIORITÁRIAS (baseado em tendências gerais):")
    priority_categories = [
        "Electronics (iPhones, gadgets)",
        "Home & Kitchen (Air Fryer, utensílios)",
        "Health & Personal Care (suplementos)",
        "Sports & Outdoors (equipamentos fitness)",
        "Books (desenvolvimento pessoal)"
    ]
    
    for cat in priority_categories:
        print(f"   • {cat}")
    
    print(f"\n🏷️ USAR ESTAS TAGS PARA TRACKING:")
    print(f"   • Twitter: twitterluiz-20 (50k seguidores - prioridade)")
    print(f"   • Telegram: grupotelegram0d-20")
    print(f"   • Threads: threads05e-20")
    print(f"   • Instagram Stories: storiesigluiz-20")
    
    print(f"\n📊 CONFIGURAÇÕES DO FILTRO:")
    print(f"   • Desconto mínimo: 15% (atual)")
    print(f"   • Rating mínimo: 4.0 (atual)")
    print(f"   • Reviews mínimas: 100 (atual)")
    print(f"   • Focar em produtos Prime: ✅")

def recommend_next_steps():
    """
    Recomenda próximos passos baseados na análise
    """
    print(f"\n🚀 PRÓXIMOS PASSOS RECOMENDADOS:")
    print("=" * 50)
    
    steps = [
        "1. Configure sua Amazon Secret Key no .env",
        "2. Teste o monitor: python src/scrapers/amazon_monitor.py",
        "3. Implemente Fase 3: Gerador de conteúdo",
        "4. Configure Twitter API para posts automáticos",
        "5. Analise performance após 1 semana de uso"
    ]
    
    for step in steps:
        print(f"   {step}")
    
    print(f"\n💡 DICA PRO:")
    print(f"   • Comece postando manualmente no Twitter usando as tags")
    print(f"   • Acompanhe quais tipos de produto geram mais cliques")
    print(f"   • Use essas informações para otimizar o bot")

def main():
    """Função principal"""
    print("🔍 ANÁLISE SIMPLES DE VENDAS AMAZON")
    print("=" * 60)
    print(f"📅 Data da análise: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    
    # Busca arquivos Excel
    excel_files = find_excel_files()
    
    if not excel_files:
        print("\n❌ Nenhum arquivo Excel (.xlsx, .xls, .csv) encontrado na pasta")
        print("\n💡 PARA USAR ESTE ANALISADOR:")
        print("   1. Coloque seu relatório de vendas da Amazon na pasta")
        print("   2. Execute novamente: python analyze_sales_simple.py")
        print("   3. O arquivo será analisado automaticamente")
        return
    
    print(f"\n📊 ARQUIVOS ENCONTRADOS: {len(excel_files)}")
    for i, file in enumerate(excel_files, 1):
        print(f"   {i}. {file}")
    
    # Analisa o primeiro arquivo
    main_file = excel_files[0]
    print(f"\n🎯 ANALISANDO: {main_file}")
    
    # Análise básica
    if analyze_excel_basic_info(main_file):
        # Sugestões baseadas no arquivo
        suggest_products_by_filename(main_file)
        
        # Configurações recomendadas
        generate_monitoring_config(main_file)
        
        # Próximos passos
        recommend_next_steps()
        
        print(f"\n✅ ANÁLISE CONCLUÍDA!")
        print(f"💾 Para análise detalhada, instale: pip install pandas openpyxl")
        print(f"🔄 Depois execute: python src/analytics/sales_analyzer.py")
    
    print(f"\n" + "=" * 60)

if __name__ == "__main__":
    main() 