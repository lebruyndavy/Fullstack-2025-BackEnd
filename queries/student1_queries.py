portfolio_items = "SELECT * FROM portfolio_items ORDER BY id;"
portfolio_items_per_category = "SELECT id, title, image_url, category_id FROM portfolio_items WHERE category_id = %s;"
portfolio_item_category = "SELECT pc.id, pc.name FROM portfolio_items pi JOIN portfolio_categories pc ON pi.id = pc.id WHERE pi.id = %s;"
portfolio_categories = "SELECT id, name FROM portfolio_categories ORDER BY id;"
