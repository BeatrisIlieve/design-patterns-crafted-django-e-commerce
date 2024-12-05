# Online Shop Database with Design Patterns

## 📖 Project Overview

This project is a relational database designed to power an online shop. It includes models for managing users, products, inventory, orders, and shopping functionality, while incorporating Facade and Strategy design patterns to handle complex operations such as processing orders and payments.

## 🌟 Key Features
User Management: Handles user credentials, shipping details, and payment information.
Product Catalog: Includes models for products, inventory, and wishlists.
Order Processing: Streamlines the creation of orders, order items, and deliveries.
Shopping Workflow: Supports shopping bag management and order confirmation.
Design Patterns:
Facade Pattern: Simplifies multi-step processes (e.g., saving shipping details, creating orders, and processing payments).
Strategy Pattern: Calculates total costs and delivery due dates based on user-selected shipping methods.

## 🏗️ Models
### User Models
- User Credentials: Stores user authentication data (e.g., email, password).
- User Shipping Details: Records user-provided shipping addresses.
- User Payment Details: Saves payment information such as card details.
### Product Models
- Category
- Color
- Product: Manages product information like description, price, and images.
- Inventory: Tracks product availability in stock per product size.
### Order Models
- Order: Links a user to their purchase and records order details.
- Order Items: Contains information about specific items in an order, including quantity and inventory data.
- Delivery: Manages delivery information, including method, total cost, and due date.
### Other Models
- Wishlist: Allows users to save products they intend to purchase later.
- Shopping Bag: Tracks products added to the user's shopping cart before purchase.
## 🛠️ Design Patterns
### Facade Pattern
The Facade Pattern is used to encapsulate and simplify multi-step workflows, making them easier to use and maintain.

#### Shipping Details Workflow
Triggered after a user submits their shipping details:

1. Save Shipping Details: Stores the user's shipping information.
2. Create Order: Creates an order with the user's details.
3. Create Delivery: Initializes a delivery linked to the order, calculating total cost and selecting the delivery method.
4. Payment Processing Workflow

Triggered after a user submits their payment:

1. Save Payment Details: Records the user's payment information.
2. Create Order Items: Links items from the shopping bag to the order.
3. Delete Shopping Bag: Clears the user's shopping bag after order completion.
4. Provide Confirmation: Sends an order confirmation to the user:

The Provide Confirmation step generates a detailed summary of the order, aggregating data from multiple related models to present the user with a comprehensive view of their purchase.

##### Query Description

###### Filters by User:
- Retrieves orders specific to the user based on their primary key (user_pk).
  
###### Joins Related Models:
- Delivery: Fetches delivery details such as the method, total cost, and due date using select_related.
- Order Items: Prefetches related OrderItem records linked to the Order using prefetch_related.
- Inventory: From OrderItem, joins the Inventory table to get product details like size and price.
- Product: From Inventory, fetches product-specific details like the first image URL.
  
###### Calculates and Annotates Data:
- Order Date: Extracts a readable created_date from the created_at field using TruncDate.
- Total Price per Product: Computes the price for each item in the order by multiplying the price of an item (inventory__price) with the quantity purchased.
- Delivery Method Title: Maps the delivery method code (SP, EH, RH) to a user-friendly string using a Case expression.

###### Organizes Output:
Selects and returns only the relevant fields to provide a concise and meaningful response:
- Order Details: created_date
- Order Items: Quantity, price, total price, size, and product image.
- Delivery Information: Delivery method, cost, and due date.
  
Orders the Data:
- Sorts the order items within the order by their primary key for consistent display.
