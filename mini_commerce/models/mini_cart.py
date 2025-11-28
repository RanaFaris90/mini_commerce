from odoo import models, fields

class MiniCart(models.Model):
    _name = "mini.cart"
    _description = "Mini Shopping Cart"

    session_id = fields.Char(required=True)
    line_ids = fields.One2many("mini.cart.line", "cart_id")
