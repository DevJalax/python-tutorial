from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def calculate_transaction_score(merchant):
    score = 0
    sales_volume = merchant.get('sales_volume', 0)
    refunds = merchant.get('refunds', 0)
    chargebacks = merchant.get('chargebacks', 0)
    
    if sales_volume > 50000:
        score += 20
    elif 10000 <= sales_volume <= 50000:
        score += 15
    else:
        score += 5
    
    if refunds < 5:
        score += 15
    elif refunds < 20:
        score += 10
    else:
        score += 0
    
    if chargebacks < 1:
        score += 15
    elif chargebacks < 5:
        score += 10
    else:
        score += 0
    
    return score

def calculate_customer_feedback_score(merchant):
    score = 0
    reviews = merchant.get('reviews', [])
    avg_rating = sum(review['rating'] for review in reviews) / len(reviews) if reviews else 0
    
    if avg_rating >= 4.5:
        score += 20
    elif avg_rating >= 3.5:
        score += 15
    else:
        score += 5

    return score

def calculate_compliance_score(merchant):
    score = 0
    if merchant.get('is_compliant', False):
        score += 20
    else:
        score += 0
    return score

def calculate_aml_kyc_score(merchant):
    score = 0
    if merchant.get('kyc_verified', False):
        score += 15
    if merchant.get('aml_screening_passed', False):
        score += 15
    return score

def calculate_fraud_detection_score(merchant):
    score = 0
    fraud_alerts = merchant.get('fraud_alerts', 0)
    
    if fraud_alerts == 0:
        score += 20
    elif fraud_alerts <= 3:
        score += 10
    else:
        score += 0

    return score

def calculate_industry_benchmark_score(merchant):
    score = 0
    industry_rating = merchant.get('industry_rating', 0)
    
    if industry_rating >= 8:
        score += 20
    elif industry_rating >= 5:
        score += 10
    else:
        score += 5

    return score

def calculate_longevity_score(merchant):
    score = 0
    years_in_business = merchant.get('years_in_business', 0)
    
    if years_in_business > 10:
        score += 20
    elif years_in_business >= 5:
        score += 15
    else:
        score += 5

    return score

def calculate_online_presence_score(merchant):
    score = 0
    if merchant.get('has_ssl', False):
        score += 10
    if merchant.get('social_media_presence', False):
        score += 10

    return score

def calculate_supply_chain_score(merchant):
    score = 0
    if merchant.get('supplier_reviews', 0) > 4:
        score += 15
    else:
        score += 5

    return score

def calculate_merchant_trustworthiness(merchant_details):
    total_score = 0
    total_score += calculate_transaction_score(merchant_details)
    total_score += calculate_customer_feedback_score(merchant_details)
    total_score += calculate_compliance_score(merchant_details)
    total_score += calculate_aml_kyc_score(merchant_details)
    total_score += calculate_fraud_detection_score(merchant_details)
    total_score += calculate_industry_benchmark_score(merchant_details)
    total_score += calculate_longevity_score(merchant_details)
    total_score += calculate_online_presence_score(merchant_details)
    total_score += calculate_supply_chain_score(merchant_details)
    
    if total_score >= 150:
        trustworthiness = "Highly Trustworthy"
    elif 100 <= total_score < 150:
        trustworthiness = "Moderately Trustworthy"
    else:
        trustworthiness = "Not Trustworthy"

    # Return the response as a JSON object
    return {
        "merchant_score": total_score,
        "trustworthiness": trustworthiness
    }

@app.route('/merchant-score', methods=['POST'])
def get_merchant_score():
    merchant_details = request.json
    result = calculate_merchant_trustworthiness(merchant_details)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
