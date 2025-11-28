# 🛍️ Odoo Mini E-Commerce Module

A complete mini-commerce system built in **Odoo 18**.  
This module includes custom product models, product variants, a shopping cart using sessions, a checkout flow, and a custom PDF order report.

---

## 🚀 Features

### 🔹 1. Product & Variant Management
- Custom product model `mini.product`
- Custom variant model `mini.product.variant`
- Variant attributes:
  - Color
  - Size
  - Extra Price
  - Initial Stock
  - Variant Image  
- Auto-calculated available quantity (`quantity_on_hand`)  
- Product categories: **Dress, Pants, Skirt, Shoes, Coat**

---

### 🔹 2. Website Shop
- Beautiful `/mini/shop` storefront
- Product grid with images, price, and gradient title
- Product filtering by type
- Stylish UI with gradients + aligned product cards
- Each product has its own page:
  - Variant selection dropdown
  - Auto-change product image when selecting variant
  - Price updates based on variant

---

### 🔹 3. Shopping Cart (Session-Based)
- Cart stored in `request.session['mini_cart']`
- Live stock checking before adding
- Calculates subtotal and total automatically

---

### 🔹 4. Checkout & Order Creation
- Checkout page collects customer info
- Order models:
  - `mini.order`
  - `mini.order.line`
- Creates an order and linked order lines automatically
- Confirmation page shows:
  - Custom image
  - Total amount
  - Delivery message

---

### 🔹 5. Custom PDF Report
- PDF report for orders
- Shows:
  - Customer information
  - Ordered products
  - Variants
  - Total amount

---

### 🔹 6. Demo Data Included
The module includes demo:
- Dresses  
- Skirts  
- Shoes  
- Colors  
- Sizes  
- Images for all products and variants  
- Prices, stock, and variant configurations  

This makes testing the module easy and fast.

---

### 🔹 7. Backend UI Enhancements
- Custom background image for Odoo backend
- Using inherited `web.layout`
- Full-page background styling using AVIF image

---


## ⚙️ Installation

### ✔️ Requirements
- Odoo 18 (Community)
- Python 3.10+
- PostgreSQL 14+

### ✔️ Installation Steps
1. Copy module into your addons folder:

```bash
cp -R mini_commerce /odoo/custom/addons/
```

2. Update apps list (enable Developer Mode)  
3. Search for **Mini Commerce**  
4. Click **Install**

---

## 🛒 Workflow Summary

### **1️⃣ Shop**
User visits `/mini/shop` and browses all products.

### **2️⃣ Product Page**
User opens a product → selects color, size, quantity  
Image changes based on selected variant.

### **3️⃣ Add to Cart**
- JS checks stock via `/mini/check_stock_js`
- If available → adds item using `/mini/add_to_cart_js`
- Cart saved in Odoo session

### **4️⃣ Cart Page**
Shows:
- Items
- Variant
- Quantity
- Subtotal
- Total price

### **5️⃣ Checkout**
User enters name, email, phone.

### **6️⃣ Order Created**
Order + order lines saved to database.

### **7️⃣ Confirmation Page**
Shows success message + total.

### **8️⃣ Export PDF (From Backend)**
Custom printable order report.

---

## 👩‍💻 Author

**Rana Faris**  
Odoo Developer – Python | QWeb | JS | OWL  
Jordan 🇯🇴
