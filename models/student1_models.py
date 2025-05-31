from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class PortfolioCategory(Base):
    __tablename__ = "portfolio_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class PortfolioItem(Base):
    __tablename__ = "portfolio_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    image_url = Column(String)
    category_id = Column(Integer, ForeignKey("portfolio_categories.id"))
