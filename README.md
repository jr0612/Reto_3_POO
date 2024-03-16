# Reto_3_POO
**Diagrama de clases de restaurante**
```mermaid
classDiagram
    class MenuItem {
        -String name
        -float price
        +calculate_total_price(quantity)
    }
    class Beverage {
        -String size
        +__init__(name, price, size)
    }
    class Appetizer {
        -int servings
        +__init__(name, price, servings)
    }
    class MainCourse {
        -List<String> ingredients
        +__init__(name, price, ingredients)
    }
    class Order {
        -List<tuple<MenuItem, int>> items
        +__init__()
        +add_item(item, quantity=1)
        +calculate_total_bill()
    }
    MenuItem <|-- Beverage
    MenuItem <|-- Appetizer
    MenuItem <|-- MainCourse
    Order "1" *-- "*" MenuItem : contains

```
