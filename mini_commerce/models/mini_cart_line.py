from odoo import models, fields

class MiniCartLine(models.Model):
    _name = "mini.cart.line"
    _description = "Mini Cart Line"

    cart_id = fields.Many2one("mini.cart", required=True, ondelete="cascade")
    product_id = fields.Many2one("mini.product", required=True)
    variant_id = fields.Many2one("mini.product.variant")
    qty = fields.Integer(default=1)
