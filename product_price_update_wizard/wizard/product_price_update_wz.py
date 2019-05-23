# -*- coding: utf-8 -*-

from odoo import api, models, fields


class ProductPriceUpdateWizard(models.TransientModel):
    _name = 'product.price.update.wizard'

    price_usd = fields.Float(
        string="Precio del dolar",
        required=True,
        help="Ingresa el precio actualizado del dolar."
    )

    products_ids = fields.Many2many('product.product')

    @api.model
    def default_get(self, fields_list):
        res = super(ProductPriceUpdateWizard, self).default_get(fields_list)
        act_ids = self._context.get('active_ids')

        res.update({
            'products_ids': [(6, 0, act_ids)]
        })

        return res

    # @api.multi
    # def create_purchase(self):
    #     if self.order_line_ids and self.supplier_id:
    #         # En este instante se va a crear el pedido de compra
    #         order_id = self.env['purchase.order'].create({
    #             'partner_id': self.supplier_id.id
    #         })
    #
    #         self.order_line_ids.write({'order_id': order_id.id})
    #
    #         action = self.env.ref('purchase.purchase_form_action').read()[0]
    #
    #         action.update({
    #             'domain': [('id', 'in', [order_id.id])]
    #         })
    #
    #     return action


