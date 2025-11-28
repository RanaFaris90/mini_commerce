from odoo import models, fields,api

class MiniProductVariant(models.Model):
    _name = "mini.product.variant"
    _description = "Mini Product Variant"

    product_id = fields.Many2one("mini.product", required=True)
    color = fields.Char()
    extra_price = fields.Float(string="Extra Price")
    stock = fields.Integer(default=0)
    image = fields.Binary("Variant Image")
    quantity_on_hand = fields.Integer(
        string="Quantity On Hand",
        compute="_compute_quantity_on_hand",
    )
    initial_qty = fields.Integer(string="Initial Stock", default=0)
    size = fields.Selection([
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'X-Large'),
    ], required=True)

    def _compute_quantity_on_hand(self):
        OrderLine = self.env['mini.order.line'].sudo()

        for variant in self:
            sold_qty = sum(
                OrderLine.search([
                    ('variant_id', '=', variant.id),
                    ('order_id.state', '=', 'confirmed')
                ]).mapped('quantity')
            )
            variant.quantity_on_hand = variant.initial_qty - sold_qty

