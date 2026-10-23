
import re
from datetime import datetime

import pandas as pd
import streamlit as st

# =====================================================
# 1. PAGE CONFIGURATION
# =====================================================
st.set_page_config(
    page_title="Secure File Scanner",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =====================================================
# 2. DARK NAVY + TEAL THEME
# =====================================================
st.markdown(
    """
    <style>
    :root {
        --bg: #08111f;
        --panel: #101d30;
        --border: #263950;
        --teal: #2dd4bf;
        --text: #e5edf7;
        --muted: #94a8bd;
    }

    .stApp {
        background: var(--bg);
        color: var(--text);
    }

    [data-testid="stHeader"] {
        background: #08111f;
    }

    [data-testid="stSidebar"] {
        background: #0c1829;
        border-right: 1px solid var(--border);
    }

    [data-testid="stSidebar"] * {
        color: var(--text);
    }

    h1, h2, h3 {
        color: #f1f7ff !important;
    }

    p, label, .stMarkdown {
        color: var(--text);
    }

    /* HEADER */
    .hero {
        padding: 28px 30px;
        border: 1px solid #24505b;
        border-radius: 18px;
        background: linear-gradient(
            120deg, #10263a, #102b38, #103b40
        );
        margin-bottom: 24px;
    }

    .hero-tag, .section-label {
        color: #5eead4;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 1.6px;
        text-transform: uppercase;
    }

    .hero-title {
        color: #f4fbff;
        font-size: 34px;
        font-weight: 750;
        margin: 8px 0;
    }

    .hero-description {
        color: #b4c8d9;
        font-size: 15px;
        line-height: 1.7;
    }

    /* DASHBOARD CARDS */
    .metric-card {
        background: var(--panel);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 19px 20px;
        min-height: 110px;
    }

    .metric-label {
        color: var(--muted);
        font-size: 13px;
        margin-bottom: 10px;
    }

    .metric-value {
        color: var(--teal);
        font-size: 30px;
        font-weight: 750;
    }

    .metric-danger {
        color: #fb7185;
    }

    .panel {
        background: var(--panel);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 20px;
        margin: 12px 0 20px;
    }

    .muted {
        color: var(--muted);
        font-size: 13px;
    }

    /* SEVERITY BADGES */
    .severity {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
    }

    .severity-low {
        color: #6ee7b7;
        background: #12372f;
        border: 1px solid #22634f;
    }

    .severity-medium {
        color: #fcd34d;
        background: #3a2d14;
        border: 1px solid #72551c;
    }

    .severity-high {
        color: #fda4af;
        background: #421e2a;
        border: 1px solid #813247;
    }

    /* ================================================
       FILE UPLOADER
       ================================================ */

    [data-testid="stFileUploader"] {
        background: #101d30 !important;
        border: 1px dashed #2dd4bf !important;
        border-radius: 12px !important;
        padding: 12px !important;
    }

    [data-testid="stFileUploader"] section {
        background: #101d30 !important;
        border: none !important;
    }

    [data-testid="stFileUploaderDropzone"] {
        background: #101d30 !important;
        border: 1px dashed #36727a !important;
        border-radius: 9px !important;
    }

    /* Upload instructions and size text */
    [data-testid="stFileUploaderDropzone"] small,
    [data-testid="stFileUploaderDropzone"] span,
    [data-testid="stFileUploaderDropzone"] p {
        color: #cbd5e1 !important;
        -webkit-text-fill-color: #cbd5e1 !important;
        opacity: 1 !important;
    }

    /* Upload button */
    [data-testid="stFileUploaderDropzone"] button {
        background: #0d9488 !important;
        color: #ffffff !important;
        border: 1px solid #2dd4bf !important;
        border-radius: 8px !important;
        opacity: 1 !important;
    }

    [data-testid="stFileUploaderDropzone"] button * {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        fill: #ffffff !important;
        opacity: 1 !important;
    }

    /* ================================================
       SELECTED FILE CARD
       White background + dark readable filename
       ================================================ */

    [data-testid="stFileUploaderFile"] {
        background: #ffffff !important;
        border: 1px solid #d5e2ed !important;
        border-radius: 10px !important;
        opacity: 1 !important;
        filter: none !important;
    }

    /* Filename */
    [data-testid="stFileUploaderFile"] p,
    [data-testid="stFileUploaderFile"] span,
    [data-testid="stFileUploaderFile"] a {
        color: #14253a !important;
        -webkit-text-fill-color: #14253a !important;
        opacity: 1 !important;
        text-shadow: none !important;
    }

    /* File size */
    [data-testid="stFileUploaderFile"] small {
        color: #475569 !important;
        -webkit-text-fill-color: #475569 !important;
        opacity: 1 !important;
    }

    /* File icon */
    [data-testid="stFileUploaderFile"] svg {
        color: #334155 !important;
        stroke: #334155 !important;
        opacity: 1 !important;
    }

    /* ================================================
       REMOVE FILE BUTTON
       Explicitly style button and icon
       ================================================ */

    [data-testid="stFileUploaderFile"] button {
        background-color: #ffffff !important;
        border: 1.5px solid #0d9488 !important;
        border-radius: 50% !important;
        width: 24px !important;
        min-width: 24px !important;
        height: 24px !important;
        min-height: 24px !important;
        padding: 0 !important;
        margin: 0 !important;
        opacity: 1 !important;
        visibility: visible !important;
        box-shadow: none !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* Make the remove icon visible */
    [data-testid="stFileUploaderFile"] button svg {
        color: #0d9488 !important;
        stroke: #0d9488 !important;
        fill: none !important;
        opacity: 1 !important;
        visibility: visible !important;
        display: block !important;
    }

    [data-testid="stFileUploaderFile"] button path,
    [data-testid="stFileUploaderFile"] button line,
    [data-testid="stFileUploaderFile"] button polyline {
        stroke: #0d9488 !important;
        fill: none !important;
        opacity: 1 !important;
    }

    [data-testid="stFileUploaderFile"] button:hover {
        background: #ccfbf1 !important;
        border-color: #0f766e !important;
    }

    [data-testid="stFileUploaderFile"] button:hover svg {
        color: #0f766e !important;
        stroke: #0f766e !important;
    }

    /* GENERAL BUTTONS */
    .stButton > button,
    .stDownloadButton > button {
        background: #0d9488 !important;
        color: #ffffff !important;
        border: 1px solid #2dd4bf !important;
        border-radius: 9px !important;
        font-weight: 650;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover {
        background: #0f766e !important;
        border-color: #5eead4 !important;
        color: #ffffff !important;
    }

    /* RESULTS TABLE */
    [data-testid="stDataFrame"] {
        border: 1px solid var(--border);
        border-radius: 10px;
        overflow: hidden;
    }

    [data-testid="stExpander"] {
        background: var(--panel);
        border: 1px solid var(--border);
        border-radius: 10px;
        margin-bottom: 8px;
    }

    hr {
        border-color: var(--border);
    }

    .footer-note {
        color: #7f94aa;
        font-size: 12px;
        text-align: center;
        padding: 20px 0 8px;
    }

    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =====================================================
# 3. HEADER
# =====================================================
st.markdown(
    """
    <div class="hero">
        <div class="hero-tag">CYBERSECURITY · DATA PROTECTION</div>
        <div class="hero-title">🛡️ Secure File Scanner</div>
        <div class="hero-description">
            Identify potential sensitive-data patterns, review findings,
            and generate structured scan reports from uploaded text files.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.info(
    "Educational prototype: use fictional test files only. "
    "Detected patterns are not proof of a data leak. "
    "Severity levels are illustrative and require analyst review."
)

# =====================================================
# 4. SENSITIVE-DATA PATTERNS
# =====================================================
PATTERNS = {
    "Email Address":
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "Phone Number":
        r"(?<!\w)(?:\+?\d[\d\s().-]{7,}\d)(?!\w)",
}

# =====================================================
# 5. SESSION STATE
# =====================================================
if "scan_results" not in st.session_state:
    st.session_state.scan_results = None

# =====================================================
# 6. INCIDENT GUIDANCE
# =====================================================
def get_guidance(findings):
    if not findings:
        return (
            "No configured sensitive-data patterns were detected.",
            "Continue following normal data-handling procedures.",
        )

    if "Email Address" in findings and "Phone Number" in findings:
        return (
            "Potential email address and phone number patterns detected.",
            "Review the data's purpose, sensitivity, and sharing "
            "permissions. Escalate if required by organizational policy.",
        )

    if "Email Address" in findings:
        return (
            "A potential email address pattern was detected.",
            "Review the file's purpose and access permissions "
            "to determine whether the information is authorized.",
        )

    if "Phone Number" in findings:
        return (
            "A potential phone number pattern was detected.",
            "Review sensitivity and confirm that storage and sharing "
            "are authorized.",
        )

    return (
        "A configured pattern was detected.",
        "Review the finding according to organizational policy.",
    )

# =====================================================
# 7. FILE SCANNING
# =====================================================
def scan_file(filename, content):
    text = content.decode("utf-8", errors="ignore")
    findings = []

    for category, pattern in PATTERNS.items():
        if re.search(pattern, text):
            findings.append(category)

    # Demonstration severity rules only
    if not findings:
        severity = "Low"
        status = "No configured patterns found"
    elif "Phone Number" in findings:
        severity = "High"
        status = "Review required"
    else:
        severity = "Medium"
        status = "Review required"

    description, action = get_guidance(findings)

    scan_time = datetime.now().astimezone().strftime(
        "%Y-%m-%d %H:%M:%S %Z"
    )

    return {
        "File Name": filename,
        "Scan Time": scan_time,
        "Findings": ", ".join(findings) if findings else "None",
        "Finding Count": len(findings),
        "Suggested Severity": severity,
        "Incident Description": description,
        "Recommended Action": action,
        "Status": status,
    }

# =====================================================
# 8. SIDEBAR
# =====================================================
with st.sidebar:
    st.markdown("## 🛡️ Secure Scanner")
    st.caption("DATA PROTECTION WORKSPACE")
    st.divider()

    st.markdown("### Detection rules")
    st.markdown("- Email address patterns")
    st.markdown("- Phone number patterns")

    st.divider()
    st.markdown("### Severity guide")

    st.markdown(
        '<span class="severity severity-low">LOW</span> '
        "No configured patterns found",
        unsafe_allow_html=True,
    )
    st.markdown(
        '<span class="severity severity-medium">MEDIUM</span> '
        "Email pattern detected",
        unsafe_allow_html=True,
    )
    st.markdown(
        '<span class="severity severity-high">HIGH</span> '
        "Phone pattern detected",
        unsafe_allow_html=True,
    )

    st.divider()
    st.markdown("### Scan restrictions")
    st.caption("• Text files only (.txt)")
    st.caption("• Maximum 1 MB per file")
    st.caption("• Files processed in memory")
    st.caption("• No automatic blocking or deletion")

# =====================================================
# 9. FILE UPLOAD
# =====================================================
st.markdown(
    '<div class="section-label">01 · FILE INTAKE</div>',
    unsafe_allow_html=True,
)

st.subheader("Upload files for analysis")
st.write(
    "Select fictional text files to identify potential "
    "sensitive-data patterns."
)

uploaded_files = st.file_uploader(
    "Choose .txt files",
    type=["txt"],
    accept_multiple_files=True,
    help="Maximum size: 1 MB per file.",
)

col_button, col_hint = st.columns([1, 3])

with col_button:
    scan_clicked = st.button(
        "🔍 Scan Files",
        type="primary",
        use_container_width=True,
    )

with col_hint:
    st.caption("Scan files and prepare a structured report.")

if scan_clicked:
    if not uploaded_files:
        st.session_state.scan_results = None
        st.warning("Please upload at least one text file.")
    else:
        results = []

        for uploaded_file in uploaded_files:
            if uploaded_file.size > 1_000_000:
                st.warning(
                    f"{uploaded_file.name} skipped: "
                    "file exceeds the 1 MB limit."
                )
                continue

            results.append(
                scan_file(
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                )
            )

        if results:
            st.session_state.scan_results = pd.DataFrame(results)
            st.success(
                f"Scan complete: {len(results)} file(s) processed."
            )
        else:
            st.session_state.scan_results = None
            st.warning("No files were scanned successfully.")

# =====================================================
# 10. DASHBOARD
# =====================================================
if st.session_state.scan_results is not None:
    df = st.session_state.scan_results

    st.divider()
    st.markdown(
        '<div class="section-label">02 · SECURITY OVERVIEW</div>',
        unsafe_allow_html=True,
    )
    st.subheader("Scan dashboard")

    total_files = len(df)
    flagged_files = int((df["Finding Count"] > 0).sum())
    clean_files = int((df["Finding Count"] == 0).sum())

    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">FILES SCANNED</div>
                <div class="metric-value">{total_files}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with metric2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">FILES FLAGGED FOR REVIEW</div>
                <div class="metric-value metric-danger">{flagged_files}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with metric3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">FILES WITH NO FINDINGS</div>
                <div class="metric-value">{clean_files}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    chart_col, summary_col = st.columns(2)

    with chart_col:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown("### Severity distribution")

        severity_counts = (
            df["Suggested Severity"]
            .value_counts()
            .reindex(["High", "Medium", "Low"], fill_value=0)
        )

        st.bar_chart(severity_counts, color="#2dd4bf")
        st.markdown(
            '<div class="muted">Illustrative rules only.</div>',
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with summary_col:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown("### Review summary")
        st.markdown(f"**Files requiring review:** {flagged_files}")
        st.markdown(f"**Files with no configured findings:** {clean_files}")
        st.markdown(
            "**Next step:** Review flagged files according to "
            "the applicable data-handling policy."
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # =================================================
    # 11. FILTER AND RESULTS TABLE
    # =================================================
    st.divider()
    st.markdown(
        '<div class="section-label">03 · FINDINGS</div>',
        unsafe_allow_html=True,
    )
    st.subheader("Scan results")

    selected_severity = st.selectbox(
        "Filter by suggested severity",
        ["All", "High", "Medium", "Low"],
        key="severity_filter",
    )

    if selected_severity == "All":
        filtered_df = df
    else:
        filtered_df = df[
            df["Suggested Severity"] == selected_severity
        ]

    if filtered_df.empty:
        st.info(f"No files found with {selected_severity} severity.")
    else:
        st.dataframe(
            filtered_df[
                [
                    "File Name",
                    "Scan Time",
                    "Findings",
                    "Finding Count",
                    "Suggested Severity",
                    "Status",
                ]
            ],
            use_container_width=True,
            hide_index=True,
        )

    # =================================================
    # 12. INCIDENT DETAILS
    # =================================================
    st.divider()
    st.markdown(
        '<div class="section-label">04 · INVESTIGATION</div>',
        unsafe_allow_html=True,
    )
    st.subheader("📝 Incident details")

    for _, row in filtered_df.iterrows():
        severity = row["Suggested Severity"]
        badge_class = {
            "High": "severity-high",
            "Medium": "severity-medium",
            "Low": "severity-low",
        }.get(severity, "severity-low")

        with st.expander(f"{row['File Name']} | {severity}"):
            st.markdown(
                f'<span class="severity {badge_class}">'
                f'{severity.upper()}</span>',
                unsafe_allow_html=True,
            )
            st.markdown(f"**Findings:** {row['Findings']}")
            st.markdown(
                f"**Incident description:** {row['Incident Description']}"
            )
            st.markdown(
                f"**Recommended action:** {row['Recommended Action']}"
            )
            st.markdown(f"**Status:** {row['Status']}")
            st.markdown(f"**Scan time:** {row['Scan Time']}")

    # =================================================
    # 13. CSV REPORT EXPORT
    # =================================================
    st.divider()
    st.markdown(
        '<div class="section-label">05 · REPORTING</div>',
        unsafe_allow_html=True,
    )
    st.subheader("Export scan report")
    st.write(
        "Download the complete scan results for documentation "
        "or further analysis."
    )

    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download CSV Report",
        data=csv_data,
        file_name="secure_file_scan_report.csv",
        mime="text/csv",
        use_container_width=True,
    )

else:
    st.markdown(
        """
        <div class="panel">
            <h3>Ready to scan</h3>
            <p class="muted">
                Upload fictional .txt files and click Scan Files
                to view the dashboard, review findings, and export
                a CSV report.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =====================================================
# 14. FOOTER
# =====================================================
st.markdown(
    """
    <div class="footer-note">
        SECURE FILE SCANNER · PYTHON · STREAMLIT · PANDAS
        <br><br>
        Educational prototype for defensive security learning.
        Findings require human review.
    </div>
    """,
    unsafe_allow_html=True,
)
