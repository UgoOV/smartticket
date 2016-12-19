import json
import warnings

from Code.raw_treatments.rawTreatment import RawTreatment

warnings.filterwarnings("ignore")

print "INTO LAMBDA ENRICH LOCATION PLACE"

# Load python files
r = RawTreatment()


def eventHandler(event, context):
    print "event init :", event
    print type(event)
    event = json.loads(event)

    if event['extraction_type'] == 'RAW':
        result = r.create_output(event)
        print result
        return result
    else:
        return {'smartticket': event, 'analytics_result': 'FAILURE'}


event = json.dumps({"status": "finished", "extraction_type": "RAW", "total": 43.8, "uuid": "20161213-1112-1230-19391", "retailer_name": "Inconnu", "lines": [{"total_price": None, "ocr_processed_description": "ReestCaurents Japeneis", "unit_price": None, "ocr_raw_description": None, "category_image_url": "http://cdn1.skerou.com/images/products/skerou_created/unknown_product.png", "quantity": None, "category_name": "NON RECONNU"}, {"total_price": None, "ocr_processed_description": "NEW KYUSHU", "unit_price": None, "ocr_raw_description": None, "category_image_url": "http://cdn1.skerou.com/images/products/skerou_created/unknown_product.png", "quantity": None, "category_name": "NON RECONNU"}, {"total_price": None, "ocr_processed_description": "3 4ixC 5AAL 36Rg", "unit_price": None, "ocr_raw_description": None, "category_image_url": "http://cdn1.skerou.com/images/products/skerou_created/unknown_product.png", "quantity": None, "category_name": "NON RECONNU"}, {"total_price": None, "ocr_processed_description": "168.Rue du Fbg Poissonniere", "unit_price": None, "ocr_raw_description": None, "category_image_url": "http://cdn1.skerou.com/images/products/skerou_created/unknown_product.png", "quantity": None, "category_name": "NON RECONNU"}, {"total_price": None, "ocr_processed_description": "75010 PARIS", "unit_price": None, "ocr_raw_description": None, "category_image_url": "http://cdn1.skerou.com/images/products/skerou_created/unknown_product.png", "quantity": None, "category_name": "NON RECONNU"}, {"total_price": None, "ocr_processed_description": "T6l:01.40.16.82.67", "unit_price": None, "ocr_raw_description": None, "category_image_url": "http://cdn1.skerou.com/images/products/skerou_created/unknown_product.png", "quantity": None, "category_name": "NON RECONNU"}, {"total_price": None, "ocr_processed_description": "RCS:Paris 753 686 716", "unit_price": None, "ocr_raw_description": None, "category_image_url": "http://cdn1.skerou.com/images/products/skerou_created/unknown_product.png", "quantity": None, "category_name": "NON RECONNU"}, {"total_price": None, "ocr_processed_description": "7x 2 0", "unit_price": None, "ocr_raw_description": None, "category_image_url": "http://cdn1.skerou.com/images/products/skerou_created/unknown_product.png", "quantity": None, "category_name": "NON RECONNU"}, {"total_price": None, "ocr_processed_description": "TABLE: 2 /3 Le 07/12/2016", "unit_price": None, "ocr_raw_description": None, "category_image_url": "http://cdn1.skerou.com/images/products/skerou_created/unknown_product.png", "quantity": None, "category_name": "NON RECONNU"}, {"total_price": None, "ocr_processed_description": "TABLE: 2 / 3 Le 07/12/2016", "unit_price": None, "ocr_raw_description": None, "category_image_url": "http://cdn1.skerou.com/images/products/skerou_created/unknown_product.png", "quantity": None, "category_name": "NON RECONNU"}, {"total_price": None, "ocr_processed_description": "Code Designation Qte Mont", "unit_price": None, "ocr_raw_description": None, "category_image_url": "http://cdn1.skerou.com/images/products/skerou_created/unknown_product.png", "quantity": None, "category_name": "NON RECONNU"}, {"total_price": None, "ocr_processed_description": "FV FORMULA A VOLONTE 3 36.00", "unit_price": None, "ocr_raw_description": None, "category_image_url": "http://cdn1.skerou.com/images/products/skerou_created/unknown_product.png", "quantity": None, "category_name": "NON RECONNU"}, {"total_price": None, "ocr_processed_description": "CCR COCA COLA ROUGE 1 2.60", "unit_price": None, "ocr_raw_description": None, "category_image_url": "http://cdn1.skerou.com/images/products/skerou_created/unknown_product.png", "quantity": None, "category_name": "NON RECONNU"}, {"total_price": None, "ocr_processed_description": "CCZ COCA ZERO 2 5.20", "unit_price": None, "ocr_raw_description": None, "category_image_url": "http://cdn1.skerou.com/images/products/skerou_created/unknown_product.png", "quantity": None, "category_name": "NON RECONNU"}, {"total_price": None, "ocr_processed_description": "***TOTAL 43.80", "unit_price": None, "ocr_raw_description": None, "category_image_url": "http://cdn1.skerou.com/images/products/skerou_created/unknown_product.png", "quantity": None, "category_name": "NON RECONNU"}, {"total_price": None, "ocr_processed_description": "Dont TVA 10.0% 3.98", "unit_price": None, "ocr_raw_description": None, "category_image_url": "http://cdn1.skerou.com/images/products/skerou_created/unknown_product.png", "quantity": None, "category_name": "NON RECONNU"}, {"total_price": None, "ocr_processed_description": "JOW.NEWKEYUSHU.COM BON\'APPETI", "unit_price": None, "ocr_raw_description": None, "category_image_url": "http://cdn1.skerou.com/images/products/skerou_created/unknown_product.png", "quantity": None, "category_name": "NON RECONNU"}, {"total_price": None, "ocr_processed_description": "MERCI ET A BIENTOT", "unit_price": None, "ocr_raw_description": None, "category_image_url": "http://cdn1.skerou.com/images/products/skerou_created/unknown_product.png", "quantity": None, "category_name": "NON RECONNU"}], "retailer_image_url": "http://cdn1.skerou.com/images/retailers/inconnu.png", "date": "13-12-2016 11:12", "nb_products": 0, "nb_recognized_products": 0, "store_address": {"latitude": None, "city": None, "street": None, "longitude": None, "zip_code": None}, "light_image_url": "http://receipts.fidmarques.com/receipts/production/21/2016/12/13/20161213-1112-1230-19391-1/20161213-1112-1230-19391-1_prerotated.jpg", "user_uuid": "antonio.calero@bnpparibas.com"})


eventHandler(event, '')