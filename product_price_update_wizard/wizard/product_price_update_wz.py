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

    def update_price(self):
        if self.price_usd and self.products_ids:
            self.products_ids.write({'list_price': 1*self.price_usd})
            action = self.env.ref('product.product_product_tree_view').read()[0]

            action.update({
                'domain': [('id', 'in', [self.products_ids.id])]
            })

        return action


