# 🍽️ NutriAI – Food Ordering System

## 📌 Project Overview

**NutriAI** is a Django-based food ordering web application that allows users to browse restaurants, explore food items, add items to their cart, place orders, manage their wishlist, and track their orders.

The application provides a simple and user-friendly food ordering experience with features such as user authentication, restaurant and menu management, cart management, food recommendations, wishlist, order history, and order tracking.

---

## 🚀 Features

* 🔐 User Registration & Login
* 👤 User Authentication
* 🏪 Restaurant Listing
* 🍔 Food Menu
* 📂 Food Categories
* 🔍 Food Search
* 🛒 Shopping Cart
* ➕ Increase Food Quantity
* ➖ Decrease Food Quantity
* ❌ Remove Items from Cart
* ❤️ Wishlist
* 🤖 Food Recommendations
* 📦 Place Orders
* 💵 Cash on Delivery
* 📋 Order History
* 🚚 Order Tracking
* 🖼️ Restaurant & Food Images
* 👨‍💼 Django Admin Panel
* 📱 Responsive User Interface

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* Bootstrap

### Backend

* Python
* Django

### Database

* MySQL

### Tools

* Visual Studio Code
* Git
* GitHub
* MySQL

---

## 🏗️ Project Architecture

NutriAI follows the **Django MVT (Model-View-Template)** architecture.

```text
User
  ↓
HTML / CSS Templates
  ↓
Django Views
  ↓
Django Models
  ↓
MySQL Database
```

---

## 📂 Project Structure

```text
NutriAI/
│
├── accounts/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── restaurant/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── menu/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── cart/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── orders/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tasks.py
│   ├── urls.py
│   └── views.py
│
├── recommendation/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── wishlist/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── static/
│   ├── css/
│   ├── images/
│   └── foods/
│
├── media/
│
├── templates/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
└── README.md
```

> Replace `db.sqlite3` with your actual database setup if your project uses MySQL only.

---

## 🗄️ Database

NutriAI uses **MySQL** as the database.

The major entities in the application include:

```text
User
 │
 ├── Cart
 │     └── Food
 │
 ├── Wishlist
 │     └── Food
 │
 └── Orders
       └── Order Items
              └── Food

Restaurant
 │
 └── Food
       │
       └── Category
```

### Main Models

* User
* Restaurant
* Category
* Food
* Cart
* Cart Item
* Order
* Order Item
* Wishlist
* Recommendation

---

## 🍴 Restaurant & Food Management

The restaurant module allows food items to be associated with specific restaurants.

Each food item can contain information such as:

* Food name
* Restaurant
* Category
* Description
* Price
* Image

Example:

```text
Restaurant
    ↓
Category
    ↓
Food Item
    ↓
Price
    ↓
Description
    ↓
Image
```

---

## 🛒 Cart Management

Users can manage their selected food items through the shopping cart.

The cart provides the following operations:

```text
Add Food
   ↓
Increase Quantity
   ↓
Decrease Quantity
   ↓
Remove Food
   ↓
Calculate Total
```

Users can review their selected food items before placing an order.

---

## ❤️ Wishlist

The wishlist allows users to save food items that they may want to order later.

Users can:

* Add food to wishlist
* View wishlist
* Remove food from wishlist

---

## 🤖 Food Recommendation

NutriAI includes a recommendation module that helps users discover food items.

The recommendation feature can suggest food based on available food categories and items in the application.

---

## 📦 Order Management

After selecting food items, users can place an order.

The order process is:

```text
Add Food to Cart
       ↓
View Cart
       ↓
Checkout
       ↓
Place Order
       ↓
Cash on Delivery
       ↓
Order Confirmed
```

There is **no online payment gateway** implemented in the current version.

---

## 🚚 Order Tracking

NutriAI includes an order tracking feature.

After placing an order, its status progresses through different stages:

```text
Order Placed
      ↓
Confirmed
      ↓
Preparing
      ↓
Delivery
      ↓
Delivered
```

The project uses background/threading logic to automatically update the order status.

Example timeline:

```text
Order Placed → Confirmed
                  ↓
              Preparing
                  ↓
               Delivery
                  ↓
               Delivered
```

---

## 📋 Order History

Users can view their previously placed orders.

Order information can include:

* Order ID
* Ordered food items
* Quantity
* Total amount
* Order date
* Order status
* Payment method

The current payment method is **Cash on Delivery (COD)**.

---

## 🔐 Authentication

NutriAI provides user authentication functionality.

Users can:

* Register an account
* Login
* Logout
* Access authenticated features
* Manage their food orders

Authentication helps protect user-specific features such as:

* Cart
* Wishlist
* Orders
* Order history

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

Move into the project directory:

