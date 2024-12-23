class MerchantNotTrustedException(Exception):
    """Custom exception raised when the merchant score is too low."""
    def __init__(self, message="Merchant cannot be trusted due to low score."):
        super().__init__(message)

def check_merchant_score_and_call_kyc(merchant_score, threshold=50):
    """
    Checks the merchant's score and calls the KYC module if the score is acceptable.

    Args:
        merchant_score (int): The score of the merchant.
        threshold (int): The minimum score required to trust the merchant.

    Returns:
        str: A success message if the KYC module is called successfully.

    Raises:
        MerchantNotTrustedException: If the merchant score is below the threshold.
    """
    print(f"Checking merchant score: {merchant_score}")
    if merchant_score < threshold:
        raise MerchantNotTrustedException(f"Merchant score {merchant_score} is below the acceptable threshold {threshold}.")
    
    # Call the KYC module (example implementation)
    result = call_kyc_module(merchant_score)
    return result

def call_kyc_module(merchant_score):
    """
    Simulates calling the KYC module.

    Args:
        merchant_score (int): The merchant's score.

    Returns:
        str: A success message.
    """
    print(f"Calling KYC module for merchant with score: {merchant_score}")
    # Logic for KYC module call goes here
    return "KYC module called successfully!"

# Example usage
try:
    merchant_score = 45  # Replace with the actual merchant score
    print(check_merchant_score_and_call_kyc(merchant_score))
except MerchantNotTrustedException as e:
    print(e)
