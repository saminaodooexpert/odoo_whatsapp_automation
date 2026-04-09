import requests
import json
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_send_whatsapp(self):
        """Ye function button dabane par WhatsApp bhejega"""
        # Aapka verified Phone Number ID aur Token yahan set hain
        url = "https://graph.facebook.com/v18.0/974135449126491/messages"
        
        headers = {
            "Authorization": "Bearer EAAZCNDwMtmpQBRPoIjHiBoo1qhP5bvZAQzF97KVP81GGTEd8zmPXgCDtFFVVX3cDpNprKt8YDmoWF85fFBiyHhwOGPRTpMDLFmXQSOrpsW4lRaMI8F6rMhpBXqHMn6NmS47AN5ixZA2XZAbvNX68eP9uIVtX8SVsAJjwTmqmdpbyUnjkqXpl9P44URYy86pkCZCmX6WrMEnD42iRqLHMhgRgLpNL8WkqHEkcv6sGKNfvINXOuHwEZAMKZB3wrV3fbEVAxF4k6hPfkOnTp1rd8cY",
            "Content-Type": "application/json"
        }
        
        # Customer ka mobile number check karein
        phone = self.partner_id.mobile or self.partner_id.phone
        if not phone:
            print("Error: No phone number found for this customer!")
            return
            
        # Number se formatting khatam karke sirf digits rakhne ke liye
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
                print(f"Meta Error: {response.text}")
        except Exception as e:
            print(f"Connection Error: {e}")

    def action_confirm(self):
        """Order confirm hote hi WhatsApp message bhejega"""
        res = super(SaleOrder, self).action_confirm()
        # Confirm button dabate hi ye line chalegi
        self.action_send_whatsapp()
        return res
