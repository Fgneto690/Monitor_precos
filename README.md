# 🛒 Monitor de Preços Python

Projeto desenvolvido para buscar e comparar preços de hardware (RTX 4060) utilizando a API do Google Shopping via SerpApi.

## 🚀 Funcionalidades
- Busca automatizada de preços em tempo real.
- Filtro de similaridade de nomes (Fuzzy Matching) para evitar acessórios irrelevantes.
- Filtro de faixa de preço para garantir resultados precisos.
- Exportação dos dados para um arquivo CSV organizado.
- Geração de links estáveis via Product ID do Google.

## 🛠️ Tecnologias
- **Python 3**
- **SerpApi**: Integração com motores de busca.
- **TheFuzz**: Lógica de comparação de strings.
- **CSV**: Persistência de dados.

## 📉 Desafios Superados
Durante o desenvolvimento, o maior desafio foi lidar com a expiração dos links de redirecionamento do Google Shopping. A solução aplicada foi a captura e construção de URLs baseadas em IDs de catálogo estáticos, garantindo que o usuário consiga acessar a oferta.

---
*Projeto de estudo para portfólio.*
