
{
    'name': 'Credit Limit Validation for Customer',
    'category': 'Custom',
    'author' :'Business Solution Consulting',
    'depends' : [
                 'base',
                 'sale',
                 'account',                 
                ],
    'data': [                          
             'views/credit_limit_view.xml',             
             ],
             
    'installable': True,
    'application': True,
    'auto_install': False,
}
