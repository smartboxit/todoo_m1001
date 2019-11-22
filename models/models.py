# -*- coding: utf-8 -*-

from odoo import models, fields, api



class CarRequest(models.Model):
    _name="car.request"   #db table name = card.request
    _description="car request"

    name=fields.char(string="Request",required="true")
    date_from=fields.datetime(string="Starting Date",default=fields.datetime.now)
    date_to=fields.datetime(string="End Date",required="false")

