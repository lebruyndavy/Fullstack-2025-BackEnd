team_members_query = "SELECT id, name, role, bio FROM team_members;"
team_members_by_id_query = "SELECT id, name, role, bio FROM team_members WHERE id = %s;"
testimonials_query = "SELECT id, client_name, company_name, content FROM testimonials;"
testimonials_by_id_query = "SELECT id, client_name, company_name, content FROM testimonials WHERE id = %s;"
