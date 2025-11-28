from odoo import models, fields

class MiniProduct(models.Model):
    _name = "mini.product"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Mini Product"

    name = fields.Char(required=True)
    description = fields.Text()
    base_price = fields.Float(string="Base Price", required=True)
    image = fields.Binary()
    variant_ids = fields.One2many("mini.product.variant", "product_id")
    product_type = fields.Selection([
        ('dress', 'Dress'),
        ('pants', 'Pants'),
        ('skirt', 'Skirt'),
        ('shoes', 'Shoes'),
        ('coat', 'Coat'),
    ], string="Product Type")
