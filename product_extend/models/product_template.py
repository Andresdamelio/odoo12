# -*- coding: utf-8 -*-

from odoo import api, models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    tipology = fields.Selection(
        string="Tipo de material",
        selection=[('metal', 'Metal'), ('pvc', 'PVC'), ('cristal', 'Cristal')]
    )
