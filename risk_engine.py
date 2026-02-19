def calculate_risk(failed_attempts, geo_mismatch, unusual_time):
    score = 0

    if failed_attempts > 3:
        score += 40

    if geo_mismatch:
        score += 30

    if unusual_time:
        score += 20

    return score


# Example simulation
if __name__ == "__main__":
    risk_score = calculate_risk(
        failed_attempts=4,
        geo_mismatch=True,
        unusual_time=False
    )

    print("Calculated Risk Score:", risk_score)

    if risk_score >= 50:
        print("Action: Trigger MFA")
    else:
        print("Action: Allow login")
