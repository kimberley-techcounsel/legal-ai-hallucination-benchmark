import re
import streamlit as st

st.set_page_config(
    page_title="Legal AI Hallucination Checker",
    page_icon="⚖️",
    layout="centered"
)

RISK_TERMS = {
    "always": 2,
    "automatically": 2,
    "every": 2,
    "exactly": 2,
    "absolute": 3,
    "whenever": 1,
    "universal": 2,
    "guaranteed": 2,
    "must": 1,
    "24 hours": 3,
    "30 days": 2,
}

def analyze_claim(text):
    normalized = text.lower().strip()
    score = 0
    matches = []

    for term, weight in RISK_TERMS.items():
        if term in normalized:
            score += weight
            matches.append((term, weight))

    # Extra signal: very precise numeric deadlines can deserve source checking.
    deadline_pattern = r"\b\d+\s+(?:calendar\s+|business\s+)?(?:day|days|hour|hours|month|months|year|years)\b"
    deadlines = re.findall(deadline_pattern, normalized)

    if deadlines:
        score += 1

    if score >= 6:
        level = "High"
        action = "Priority source verification"
    elif score >= 3:
        level = "Moderate"
        action = "Source verification recommended"
    elif score >= 1:
        level = "Low"
        action = "Review supporting authority"
    else:
        level = "No lexical flag"
        action = "No language-based warning detected"

    return {
        "score": score,
        "matches": matches,
        "deadlines": deadlines,
        "level": level,
        "action": action
    }

st.title("⚖️ Legal AI Hallucination Checker")
st.caption("A transparent legal-AI screening prototype for identifying claims that may need authoritative-source verification.")

st.info(
    "This tool does not determine whether a legal claim is true or false. "
    "It identifies language patterns that may justify closer legal verification."
)

claim = st.text_area(
    "Enter a legal proposition",
    height=160,
    placeholder="Example: The GDPR always requires companies to notify users exactly 30 days before changing a privacy policy."
)

col1, col2 = st.columns(2)
analyze = col1.button("Analyze claim", type="primary", use_container_width=True)
clear = col2.button("Clear", use_container_width=True)

if clear:
    st.rerun()

if analyze:
    if not claim.strip():
        st.warning("Enter a legal proposition first.")
    else:
        result = analyze_claim(claim)

        st.divider()
        st.subheader("Screening result")

        c1, c2 = st.columns(2)
        c1.metric("Lexical risk score", result["score"])
        c2.metric("Review level", result["level"])

        st.write(f"**Recommended action:** {result['action']}")

        if result["matches"]:
            st.write("**Detected linguistic signals**")
            for term, weight in result["matches"]:
                st.write(f"- `{term}` — +{weight}")
        else:
            st.write("**Detected linguistic signals:** None from the current rule set.")

        if result["deadlines"]:
            st.write("**Specific time periods detected**")
            for deadline in result["deadlines"]:
                st.write(f"- `{deadline}`")

        st.subheader("Why this is not a legal conclusion")
        st.write(
            "Correct legal rules can use categorical wording, while hallucinated legal claims can sound cautious and professional. "
            "A reliable legal-AI workflow must therefore retrieve the relevant authority, confirm that it exists and is current, "
            "and test whether it actually supports the proposition."
        )

        st.subheader("Suggested verification workflow")
        st.write(
            "1. Identify the jurisdiction and applicable date.\n"
            "2. Locate primary or authoritative legal sources.\n"
            "3. Confirm that any cited authority exists.\n"
            "4. Compare the claim with the text and scope of the authority.\n"
            "5. Escalate uncertain or high-impact conclusions for human legal review."
        )

st.divider()
st.caption(
    "Portfolio prototype only — not legal advice and not a production hallucination-detection system."
)