```bash
cd NutriAI
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

---

### 3. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

---

### 4. Install Required Packages

```bash
pip install -r requirements.txt
```

---

## 🗄️ MySQL Configuration

Create a MySQL database for the project.

Example:

```sql
CREATE DATABASE nutriai;
```

Then configure the database in `settings.py`.

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "nutriai",
        "USER": "root",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

Replace:

```text
your_password
```

with your MySQL password.

---

## 🔄 Run Migrations

Run:

```bash
python manage.py makemigrations
```

Then:

```bash
python manage.py migrate
```

---

## 👨‍💼 Create Superuser

To access the Django admin panel:

```bash
python manage.py createsuperuser
```

Enter:

```text
Username
Email
Password
```

---

## ▶️ Run the Project

Start the Django development server:

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

---

## 🖼️ Static & Media Files

The project uses Django static files for CSS, JavaScript, and application assets.

Example structure:

```text
static/
│
├── css/
│   └── style.css
│
├── images/
│   ├── logo.png
│   └── hero.jpg
│
└── foods/
    ├── biryani.jpg
    ├── pizza.jpg
    ├── burger.jpg
    └── ...
```

Media files are stored separately when required:

```text
media/
└── images/
```

---

## 🔄 Application Workflow

```text
                    NutriAI
                       │
          ┌────────────┴────────────┐
          ↓                         ↓
       Register                  Login
          │                         │
          └────────────┬────────────┘
                       ↓
              Browse Restaurants
                       ↓
                Browse Menu
                       ↓
              Select Food Items
                       ↓
                  Add to Cart
                       ↓
                 Manage Cart
                       ↓
                   Checkout
                       ↓
                 Place Order
                       ↓
              Cash on Delivery
                       ↓
               Order Confirmed
                       ↓
              Order Status Tracking
                       ↓
                  Delivered
```

---

## 🎯 Project Objectives

The main objectives of NutriAI are:

1. To develop a complete food ordering web application.
2. To implement restaurant and food menu management.
3. To provide users with an easy-to-use shopping cart.
4. To implement wishlist functionality.
5. To provide food recommendations.
6. To implement order placement and order history.
7. To provide order status tracking.
8. To integrate Django with MySQL.
9. To implement authentication and session-based functionality.
10. To gain practical experience in full-stack web development.

---

## 💡 Key Django Concepts Used

This project demonstrates practical use of:

* Django Models
* Django Views
* Django Templates
* URL Routing
* Django ORM
* MySQL Integration
* Authentication
* Sessions
* CRUD Operations
* Foreign Key Relationships
* Static Files
* Media Files
* Template Inheritance
* Django Admin
* Background Threading
* Migrations

---

## 🔮 Future Enhancements

The following features can be added in future versions:

* 💳 Online Payment Gateway
* ⭐ Food Reviews & Ratings
* 📍 Location-Based Restaurant Search
* 📧 Email Order Notifications
* 📱 Mobile Application
* 🤖 Advanced AI-Based Recommendations
* 🧑‍🍳 Restaurant Owner Dashboard
* 🚴 Delivery Partner Module
* 📊 Admin Analytics Dashboard
* 🔔 Real-Time Notifications
* 🌐 REST API

---

## 📸 Project Screenshots

Add screenshots of your application here.

Example:

```markdown
## 📸 Screenshots

### Home Page
![Home Page](screenshots/home.png)

### Restaurant Page
![Restaurant Page](screenshots/restaurants.png)

### Menu Page
![Menu Page](screenshots/menu.png)

### Cart Page
![Cart Page](screenshots/cart.png)

### Order Tracking
![Order Tracking](screenshots/order-tracking.png)
```

---

## 🧪 Testing

The application was tested for major user workflows including:

* User registration
* User login/logout
* Restaurant browsing
* Food browsing
* Food search
* Add to cart
* Increase/decrease quantity
* Remove cart items
* Wishlist functionality
* Order placement
* Order history
* Order tracking
* Django admin functionality

---

## 🌐 Deployment

The project can be deployed using platforms such as:

* Render
* Railway
* PythonAnywhere

For production deployment, configure:

* `ALLOWED_HOSTS`
* Static files
* Media files
* Production database
* Environment variables
* `DEBUG = False`

---

## 👩‍💻 Author

**Aaradhana Prajapati**

### Skills Demonstrated

```text
Python
Django
MySQL
HTML5
CSS3
Bootstrap
Git
GitHub
```

---

## 📄 License

This project was developed for educational and project demonstration purposes.

---

## ⭐ Acknowledgement

This project helped in gaining practical experience in developing a database-driven web application using **Python, Django, MySQL, HTML, CSS, and Bootstrap**.
