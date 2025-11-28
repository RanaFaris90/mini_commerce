{
    'name': 'Mini Commerce',
    'summary': "Mini Commerce System – Products, Variants, Orders, Website Shop & Cart",
    'description': """
    Full Mini E-Commerce Prototype

    This module provides a complete end-to-end mini-commerce system inside Odoo, built as a full technical assignment.

    Included Features:
    ----------------------------------------------------
    🔹 Product Management
        - Custom Product model: mini.product
        - Product fields: name, description, product_type, base_price, image
        - Variant model: mini.product.variant (color, size, extra_price, stock, quantity_on_hand)
        - Automatic stock computation based on confirmed orders

    🔹 Website Shop
        - /mini/shop       → Product Grid
        - Filter by Product Type (Dress, Pants, Skirt, Shoes, Coat)
        - Product Page with color/size variants, image switching, dynamic price

    🔹 Cart & Checkout
        - Add-to-cart using AJAX (JS Fetch API)
        - Stock validation before adding to cart
        - Session-based shopping cart stored in request.session
        - Cart summary page with totals
        - Checkout form (Name, Email, Phone)
        - Creates Orders + Order Lines

    🔹 Orders
        - Order Model (mini.order)
        - Order Line Model (mini.order.line)
        - Fields: subtotal, tax, total (computed)
        - Order confirmation page with success message
        - Back-end tree + form views for both orders & order lines

    🔹 Demo Data
        - Demo products with real images
        - Demo variants (color/size/extra price + images)

    🔹 Report
        - Custom Order Report (PDF) showing:
            * Customer info
            * Order lines
            * Subtotals, totals, variant details

    🔹 UI Enhancements
        - Custom backend background image
        - Beautiful front-end design (gradient titles, styled tables, SweetAlert popups)

    Perfect for demonstrating Odoo ORM, controllers, QWeb, sessions, website development, and full flow integration.
        """,
    'version': '1.2',
    'author': 'Rana',
    'category': 'Website',
    'depends': [
        'base',
        'website',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/demo_products.xml',
        'reports/reports.xml',
        'views/mini_product_views.xml',
        'views/mini_order_views.xml',
        'views/website_templates.xml',
    ],

    'installable': True,
    'application': True,
}
