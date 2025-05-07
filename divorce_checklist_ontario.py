# divorce_checklist_ontario.py

"""
Divorce in Ontario: Basic Filing Checklist Script
Author: [Your Name]
Date: [YYYY-MM-DD]

This script provides a basic step-by-step checklist for individuals looking to file for divorce in Ontario, Canada.
This is not legal advice. For official guidance, visit https://www.ontario.ca/page/divorce
"""

def print_divorce_checklist():
    checklist = [
        "✅ You or your spouse must have lived in Ontario for at least 12 months.",
        "✅ You must have valid grounds for divorce (usually separation for 1 year).",
        "✅ Gather documents: Marriage certificate, any agreements (prenup, separation agreement), and ID.",
        "✅ Choose the correct court (Superior Court of Justice).",
        "✅ Fill out and file the following forms:\n"
        "   - Form 8: Application (General or Simple)\n"
        "   - Form 36: Affidavit for Divorce\n"
        "   - Form 25A: Divorce Order",
        "✅ Pay the court filing fee (approximately $632 CAD, as of 2024).",
        "✅ Serve the application to your spouse, unless it's a joint divorce.",
        "✅ Wait for your spouse's response or wait the appropriate period.",
        "✅ Attend court (if required).",
        "✅ Receive the Divorce Order and Certificate of Divorce."
    ]

    print("=== Divorce Filing Checklist: Ontario, Canada ===\n")
    for item in checklist:
        print(item)
    print("\nNote: Always consult a licensed family lawyer or legal aid if unsure.")

if __name__ == "__main__":
    print_divorce_checklist()
