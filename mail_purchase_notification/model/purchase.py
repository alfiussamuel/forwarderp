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

    @api.multi
    def button_submit(self):
        for res in self:
            result = super(PurchaseOrder, self).button_submit()
            print ("Result ", result)
            if result:
                print ("If Result")
                mail_id = ''
                mail_to = "samuel.alfius@gmail.com"
                tmplt_id = self.env['mail.template'].search([("name", "=", "Purchase Order")])
                if tmplt_id:
                    tmplt_id.write({'email_to':mail_to})
                    mail_id = self.env['mail.template'].browse(tmplt_id.id).send_mail(res.id, force_send=True)
                    if not mail_id:
                        raise Warning('Email Not Sent')
                else:
                    raise Warning('Email Template Not Found')
