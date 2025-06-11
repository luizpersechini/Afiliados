# 🤖 Amazon Affiliate Automation Bot

Sistema automatizado para gerenciar links de afiliado da Amazon e postar nas redes sociais.

## 📊 Status do Projeto
- ✅ **Fase 1**: Estrutura básica (CONCLUÍDA)
- ✅ **Fase 2**: Monitor de produtos (FUNCIONANDO) 
- ⏳ **Fase 3**: Gerador de conteúdo
- ⏳ **Fase 4**: Integração com redes sociais
- ⏳ **Fase 5**: Analytics e otimização

## 🎯 Objetivo
Automatizar o processo de:
1. Encontrar produtos em promoção na Amazon
2. Gerar links de afiliado
3. Criar posts orgânicos e engajantes
4. Publicar nas redes sociais (Twitter, Telegram, Threads, Bluesky)
5. Acompanhar performance e vendas

## 🚀 Quick Start
```bash
# 1. Clone o repositório
git clone <seu-repositorio>
cd amazon-affiliate-bot

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Configurar chaves de API
cp env_example.txt .env
# Edite o .env com suas chaves reais

# 4. Executar
python main.py
```

## 🏷️ Tags de Afiliado Configuradas
- **Twitter**: twitterluiz-20 (50k seguidores)
- **Telegram**: grupotelegram0d-20
- **Threads**: threads05e-20 (10k seguidores)
- **Bluesky**: bsky01-20 (10k seguidores)
- **Instagram Stories**: storiesigluiz-20 (20k seguidores)
- **Email**: emailsherwa-20
- **Default**: sherwa-20

## 📱 Redes Sociais Suportadas
- **Twitter**: ✅ Configurado
- **Telegram**: ✅ Configurado  
- **Threads**: ✅ Configurado
- **Bluesky**: ✅ Configurado
- **Instagram**: 🔄 Futuro

## 🔧 Testando o Sistema
```bash
# Testar monitor de produtos
python src/scrapers/amazon_monitor.py

# Testar análise de vendas (coloque seu Excel na pasta)
python src/analytics/sales_analyzer.py

# Status geral do projeto
python main.py
```

## 📈 Métricas
- **Audiência Total**: 96.000+ pessoas
- **Foco**: Produtos com desconto ≥15% e rating ≥4.0
- **Meta**: Automatização 80% do processo manual

## 🔐 Segurança
- ✅ Chaves de API protegidas (.env não commitado)
- ✅ Dados de vendas ignorados pelo Git
- ✅ Logs locais não sincronizados
- ✅ Access Keys da Amazon configuradas

## 🏗️ Estrutura do Projeto
```
amazon-affiliate-bot/
├── 📁 config/          # Configurações e APIs
├── 📁 src/
│   ├── 📁 scrapers/    # Monitor de produtos Amazon
│   ├── 📁 analytics/   # Análise de vendas
│   ├── 📁 content/     # Gerador de posts
│   ├── 📁 social/      # Bots das redes sociais
│   └── 📁 scheduler/   # Agendamento
├── 📁 data/            # Dados (ignorado pelo Git)
├── 📁 logs/            # Logs (ignorado pelo Git)
└── 📁 templates/       # Templates de posts
```

## 💡 Próximos Passos
1. **Configurar Amazon Secret Key** no arquivo .env
2. **Testar análise de vendas** com seus dados
3. **Configurar APIs das redes sociais**
4. **Implementar gerador de conteúdo** (Fase 3)

---
**Desenvolvido para afiliados Amazon Brasil** 🇧🇷

> ⚠️ **Importante**: Mantenha suas chaves de API seguras e nunca as compartilhe!