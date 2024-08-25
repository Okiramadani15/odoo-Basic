from odoo import fields, models

class MyPurchase(models.Model):
    _name = "my_purchase.purchase"
    _description = "Purchase Model"

    name = fields.Char(string="Jenis Pembelian")
    date = fields.Date(string="Tanggal Pembelian")
    status = fields.Selection([
        ('draft', 'Draft'),
        ('approve', 'Approve'),
        ('done', 'done'),
    ], default='draft')

    def button_success(self):
        for record in self:
            record.status = 'success'
