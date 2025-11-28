from odoo import models, fields, api

class MiniOrder(models.Model):
    _name = "mini.order"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Mini Order"

    name = fields.Char(default="New Order")
    customer_name = fields.Char(required=True)
    customer_email = fields.Char()
    customer_phone = fields.Char()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
    ], string="Status", default='draft', tracking=True)
    order_line_ids = fields.One2many("mini.order.line", "order_id")
    subtotal = fields.Float(compute="_compute_totals", store=True)
    tax = fields.Float(compute="_compute_totals", store=True)
    total = fields.Float(compute="_compute_totals", store=True)


    @api.depends("order_line_ids.subtotal")
    def _compute_totals(self):
        for order in self:
            order.subtotal = sum(order.order_line_ids.mapped("subtotal"))
            order.tax = order.subtotal * 0.16
            order.total = order.subtotal + order.tax

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_print_order(self):
        return self.env.ref('mini_commerce.report_mini_order_action').report_action(self)

