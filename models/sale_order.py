# -*- coding: utf-8 -*-
# Part of Odoo. Created by Shameena Moin.
from odoo import models, fields, api
import requests
import json

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_send_whatsapp(self):
        # Yahan hum Meta ki API call karenge
        pass
