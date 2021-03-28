12.0.1 (21 FEB 2020)
=======
- initial release.


code changed.
                    if stock_picking_line.quantity_done == stock_picking_line.product_uom_qty + 1:
                        raise Warning('Becareful! Quantity exceed than initial demand!')  
- Inventoried Location problem solved in inventory adjustment barcode scan.(Inventoried Location and Location in inventory line must be same)
- new standard odoo widget="barcode_handler" implemented.
- new settings given to scan internal reference or barcode or both.
- in picking, product uom qty is set to 1 rather than 0 when first barcode scanned.
- In lines, Last scanned product move to top, Last scanned product change color and play sound while warning/error features added.
- Auto close error/alert message popup after some miliseconds.
- Multi Barcodes Supported
- Bug Fixed: in Sale, Discount not apply from pricelist when product added by Scanner.
	call line._onchange_discount() method in sale model file.
	
	
	
12.0.2 (Date: 11 July 2020)
=========================
==> QR Scanning Support Added.

12.0.3 (Date: 1 Oct 2020)
=========================
==> multi barcode bug fixed.


12.0.4 (Date: 26 Jan 2021)
=========================
==> [Fixed] multi barcode read access for normal user given in csv file(base.group_user) (product.template.barcode)

12.0.5 (22 Feb 2021)
==================
==> [Add] Global Document Search Added.
==> [Add] Scan Barcode and add into barcode field in product variant and template.

