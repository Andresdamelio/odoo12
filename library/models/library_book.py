# -*- coding: utf-8 -*-

from odoo import models, fields


class LibraryBook(models.Model):
    _name = "library.book"

    name = fields.Char(string="Book", default="New")
    description = fields.Text(string="Description")

    """"
    =================== Como crear una relacion Many2one ===================
    """
    # category_id = fields.Many2one(
    #     comodel_name="library.category", string="Category"
    # )
    """"
    =================== Como crear una relacion Many2Many ===================
    """
    # category_id = fields.Many2many(
    #     comodel_name="library.category", string="Category"
    # )

    """"
    =================== Como crear una relacion Many2Many ===================
    """
    category_id = fields.One2many(
        comodel_name="library.category",
        inverse_name= "book_id",
        string="category"
    )

