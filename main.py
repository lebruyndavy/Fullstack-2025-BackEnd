from fastapi import FastAPI
import database
from queries import student1_queries as queries
import config

app = FastAPI(docs_url=config.documentation_url)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/portfolio_items")
def get_all_portfolio_items():
    query = queries.portfolio_names_query
    portfolio_items = database.execute_sql_query(query)
    if isinstance(portfolio_items, Exception):
        return portfolio_items, 500
    portfolio_items_to_return = []
    for portfolio_item in portfolio_items:
        portfolio_items_to_return.append(portfolio_item[0])
    return {'portfolio_items': portfolio_items_to_return}
