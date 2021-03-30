{
    'name' : 'Email Notification for Purchase Order',
    'version' : '10',    
    'category': 'Custom',    
    'author' :'Alfius Samuel Sutopo',        
    'depends' : ['base','purchase'],
    'data': [                            
        'views/purchase_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
