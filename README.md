# Projeto  - Análise de Dados do ENEM

Este projeto é uma aplicação web desenvolvida em Flask que permite analisar dados do ENEM e informações sobre acesso à internet nas escolas brasileiras. A aplicação oferece uma interface para visualização e análise de dados educacionais, incluindo notas do ENEM por município e informações sobre infraestrutura escolar.

## Funcionalidades

- Visualização de dados do ENEM por município
- Análise de notas em diferentes áreas do conhecimento
- Informações sobre infraestrutura escolar
- Dados demográficos dos estudantes
- Exportação de dados em formato CSV
- Importação de novos dados

## Tecnologias Utilizadas

- Python 3.x
- Flask
- PostgreSQL
- Bootstrap
- Gunicorn (para produção)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Alef25-dev/Projeto-Matheus.git
cd Projeto-Matheus
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure o banco de dados PostgreSQL e atualize as credenciais em `db.py`

4. Execute a aplicação:
```bash
python app.py
```

## Rotas da API

### Rotas Principais

- `/` - Página inicial com listagem de dados
- `/exportar` - Exporta os dados em formato CSV
- `/importar` - Interface para importação de novos dados

### Rotas do ENEM

#### Notas por Área
- `/enem/humanas/<co_municipio>` - Média de notas em Ciências Humanas
- `/enem/natureza/<co_municipio>` - Média de notas em Ciências da Natureza
- `/enem/linguagens/<co_municipio>` - Média de notas em Linguagens
- `/enem/matematica/<co_municipio>` - Média de notas em Matemática

#### Dados das Escolas
- `/enem/fed_priv/<co_municipio>` - Total de escolas federais/particulares
- `/enem/est_mun/<co_municipio>` - Total de escolas estaduais/municipais

#### Acesso à Tecnologia
- `/enem/s_pc/<co_municipio>` - Alunos com acesso a computador
- `/enem/n_pc/<co_municipio>` - Alunos sem acesso a computador
- `/enem/s_cel/<co_municipio>` - Alunos com acesso a celular
- `/enem/n_cel/<co_municipio>` - Alunos sem acesso a celular
- `/enem/s_int/<co_municipio>` - Alunos com acesso à internet
- `/enem/n_int/<co_municipio>` - Alunos sem acesso à internet

#### Dados Demográficos
- `/enem/cor_bra_ama/<co_municipio>` - Total de alunos brancos/amarelos
- `/enem/cor_outros/<co_municipio>` - Total de alunos de outras raças
- `/enem/masculino/<co_municipio>` - Total de alunos do sexo masculino
- `/enem/feminino/<co_municipio>` - Total de alunos do sexo feminino

### Rotas de Internet

- `/internet/<co_municipio>` - Informações sobre acesso à internet nas escolas do município

## Formato dos Dados

Todas as rotas do ENEM retornam dados no seguinte formato:
```json
{
    "co_municipio": 3550308,
    "uf": "SP",
    "municipio": "São Paulo",
    "metric_name": "Nome da métrica",
    "metric_value": "Valor da métrica"
}
```

A rota de internet retorna:
```json
{
    "co_municipio": 3550308,
    "no_regiao": "Sudeste",
    "no_uf": "São Paulo",
    "no_municipio": "São Paulo",
    "total_in_acesso_internet_computador": 1000
}
```

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
