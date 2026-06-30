def generate_recommendations(customer):
    """
    Generate personalized retention recommendations
    based on customer characteristics.
    """

    recommendations = []

    # Customer is inactive
    if customer["is_active_member"] == 0:
        recommendations.append(
            "Launch a personalized re-engagement campaign."
        )

    # Customer owns only one product
    if customer["num_of_products"] <= 1:
        recommendations.append(
            "Recommend additional banking products through cross-selling."
        )

    # High balance customers deserve personal attention
    if customer["balance"] >= 100000:
        recommendations.append(
            "Assign a dedicated relationship manager."
        )

    # Low credit score
    if customer["credit_score"] < 600:
        recommendations.append(
            "Provide personalized financial planning assistance."
        )

    # Senior customers
    if customer["age"] >= 55:
        recommendations.append(
            "Offer senior customer loyalty benefits."
        )

    # High salary customers
    if customer["estimated_salary"] >= 100000:
        recommendations.append(
            "Recommend premium banking services."
        )

    # Germany has relatively higher churn in this dataset
    if customer["geography_Germany"] == 1:
        recommendations.append(
            "Provide region-specific retention offers."
        )

    # Safe customer
    if len(recommendations) == 0:
        recommendations.append(
            "Customer has low churn risk. Continue regular engagement."
        )

    return recommendations