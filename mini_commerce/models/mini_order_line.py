from odoo import models, fields, api

class MiniOrderLine(models.Model):
    _name = "mini.order.line"
    _description = "Mini Order Line"

    order_id = fields.Many2one("mini.order", required=True)
    product_id = fields.Many2one("mini.product", required=True)
    variant_id = fields.Many2one("mini.product.variant")
    quantity = fields.Integer(default=1)
    price_unit = fields.Float()
    subtotal = fields.Float(compute="_compute_subtotal", store=True)
    size = fields.Selection(
        [
            ('S', 'Small'),
            ('M', 'Medium'),
            ('L', 'Large'),
            ('XL', 'X-Large')
        ],
        string="Size"
    )
    @api.onchange("product_id", "variant_id")
    def _onchange_price(self):
        if self.product_id:
            base = self.product_id.base_price
            extra = self.variant_id.extra_price if self.variant_id else 0
            self.price_unit = base + extra

    @api.depends("price_unit", "quantity")
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.price_unit * line.quantity
