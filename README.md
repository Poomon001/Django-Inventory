# Django-Inventory
A Django inventory application that provides a functional product catalog with 10 preloaded categories, 15 tags, and 23 sample products that can be managed via the admin interface. Users can search products by description and filter by category or tags via a HTML interface.

# Design and Decision
This project follows Django's Model-View-Template pattern:
* Models define the data schema, including Product, Category, and Tag.
* Views handle busniness logic and request processing.
* Template render HTML for the user interface and dynamic data display.

## Assumptions
* The dataset is small, so no advanced database infrastructure is considered.
* Each product must belong to exactly one category.
* A product may have zero or multiple tags.
* Categories and tags cannot be deleted if they are referenced by products
* Category and tag names cannot be duplicated, but product names are not required to be unique.
* Products are not required to have a description.
* URL paths are not strict and can be designed freely.
* Basic unit and integration tests are provided in test.py, but they are not strictly required.

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
** Note: Credentials are for demo purposes only


# Sample
![Sample](https://github.com/Poomon001/Django-Inventory/blob/main/static/assets/readme/Sample.png)
