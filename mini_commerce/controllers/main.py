from odoo import http
from odoo.http import request
import json

class MiniShop(http.Controller):

    # --------------------------------
    # INTERNAL: Get/Create User Cart
    # --------------------------------
    def _get_cart(self):
        session_id = request.session.sid
        Cart = request.env['mini.cart'].sudo()

        cart = Cart.search([('session_id', '=', session_id)], limit=1)
        if not cart:
            cart = Cart.create({'session_id': session_id})
        return cart

    # --------------------------------
    # 1) SHOP PAGE
    # --------------------------------
    @http.route('/mini/shop', type='http', auth='public', website=True)
    def mini_shop(self, **kw):
        selected_type = kw.get('type')
        domain = [('product_type', '=', selected_type)] if selected_type else []
        products = request.env['mini.product'].sudo().search(domain)

        return request.render('mini_commerce.shop_page', {
            'products': products,
            'selected_type': selected_type,
        })

    # --------------------------------
    # 2) PRODUCT PAGE
    # --------------------------------
    @http.route('/mini/product/<int:product_id>', type='http', auth='public', website=True)
    def product_detail(self, product_id):
        product = request.env['mini.product'].sudo().browse(product_id)
        return request.render('mini_commerce.product_page', {
            'product': product
        })

    # --------------------------------
    # 3) CART PAGE
    # --------------------------------
    @http.route('/mini/cart', type='http', auth='public', website=True)
    def mini_cart(self):
        cart = self._get_cart()

        items = []
        total = 0

        for line in cart.line_ids:
            price = line.product_id.base_price + (line.variant_id.extra_price if line.variant_id else 0)
            subtotal = price * line.qty

            items.append({
                'product': line.product_id,
                'variant': line.variant_id,
                'qty': line.qty,
                'subtotal': subtotal,
            })

            total += subtotal

        return request.render('mini_commerce.cart_page', {
            'items': items,
            'total': total,
        })

    # --------------------------------
    # 4) ADD TO CART (JS)
    # --------------------------------
    @http.route('/mini/add_to_cart_js', type='http', auth='public', methods=['POST'], csrf=False)
    def add_to_cart_js(self, **post):
        cart = self._get_cart()

        product_id = int(post.get('product_id'))
        variant_id = int(post.get('variant_id')) if post.get('variant_id') else False
        qty = int(post.get('qty') or 1)

        CartLine = request.env['mini.cart.line'].sudo()

        existing = CartLine.search([
            ('cart_id', '=', cart.id),
            ('product_id', '=', product_id),
            ('variant_id', '=', variant_id),
        ], limit=1)

        if existing:
            existing.qty += qty
        else:
            CartLine.create({
                'cart_id': cart.id,
                'product_id': product_id,
                'variant_id': variant_id,
                'qty': qty,
            })

        return request.make_response(
            json.dumps({'ok': True}),
            headers=[('Content-Type', 'application/json')]
        )

    # --------------------------------
    # 5) STOCK CHECK (JS)
    # --------------------------------
    @http.route('/mini/check_stock_js', type='http', auth='public', methods=['POST'], csrf=False)
    def check_stock_js(self, **post):
        product_id = int(post.get('product_id') or 0)
        variant_id = int(post.get('variant_id') or 0) if post.get('variant_id') else False
        qty = int(post.get('qty') or 0)

        Variant = request.env['mini.product.variant'].sudo()
        OrderLine = request.env['mini.order.line'].sudo()

        if variant_id:
            variant = Variant.browse(variant_id)

            # Calculating sold qty for confirmed orders
            sold_qty = sum(OrderLine.search([
                ('variant_id', '=', variant.id),
                ('order_id.state', '=', 'confirmed'),
            ]).mapped('quantity'))

            available = (variant.initial_qty or 0) - sold_qty

            if qty > available:
                data = {
                    'error': True,
                    'message': f"Only {max(available, 0)} pieces left for this color."
                }
                return request.make_response(
                    json.dumps(data),
                    headers=[('Content-Type', 'application/json')]
                )

        return request.make_response(
            json.dumps({'error': False}),
            headers=[('Content-Type', 'application/json')]
        )

    # --------------------------------
    # 6) CHECKOUT PAGE
    # --------------------------------
    @http.route('/mini/checkout', type='http', auth='public', website=True)
    def checkout_page(self):
        return request.render('mini_commerce.checkout_page')

    # --------------------------------
    # 7) SUBMIT CHECKOUT
    # --------------------------------
    @http.route('/mini/checkout/submit', type='http', auth='public', website=True, methods=['POST'])
    def checkout_submit(self, **post):
        order = request.env['mini.order'].sudo().create({
            'customer_name': post.get('name'),
            'customer_email': post.get('email'),
            'customer_phone': post.get('phone'),
            'state': 'confirmed',
        })

        cart = self._get_cart()

        for line in cart.line_ids:
            request.env['mini.order.line'].sudo().create({
                'order_id': order.id,
                'product_id': line.product_id.id,
                'variant_id': line.variant_id.id or False,
                'quantity': line.qty,
                'price_unit': line.product_id.base_price +
                              (line.variant_id.extra_price if line.variant_id else 0),
            })

        # Clear cart
        cart.line_ids.unlink()

        return request.redirect('/mini/confirm/%s' % order.id)

    # --------------------------------
    # 8) CONFIRM PAGE
    # --------------------------------
    @http.route('/mini/confirm/<int:order_id>', type='http', auth='public', website=True)
    def confirm_page(self, order_id):
        order = request.env['mini.order'].sudo().browse(order_id)
        return request.render('mini_commerce.confirm_page', {
            'order': order
        })
