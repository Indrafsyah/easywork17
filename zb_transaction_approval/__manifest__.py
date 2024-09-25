# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2024 ZestyBeanz Technologies.
#    (http://wwww.zbeanztech.com)
#    contact@zbeanztech.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Transaction Approval',
    'version': '17.0.0.1',
    'category': 'All',
    'summary': """Approval functionality in Sales Order, Purchase Order, Accounting Entries, Payments.""",
    'description': """
        Approval functionality in
        - Sales Order
        - Purchase Order
        - Accounting Entries
        - Payments.
    """,
    'author': 'ZestyBeanz Technologies',
    'maintainer': 'ZestyBeanz Technologies',
    'support': 'support@zbeanztech.com',
    'website': 'http://www.zbeanztech.com/',
    'license': 'LGPL-3',
    'icon': "/zb_transaction_aproval/static/description/icon.png",
    'images': ['static/description/banners/banner.png',],
    'currency': 'USD',
    'price': 0.0,
    'depends': [
        'purchase', 'sale_management'
    ],
    'data': [
      'security/security.xml',
      'data/mail_template_approval.xml',
      'data/mail_template_purchase_approval.xml',
      'data/mail_template_invoice_approval.xml',
      'data/mail_template_payment_approval.xml',
      'views/sale_order_view.xml',
      'views/purchase_order_view.xml',
      'views/account_move_view.xml',
      'views/account_payment_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
