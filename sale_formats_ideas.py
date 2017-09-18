# -*- coding: utf-8 -*-

from openerp import addons
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
#from dateutil.relativedelta import relativedelta
#from datetime import timedelta
from datetime import datetime
from datetime import date
#import time

class sale_formats(models.Model):
    _inherit = ['account.invoice']
   
    @api.multi
    def check_vat_mx(self, vat):
        # we convert to 8-bit encoding, to help the regex parse only bytes
        vatt = vat.replace('MX','')
       
        return vatt


