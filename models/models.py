# -*- coding: utf-8 -*-

from odoo import models, fields, api



class CarRequest(models.Model):
    _name="car.request"   #db table name = card.request
    _description="car request"

    name=fields.Char(string="Request",required=True)
    date_from=fields.Datetime(string="Starting Date",default=fields.datetime.now())
    date_to=fields.Datetime(string="End Date",required=False)
    employee_id=fields.Many2one(
        string='employee',
        comodel_name='hr.employee',
        ondelete='restrict',
        required=True
    )   
    car_id=fields.Many2one(
        string='car',
        comodel_name='fleet.vehicle',
        ondelete='restrict', 
        required=True
    ) 
    state=fields.Selection(
        string='Status',
        selection=[('draft','Draft') , ('confirm','Confirm') , ('validate','Validate') , ('refuse','Refuse') , ('approve','Approve') ],
        default='draft'
    )
    
                                
    
