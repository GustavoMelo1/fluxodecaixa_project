# Personal Finance

Automated personal cash flow system. The goal is to connect a material/personal goal with your current cash flow — finding the best prices, across the best stores, to bring more comfort and organization to your budget.

## Project structure

```text
personal-finance/
├── .gitignore
├── README.md
├── requirements.txt
│
└── src/
    ├── __init__.py
    ├── config.py                  
    │
    ├── api/
    │   ├── __init__.py
    │   ├── main.py                
    │   └── routers/
    │       ├── __init__.py
    │       ├── expenses.py
    │       ├── investments.py
    │       └── wishes.py
    │
    ├── database/
    │   ├── crud.py
    │   └── table.py
    │
    ├── ingestion/
    │   ├── __init__.py
    │   ├── searcher.py
    │   └── readers/
    │       ├── __init__.py
    │       ├── base.py
    │       ├── CSVReader.py
    │       ├── OFXReader.py
    │       └── PDFReader.py
    │
    └── transform/
```

> `data/`, `.env` e outros arquivos sensíveis/gerados estão no `.gitignore` e não aparecem na árvore acima.
