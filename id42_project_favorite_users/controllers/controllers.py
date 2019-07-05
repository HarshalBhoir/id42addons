# -*- coding: utf-8 -*-
from odoo import http

# class Id42ProjectFavorites(http.Controller):
#     @http.route('/id42_project_favorites/id42_project_favorites/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/id42_project_favorites/id42_project_favorites/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('id42_project_favorites.listing', {
#             'root': '/id42_project_favorites/id42_project_favorites',
#             'objects': http.request.env['id42_project_favorites.id42_project_favorites'].search([]),
#         })

#     @http.route('/id42_project_favorites/id42_project_favorites/objects/<model("id42_project_favorites.id42_project_favorites"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('id42_project_favorites.object', {
#             'object': obj
#         })