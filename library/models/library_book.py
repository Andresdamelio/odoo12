# -*- coding: utf-8 -*-

from odoo import api, models, fields, exceptions


class LibraryBook(models.Model):
    _name = "library.book"

    name = fields.Char(string="Book", default="New")
    isbn = fields.Char(string="ISBN")
    description = fields.Text(string="Description")

    # campos calculados
    categ_count = fields.Integer(
        string="Numero de categorias",
        compute="_count_categ")

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

    # Como definir un constrain para postgres
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (name)', 'El nombre del libro es unico, y ya existe en los registros'),
    ]

    # Como definir un constrain con python
    @api.constrains('isbn')
    def check_isbn(self):
        isbn = self.search([['id', '!=', self.id]]).mapped("isbn")
        if self.isbn and self.isbn in isbn:
            raise exceptions.ValidationError("Isbn duplicado")

    def _count_categ(self):
        for book in self:
            book.categ_count = len(book.category_id)
