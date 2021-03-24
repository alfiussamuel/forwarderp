from odoo import api,fields,models,_
import time
from odoo.exceptions import UserError, RedirectWarning, ValidationError, except_orm, Warning
from datetime import datetime, date
from datetime import datetime, timedelta
from dateutil.relativedelta import *
from odoo.tools.safe_eval import safe_eval
import odoo.addons.decimal_precision as dp
from odoo.tools.float_utils import float_compare, float_round
from odoo.tools import email_re, email_split, email_escape_char, float_is_zero, float_compare, \
    pycompat, date_utils
import math
import re    
from num2words import num2words

class ResPartner(models.Model):    
    _inherit = "res.partner"

    credit_limit = fields.Float('Credit Limit')

class SaleOrder(models.Model):    
    _inherit = "sale.order"

    @api.model
    def create(self, vals):
        result = False
        
        if vals.get('name', _('New')) == _('New'):
            if 'company_id' in vals:
                vals['name'] = self.env['ir.sequence'].with_context(force_company=vals['company_id']).next_by_code('sale.order') or _('New')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code('sale.order') or _('New')

        partner = self.env['res.partner'].browse(vals.get('partner_id'))

        # Makes sure partner_invoice_id', 'partner_shipping_id' and 'pricelist_id' are defined
        if any(f not in vals for f in ['partner_invoice_id', 'partner_shipping_id', 'pricelist_id']):            
            addr = partner.address_get(['delivery', 'invoice'])
            vals['partner_invoice_id'] = vals.setdefault('partner_invoice_id', addr['invoice'])
            vals['partner_shipping_id'] = vals.setdefault('partner_shipping_id', addr['delivery'])
            vals['pricelist_id'] = vals.setdefault('pricelist_id', partner.property_product_pricelist and partner.property_product_pricelist.id)
        
        invoice_ids = self.env['account.invoice'].search([
            ('partner_id','=',partner.id), 
            ('state','=','open'),
            ])

        print ("Invoice IDS ", invoice_ids)

        unpaid_invoice_amount = 0
        if invoice_ids:
            for inv in invoice_ids:
                unpaid_invoice_amount += inv.residual
                print ("Invoice amount ", unpaid_invoice_amount)

        if unpaid_invoice_amount > partner.credit_limit and partner.credit_limit > 0:
            raise UserError(_('Credit Limit for this Customer reached the Limit'))
        else:
            result = super(SaleOrder, self).create(vals)

        return result    