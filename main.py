# CyberGuard Africa - Basic Scam Detector

scam_keywords = [
    "send money",
    "urgent",
    "winner",
    "lottery",
    "claim now",
    "congratulations",
    "limited time",
    "account suspended",
    "verify now"
]


def detect_scam(message):
    message = message.lower()

    score = 0

    for word in scam_keywords:
        if word in message:
            score += 1

    if score >= 2:
        return "🚨 Likely Scam"
    elif score == 1:
        return "⚠️ Suspicious"
    else:
        return "✅ Likely Safe"


# Test it
if __name__ == "__main__":
    msg = input("Enter message: ")
    result = detect_scam(msg)
    print(result)
