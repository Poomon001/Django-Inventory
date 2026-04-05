# Django-Inventory
A Django inventory application that provides a functional product catalog with 10 preloaded categories, 15 tags, and 23 sample products that can be managed via the admin interface. Users can search products by description and filter by category or tags via a HTML interface.

## Tools

# Design and Decision
## Workflow
![Workflow](https://github.com/Poomon001/Django-Inventory/blob/main/static/assets/readme/Workflow.png)

## Database Relations
![DB Relations](https://raw.githubusercontent.com/Poomon001/Django-Inventory/main/static/assets/readme/DB%20Relations.png)

## Table Details
### Category

| Name | Type      | Details       | Properties                          | Required |
|------|----------|--------------|-------------------------------------|----------|
| id   | AutoField| Primary key  | Auto-generated                      | Yes      |
| name | CharField| Category name| max_length=50, unique=True, indexed | Yes      |

### Tag

| Name | Type      | Details    | Properties                          | Required |
|------|----------|-----------|-------------------------------------|----------|
| id   | AutoField| Primary key| Auto-generated                      | Yes      |
| name | CharField| Tag name   | max_length=50, unique=True, indexed | Yes      |

### Product

| Name        | Type             | Details                    | Properties                                      | Required |
|------------|------------------|----------------------------|-------------------------------------------------|----------|
| id         | AutoField        | Primary key                | Auto-generated                                  | Yes      |
| name       | CharField        | Product name               | max_length=100                                  | Yes      |
| description| TextField        | Product description        | default="", blank=True                          | No       |
| category   | ForeignKey       | Reference to Category      | on_delete=PROTECT                               | Yes      |
| tags       | ManyToManyField  | Multiple Tag relationships | blank=True                                      | No       |
| created_at | DateTimeField    | Creation timestamp         | auto_now_add=True, editable=False               | Yes      |
| updated_at | DateTimeField    | Last update timestamp      | auto_now=True, editable=False                   | Yes      |


# Setup
## Instructions
```bash
git clone https://github.com/Poomon001/Django-Inventory.git
cd Django-Inventory
docker compose up --build
```
| Link | Description |
|------|------------|
| http://localhost:8000/admin | Admin page (ID: admin, PW: admin123) |
| http://localhost:8000/inventory/products/ | Inventory page |
