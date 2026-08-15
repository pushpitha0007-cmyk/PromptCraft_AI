import streamlit as st

from prompt_optimizer import build_optimization_prompt
from llm_client import optimize_with_ai
from ai_evaluator import evaluate_prompt
from output_detector import detect_output_format
from prompt_guard import scan_prompt

st.set_page_config(
    page_title="PromptCraft AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 PromptCraft AI")
st.subheader("AI Prompt Optimizer & Analyzer")

st.write(
    "Turn simple instructions into powerful, structured AI prompts."
)

prompt = st.text_area(
    "Enter your prompt",
    placeholder="Example: explain machine learning",
    height=180
)

mode = st.selectbox(
    "Optimization Mode",
    [
        "General",
        "Academic",
        "Coding",
        "AI / ML",
        "Cybersecurity",
        "Research",
        "Professional",
        "Creative"
    ]
)

if st.button("✨ Analyze & Optimize", type="primary"):
    if not prompt.strip():
        st.warning("Please enter a prompt first.")
        st.stop()

    with st.spinner("🛡️ PromptGuard is scanning your prompt..."):
        guard_result = scan_prompt(prompt)
    st.markdown("---")
    st.markdown("## 🛡️ PromptGuard Security Scan")

    if guard_result["safe"]:

        st.success(
            f"🟢 SAFE — Risk Score: "
            f"{guard_result['risk_score']}/100"
        )

    else:

        if guard_result["risk_level"] == "High":

            st.error(
                f"🔴 HIGH RISK — Risk Score: "
                f"{guard_result['risk_score']}/100"
            )

        elif guard_result["risk_level"] == "Medium":

            st.warning(
                f"🟠 MEDIUM RISK — Risk Score: "
                f"{guard_result['risk_score']}/100"
            )

        else:

            st.info(
                f"🟡 LOW RISK — Risk Score: "
                f"{guard_result['risk_score']}/100"
            )

        st.markdown("### 🔎 Security Findings")

        for finding in guard_result["findings"]:

            category = (
                finding["category"]
                .replace("_", " ")
                .title()
            )

            st.write(
                f"⚠️ **{category}**"
            )


        st.markdown("### 💡 Recommendation")

        st.info(
            guard_result["recommendation"]
        )

    if (
        not guard_result["safe"]
        and guard_result["risk_score"] >= 75
    ):

        st.error(
            "🚫 Prompt blocked by PromptGuard because "
            "it contains high-risk instruction patterns."
        )

        st.stop()

    with st.spinner("🧠 AI is analyzing your prompt..."):

        evaluation = evaluate_prompt(prompt)


    st.markdown("---")

    st.markdown("## 🧠 AI Prompt Analysis")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Overall Score",
        f"{evaluation['overall_score']}/100"
    )

    col2.metric(
        "Clarity",
        evaluation["clarity"]
    )

    col3.metric(
        "Specificity",
        evaluation["specificity"]
    )


    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Context",
        evaluation["context"]
    )

    col2.metric(
        "Constraints",
        evaluation["constraints"]
    )

    col3.metric(
        "Output Format",
        evaluation["output_format"]
    )

    st.markdown("### 💪 Strengths")

    for strength in evaluation["strengths"]:

        st.write(
            f"✅ {strength}"
        )


    st.markdown("### ⚠️ Weaknesses")

    for weakness in evaluation["weaknesses"]:

        st.write(
            f"⚠️ {weakness}"
        )


    st.markdown("### 💡 Suggestions")

    for suggestion in evaluation["suggestions"]:

        st.write(
            f"💡 {suggestion}"
        )

    with st.spinner(
        "📤 Detecting expected output format..."
    ):

        output_format = detect_output_format(prompt)


    st.markdown("### 📤 Expected Output")

    st.info(output_format)

    st.markdown("---")

    st.markdown("## ✨ Optimized Prompt")


    optimization_prompt = build_optimization_prompt(
        prompt,
        mode
    )


    with st.spinner(
        "🚀 Creating optimized prompt..."
    ):

        optimized_prompt = optimize_with_ai(
            optimization_prompt
        )

    st.markdown("## 🔄 Before vs After")


    col1, col2 = st.columns(2)


    with col1:

        st.markdown("### ❌ Original Prompt")

        st.info(prompt)


    with col2:

        st.markdown("### ✅ Optimized Prompt")

        st.success(optimized_prompt)
    st.markdown("---")

    st.markdown(
        "### 📋 Optimized Prompt — Copy"
    )

    st.code(
        optimized_prompt,
        language="text"
    )


    st.success(
        "🎉 PromptGuard security scan, "
        "AI analysis, and prompt optimization completed!"
    )
