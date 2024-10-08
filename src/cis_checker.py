# cis_checker.py

def check_cis_compliance(gpo_list):
    compliance_report = []
    # Example logic to check GPO against CIS guidelines
    for gpo in gpo_list:
        # Compare each GPO item with CIS benchmarks
        if gpo['policy'] == 'CIS_Policy_Example':
            compliance_report.append({'policy': gpo['policy'], 'compliance': 'Compliant'})
        else:
            compliance_report.append({'policy': gpo['policy'], 'compliance': 'Non-Compliant'})
    
    return compliance_report
