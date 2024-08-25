from odoo import fields, models # type: ignore

class students (models.Model):
	_name = "students"
	_description = "Student Model"
	
	image = fields.Binary()
	name = fields.Char(string="Nama")
	code = fields.Char(string="NIM")
	trial_date = fields.Date(string="Trial Date")
	state = fields.Selection([
		('waiting','Waiting'),
		('success','Success'),
		('failed','Failed'),
		],default='waiting', string='Status')

	def button_success(self):
		self.state='success'
	
	def button_failed(self):
	    self.state='failed'

	 
	
