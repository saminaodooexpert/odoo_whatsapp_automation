import requests
import json
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        # Jab aap Odoo mein 'Confirm' dabayengi, toh ye function chalega
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            self.send_whatsapp_message(order)
        return res

    def action_send_whatsapp(self):
        # Ye wo function hai jiski wajah se error aa raha tha
        for order in self:
            self.send_whatsapp_message(order)

    def send_whatsapp_message(self, order):
        # Aapka Access Token aur Phone ID
        token = "EAAZCNDwMtmpQBRPoIjHiBoo1qhP5bvZAQzF97KVP81GGTEd8zmPXgCDtFFVVX3cDpNprKt8YDmoWF85fFBiyHhwOGPRTpMDLFmXQSOrpsW4lRaMI8F6rMhpBXqHMn6NmS47AN5ixZA2XZAbvNX68eP9uIVtX8SVsAJjwTmqmdpbyUnjkqXpl9P44URYy86pkCZCmX6WrMEnD42iRqLHMhgRgLpNL8WkqHEkcv6sGKNfvINXOuHwEZAMKZB3wrV3fbEVAxF4k6hPfkOnTp1rd8cY"
        phone_id = "974135449126491"
        
        url = f"https://graph.facebook.com/v18.0/{phone_id}/messages"
        
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        recipient = order.partner_id.mobile or order.partner_id.phone
        
        if recipient:
            recipient = recipient.replace("+", "").replace(" ", "")
            
            payload = {
                "messaging_product": "whatsapp",
                "to": recipient,
                "type": "template",
                "template": {
                    "name": "hello_world",
                    "language": {
                        "code": "en_US"
                    }
                }
            }
            
            try:
                requests.post(url, headers=headers, data=json.dumps(payload))
            except Exception as e:
                print(f"Error: {str(e)}")
