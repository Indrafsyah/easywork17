from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    last_purchase_qty = fields.Float(string="Last Quantity", compute="_compute_last_purchase_qty_price")
    last_purchase_price = fields.Float(string="Last Price", compute="_compute_last_purchase_qty_price")

    def _compute_last_purchase_qty_price(self):
        for po_line_id in self:
            po_line_id.last_purchase_qty = 0
            po_line_id.last_purchase_price = 0
            if type(po_line_id.id) == int:
                last_po_line_id = self.search(
                    [('product_id', '=', po_line_id.product_id.id), ('partner_id', '=', po_line_id.partner_id.id),
                     ('id', '!=', po_line_id.id)],
                    order='id desc', limit=1)
            else:
                last_po_line_id = self.search(
                    [('product_id', '=', po_line_id.product_id.id), ('partner_id', '=', po_line_id.partner_id.id),
                     ('id', '!=', po_line_id.id.origin)],
                    order='id desc', limit=1)

            if last_po_line_id:
                po_line_id.last_purchase_qty = last_po_line_id.product_qty
                po_line_id.last_purchase_price = last_po_line_id.price_unit

