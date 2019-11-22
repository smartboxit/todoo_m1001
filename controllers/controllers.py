# -*- coding: utf-8 -*-
from odoo import http

# class ZemployeeCarRequest(http.Controller):
#     @http.route('/zemployee_car_request/zemployee_car_request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zemployee_car_request/zemployee_car_request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('zemployee_car_request.listing', {
#             'root': '/zemployee_car_request/zemployee_car_request',
#             'objects': http.request.env['zemployee_car_request.zemployee_car_request'].search([]),
#         })

#     @http.route('/zemployee_car_request/zemployee_car_request/objects/<model("zemployee_car_request.zemployee_car_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zemployee_car_request.object', {
#             'object': obj
#         })