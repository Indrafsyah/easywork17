{
    'name': 'Meeting Management',
    'version': '17.0',
    'category': 'Productivity/Calendar',
    'summary': 'Manage Minute Meeting in Calender',
    'author': 'INKERP',
    'website': 'https://www.inkerp.com/',
    'depends': ['calendar'],
    
    'data': [
        'security/ir.model.access.csv',
        'views/minute_meeting_view.xml',
    ],
    
    'images': ['static/description/banner.png'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}
