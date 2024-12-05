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
