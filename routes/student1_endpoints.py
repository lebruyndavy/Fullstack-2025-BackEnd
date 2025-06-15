from typing import Optional
from fastapi import APIRouter, HTTPException, Query
import database
from models.student1_models import NewsletterSubscription
from queries import student1_queries as queries

app = APIRouter()

@app.get("/v1/portfolio/items")
def get_portfolio_items(category_id: Optional[int] = Query(default=None)):
    if category_id is not None:
        try:
            result = database.execute_sql_query(queries.portfolio_items_per_category, (category_id,))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Database query failed: {str(e)}")

        if not result:
            raise HTTPException(status_code=404, detail="No portfolio items found for this category")
    else:
        try:
            result = database.execute_sql_query(queries.portfolio_items)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Database query failed: {str(e)}")

    portfolio_items = [
        {
            "id": row[0],
            "name": row[1],
            "category_id": row[2],
            "image_url": row[3]
        }
        for row in result
    ]
    return {"portfolio_items": portfolio_items}

@app.get("/v1/portfolio/categories")
def get_all_portfolio_categories():
    try:
        result = database.execute_sql_query(queries.portfolio_categories)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database query failed: {str(e)}")

    portfolio_categories = [
        {
            "id": row[0],
            "name": row[1]
        }
        for row in result
    ]
    return {"portfolio_categories": portfolio_categories}

@app.get("/v1/portfolio/item/{item_id}/category")
def get_portfolio_item_category(item_id: int):
    try:
        result = database.execute_sql_query(queries.portfolio_item_category, (item_id,))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database query failed: {str(e)}")

    if not result:
        raise HTTPException(status_code=404, detail="Portfolio item not found")

    return {"id": result[0][0], "name": result[0][1]}

@app.post("/v1/newsletter/subscribe")
def subscribe_to_newsletter(subscription: NewsletterSubscription):
    query = queries.insert_newsletter_subscription
    try:
        database.execute_sql_query(query, (subscription.name, subscription.email))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Subscription failed: {e}")
    return {"message": "Successfully subscribed to the newsletter"}