import requests
import json
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_send_whatsapp(self):
        """Ye function button dabane par WhatsApp bhejega"""
        url = "https://graph.facebook.com/v18.0/974135449126491/messages"
        
        headers = {
            "Authorization": "Bearer YOUR_ACCESS_TOKEN_HERE",
            "Content-Type": "application/json"
        }
        
        # Customer ka mobile number check karein
        phone = self.partner_id.mobile or self.partner_id.phone
        if not phone:
            return
            
        # Number se '+' ya spaces khatam karne ke liye
        phone = ''.join(filter(str.isdigit, phone))

        data = {
            "messaging_product": "whatsapp",
            "to": phone,
            "type": "template",
            "template": {
                "name": "hello_world",
                "language": {"code": "en_us"}
            }
        }
        
        try:
            response = requests.post(url, headers=headers, data=json.dumps(data))
            if response.status_code == 200:
                print("WhatsApp Message Sent Successfully!")
            else:
                print(f"Failed to send message: {response.text}")
        except Exception as e:
            print(f"Error occurred: {e}")

    def action_confirm(self):
        """Order confirm hote hi ye function chalega"""
        res = super(SaleOrder, self).action_confirm()
        # Agar aap chahti hain ke confirm hote hi message chala jaye:
        self.action_send_whatsapp()
        return res
