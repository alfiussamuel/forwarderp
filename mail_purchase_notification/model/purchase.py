import time
import re
from collections import namedtuple
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.tools import float_is_zero
from odoo.exceptions import UserError, except_orm, Warning, RedirectWarning, ValidationError
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
import odoo.addons.decimal_precision as dp
from collections import defaultdict


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.model
    def create(self, vals):
        result = super().create(vals)
        if result:
            mail_id = ''
            mail_to = "samuel.alfius@gmail.com"
            tmplt_id = self.env['mail.template'].search([("name", "=", "Purchase Order")])
            if tmplt_id:
                tmplt_id.write({'email_to':mail_to})
                print ("Mail Belum ")
                mail_id = self.env['mail.template'].browse(tmplt_id.id).send_mail(result.id, force_send=True)
                print ("Mail ", mail_id)
                if not mail_id:
                    raise Warning('Email Not Sent')
            else:
                raise Warning('Email Template Not Found')

