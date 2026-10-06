def predict_risk(
    water_level,
    water_flow,
    rainfall,
    mud_risk,
    animal_risk
):
    score = (
        water_level * 0.30
        + water_flow * 0.25
        + rainfall * 0.15
        + mud_risk * 0.15
        + animal_risk * 0.15
    )

    if score < 30:
        prediction = "SAFE"
    elif score < 60:
        prediction = "WARNING"
    elif score < 80:
        prediction = "DANGER"
    else:
        prediction = "CRITICAL"

    confidence = min(95, 60 + abs(score - 50) * 0.7)

    return prediction, confidence