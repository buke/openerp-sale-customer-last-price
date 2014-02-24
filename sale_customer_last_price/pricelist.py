# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright 2013 wangbuke <wangbuke@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import osv

class product_pricelist(osv.osv):
    _inherit = "product.pricelist"

    def _price_get_last(self, cr, uid, ids, prod_id, qty, partner=None, context=None):
        res = {'item_id': {1: 1}}
        states = ["confirmed","done"]
        cr.execute( 'SELECT sale_order_line.price_unit \
                FROM sale_order_line \
                JOIN sale_order \
                ON sale_order.id = sale_order_line.order_id  \
                AND sale_order.partner_id=%s \
                WHERE sale_order_line.product_id=%s \
                AND sale_order_line.state=ANY(%s) \
                ORDER BY sale_order_line.id DESC LIMIT 1',(partner,prod_id,states))
        re = [rid for (rid,) in cr.fetchall()]
        if re:
            res.update({1:re[0]})
        else:
            res = super(product_pricelist, self).price_get(cr, uid, ids, prod_id, qty, partner=partner, context=context)
        return res

    def price_get(self, cr, uid, ids, prod_id, qty, partner=None, context=None):
        if partner is None :
            return super(product_pricelist, self).price_get(cr, uid, ids, prod_id, qty, partner=partner, context=context)

        pricelist_default = self.pool.get('ir.property').get(cr, uid, 'property_product_pricelist', 'res.partner', context=context)
        pricelist_partner = self.pool.get('res.partner').browse(cr, uid, partner, context=context).property_product_pricelist

        if (pricelist_default.id == pricelist_partner.id):
            res = self._price_get_last(cr, uid, ids, prod_id, qty, partner=partner, context=context)
        else:  # this partner has price_list
            res = super(product_pricelist, self).price_get(cr, uid, ids, prod_id, qty, partner=partner, context=context)

        return res

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
