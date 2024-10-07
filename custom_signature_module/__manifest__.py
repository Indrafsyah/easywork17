{
    'name': 'Custom Signature in Reports',
    'version': '1.0',
    'summary': 'Adds signature fields to Purchase Request, Purchase Order, Picking Operations, and Delivery Slip reports',
    'category': 'Purchases',
    'author': 'Your Name',
    'depends': ['purchase', 'stock', 'purchase_request'],
    'data': [
        'views/custom_report_views.xml',
        'report/custom_report.xml',
    ],
    'installable': True,
    'application': False,
}
