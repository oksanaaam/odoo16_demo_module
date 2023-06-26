from odoo import models, fields


class DemoDemo(models.Model):
    _name = "demo.demo"
    _description = "Demo Object"

    name = fields.Char(string="Name")
