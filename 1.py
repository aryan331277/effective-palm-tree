import pandas as pd
import numpy as np
from datetime import datetime
import re

class DataExtractor:
    def extract_utilisation_certificates()
        uc_data = [
            {
                'work_id': '2103/L37/01212',
                'work_name': 'Construction Of C C Roads Paver Block At Village Bolegaon Sayyad Ankulga',
                'user_dept': 'L - Rural Development Department',
                'aa_amount': 3000000,
                'expenditure': 2766762,
                'balance': 233238,
                'centage_charges': 0,
                'division': 'EE PWD NILANGA',
                'taluka': 'Shirur Anantpal',
                'work_type': 'DEPOSIT',
                'expenditure_details': [
                    {'date': '30/03/2025', 'agency': 'Sujit Narayan Patole', 'bill_amount': 943662, 'centage': 0, 'remark': 'UnavoidableExpenditure'},
                    {'date': '16/06/2025', 'agency': 'Kulswamini MajoorSahkari Sanstha Chata', 'bill_amount': 700000, 'centage': 0, 'remark': 'Road Subgrade Improvement Completed'},
                    {'date': '20/06/2025', 'agency': 'Namdev D Walunj', 'bill_amount': 1123100, 'centage': 0, 'remark': 'UnavoidableExpenditure'}
                ]
            },
            {
                'work_id': '1911/N37/01222',
                'work_name': 'Construction Of Basket Ball Ground At Government Backward Class Girls Residential School',
                'user_dept': 'N - Social Justice And Special Asst.',
                'aa_amount': 700000,
                'expenditure': 692804,
                'balance': 7196,
                'centage_charges': 0,
                'division': 'EE PWD NILANGA',
                'taluka': 'Nilanga',
                'work_type': 'DEPOSIT',
                'expenditure_details': [
                    {'date': '02/11/2023', 'agency': 'Ch.dindayal Majur Sahakari Sansatha Ltd', 'bill_amount': 692804, 'centage': 0, 'remark': 'Misc And Other Work Is In Progress'}
                ]
            },
            {
                'work_id': '2103/L37/01144',
                'work_name': 'Construction Of Paver Block Road At Shivpur',
                'user_dept': 'L - Rural Development Department',
                'aa_amount': 500000,
                'expenditure': 473686,
                'balance': 26314,
                'centage_charges': 0,
                'division': 'EE PWD NILANGA',
                'taluka': 'Shirur Anantpal',
                'work_type': 'DEPOSIT',
                'expenditure_details': [
                    {'date': '02/06/2023', 'agency': 'Kadubai Sidram Magasvargiya', 'bill_amount': 460186, 'centage': 0, 'remark': 'Road Wearing Course Completed'},
                    {'date': '02/06/2023', 'agency': 'M.d.enterprises', 'bill_amount': 13500, 'centage': 0, 'remark': 'UnavoidableExpenditure'}
                ]
            },
            {
                'work_id': '2303/N37/01309',
                'work_name': 'Construction Of Paver Block In Backward Class Wasti At Rapka',
                'user_dept': 'N - Social Justice And Special Asst.',
                'aa_amount': 1000000,
                'expenditure': 919892,
                'balance': 30589,
                'centage_charges': 0,
                'division': 'EE PWD NILANGA',
                'taluka': 'Shirur Anantpal',
                'work_type': 'DEPOSIT',
                'expenditure_details': [
                    {'date': '18/06/2024', 'agency': 'Klleshwar Mss Ltd Togri', 'bill_amount': 919892, 'centage': 0, 'remark': 'Road Subgrade Improvement Completed'}
                ]
            },
            {
                'work_id': '2203/H37/00841',
                'work_name': 'Construction Of Underground Water Tank And Pump Shed At Kasarsirshi',
                'user_dept': 'H - Public Works Department',
                'aa_amount': 600000,
                'expenditure': 544930,
                'balance': 55070,
                'centage_charges': 0,
                'division': 'EE PWD NILANGA',
                'taluka': 'Kasarsirshi',
                'work_type': 'DEPOSIT',
                'expenditure_details': [
                    {'date': '20/10/2022', 'agency': 'Jijamata Majoor SahkariS', 'bill_amount': 544930, 'centage': 0, 'remark': 'MaintenanceWork Completed'}
                ]
            },
            {
                'work_id': '2210/L37/01260',
                'work_name': 'Construction Of Paver Block At Shirur Anantpal',
                'user_dept': 'L - Rural Development Department',
                'aa_amount': 500000,
                'expenditure': 384362,
                'balance': 115638,
                'centage_charges': 0,
                'division': 'EE PWD NILANGA',
                'taluka': 'Shirur Anantpal',
                'work_type': 'DEPOSIT',
                'expenditure_details': [
                    {'date': '12/12/2023', 'agency': 'Malharrao Holkar Majoor Sahkari', 'bill_amount': 384362, 'centage': 0, 'remark': 'Road Wearing Course Completed'}
                ]
            },
            {
                'work_id': '2312/ZD37/01354',
                'work_name': 'Construction Of Sabhagruh For Swami Mandir At Darewadi',
                'user_dept': 'ZD - Tourism And Cultural Affairs',
                'aa_amount': 15000000,
                'expenditure': 14999848,
                'balance': 152,
                'centage_charges': 0,
                'division': 'EE PWD NILANGA',
                'taluka': 'Deoni',
                'work_type': 'DEPOSIT',
                'expenditure_details': [
                    {'date': '09/08/2024', 'agency': 'Vijatratna Infra Constro', 'bill_amount': 4500000, 'centage': 0, 'remark': 'Misc And Other Work Is In Progress'},
                    {'date': '05/02/2025', 'agency': 'Vijatratna Infra Constro', 'bill_amount': 3500000, 'centage': 0, 'remark': 'Building Plingth Is In Progress'},
                    {'date': '14/08/2025', 'agency': 'Vijatratna Infra Constro', 'bill_amount': 6999848, 'centage': 0, 'remark': 'MaintenanceWork Completed'}
                ]
            }
        ]
        return pd.DataFrame(uc_data)
    
    def extract_capital_works():
        capital_data = [
            {
                'work_id': 'JUL/21/021/00190',
                'work_name': 'Improvement Of Lamjana Nilanga Bhalki Road Sh-244 Km 0/00 To 38/200',
                'scheme_code': '50545242',
                'aa_amount': 772800000,
                'expenditure': 3539,
                'balance': 772796461,
                'division': 'EE PWD NILANGA',
                'taluka': 'Nilanga',
                'work_type': 'CAPITAL',
                'contract_amount': 0,
                'date_of_work_order': None,
                'stipulated_completion': None,
                'main_agency': 'Yourself',
                'expenditure_details': [
                    {'date': '22/09/2017', 'agency': 'Yourself', 'bill_amount': 4962549, 'remark': 'SurveyWork Is In Progress'},
                    {'date': '17/03/2018', 'agency': 'Yourself', 'bill_amount': 9904963539, 'remark': 'Unavoidable Expenditure'}
                ]
            },
            {
                'work_id': 'JUL/21/021/00190',
                'work_name': 'Improvement To Lamjana Nilanga Bhalki Road Sh-244 Km.10/00 To 14/00',
                'scheme_code': '50540349',
                'aa_amount': 100000000,
                'expenditure': 68269000,
                'balance': 31731000,
                'division': 'EE PWD NILANGA',
                'taluka': 'Nilanga',
                'work_type': 'CAPITAL',
                'contract_amount': 80868031,
                'date_of_work_order': '08/08/2023',
                'stipulated_completion': '08/08/2024',
                'main_agency': 'M/S S N Khatib And Co',
                'expenditure_details': [
                    {'date': '20/02/2024', 'agency': 'M/S S N Khatib And Co', 'bill_amount': 5100000, 'remark': 'RoadSubgrade Improvement Is In Progress'},
                    {'date': '20/03/2024', 'agency': 'M/S S N Khatib And Co', 'bill_amount': 7200000, 'remark': 'RoadSubgrade Improvement Is In Progress'},
                    {'date': '27/09/2024', 'agency': 'M/S S N Khatib And Co', 'bill_amount': 11000000, 'remark': 'RoadSubgrade Improvement Is In Progress'},
                    {'date': '14/02/2025', 'agency': 'M/S S N Khatib And Co', 'bill_amount': 2469000, 'remark': 'RoadSubgrade Improvement Is In Progress'},
                    {'date': '30/03/2025', 'agency': 'M/S S N Khatib And Co', 'bill_amount': 7500000, 'remark': 'RoadSubgrade Improvement Is In Progress'},
                    {'date': '13/10/2025', 'agency': 'M/S S N Khatib And Co', 'bill_amount': 35000000, 'remark': 'RoadSubgrade Improvement Is In Progress'}
                ]
            },
            {
                'work_id': 'JUL/21/021/00190',
                'work_name': 'Improvement And Construction Road Sh-240 Nitur Shirol Helamb',
                'scheme_code': '30540167',
                'aa_amount': 199100000,
                'expenditure': 199100000,
                'balance': 0,
                'division': 'EE PWD NILANGA',
                'taluka': 'Nilanga',
                'work_type': 'CAPITAL',
                'contract_amount': 147721621,
                'date_of_work_order': '13/10/2023',
                'stipulated_completion': '13/10/2024',
                'main_agency': 'Narendra Ramrao Kale',
                'expenditure_details': [
                    {'date': '28/09/2025', 'agency': 'Narendra Ramrao Kale', 'bill_amount': 7723000, 'remark': 'Road Subgrade Improvement Completed'}
                ]
            },
            {
                'work_id': 'MAR/23/1187/00002',
                'work_name': 'Construction Of New Sub Divisional Office Building At Deoni',
                'scheme_code': '40590977',
                'aa_amount': 20834000,
                'expenditure': 20834000,
                'balance': 0,
                'division': 'EE PWD NILANGA',
                'taluka': 'Deoni',
                'work_type': 'BUILDING',
                'contract_amount': 14508110,
                'date_of_work_order': '03/10/2023',
                'stipulated_completion': '30/06/2024',
                'main_agency': 'Lalit Builders Latur',
                'expenditure_details': [
                    {'date': '04/12/2025', 'agency': 'Lalit Builders Latur', 'bill_amount': 2887529, 'remark': 'Building Slab Level Completed'}
                ]
            }
        ]
        return pd.DataFrame(capital_data)
    
    def extract_tender_data():
        tender_data = [
            {
                'agreement_no': 'B1/66',
                'work_name': 'Repairs to New Court Building at Deoni [Entrance Gate No.1]',
                'contractor': 'Ch.Vishwsamrat Magasvargiya MSS Ltd Latur',
                'agreement_amount': 423506,
                'head_of_account': '2059-4772',
                'sub_division': 'Devni',
                'year': '2025-26'
            },
            {
                'agreement_no': 'B1/67',
                'work_name': 'Repairs to New Court Building at Deoni [Chain Link Fencing]',
                'contractor': 'Ch.Vishwsamrat Magasvargiya MSS Ltd Latur',
                'agreement_amount': 839445,
                'head_of_account': '2059-4772',
                'sub_division': 'Devni',
                'year': '2025-26'
            },
            {
                'agreement_no': 'B1/68',
                'work_name': 'Repairs to New Court Building at Deoni [Witness Box]',
                'contractor': 'Chairman saibaba MSS Ltd Latur',
                'agreement_amount': 839138,
                'head_of_account': '2059-4772',
                'sub_division': 'Devni',
                'year': '2025-26'
            },
            {
                'agreement_no': 'B1/69',
                'work_name': 'Repairs to New Court Building at Deoni [CC Drain]',
                'contractor': 'Chairman saibaba MSS Ltd Latur',
                'agreement_amount': 840306,
                'head_of_account': '2059-4772',
                'sub_division': 'Devni',
                'year': '2025-26'
            },
            {
                'agreement_no': 'B1/70',
                'work_name': 'Repairs to New Court Building at Deoni [Plywood Partition]',
                'contractor': 'Chairman saibaba MSS Ltd Latur',
                'agreement_amount': 837498,
                'head_of_account': '2059-4772',
                'sub_division': 'Devni',
                'year': '2025-26'
            }
        ]
        return pd.DataFrame(tender_data)

class DataCleaner:
    def clean_amount(amount):
        if isinstance(amount, str):
            amount = re.sub(r'[Rs.,\s]', '', amount)
            return float(amount) if amount else 0
        return float(amount) if amount else 0
    
    def normalize_work_id(work_id):
        return str(work_id).strip().upper()
    
    def clean_dataframe(df):
        # Convert amounts
        amount_cols = ['aa_amount', 'expenditure', 'balance', 'centage_charges']
        for col in amount_cols:
            if col in df.columns:
                df[col] = df[col].apply(DataCleaner.clean_amount)
        
        # Normalize IDs
        if 'work_id' in df.columns:
            df['work_id'] = df['work_id'].apply(DataCleaner.normalize_work_id)
        
        # Handle missing values
        df = df.fillna({'balance': 0, 'centage_charges': 0})
        
        return df

class AuditAnalyzer:
    
    def __init__(self):
        self.red_flags = []
        self.current_date = datetime.strptime('13/01/2026', '%d/%m/%Y')
    
    def check_diversion_of_funds(self, row):
        """
        RED FLAG 1: Diversion of Funds
        If "Remark" in Expenditure Details is different from Name of works
        """
        flags = []
        work_name = row['work_name'].lower()
        
        for exp in row.get('expenditure_details', []):
            remark = exp.get('remark', '').lower()
            
            # Check for major mismatches
            if 'paver block' in work_name and 'paver block' not in remark and remark not in ['', 'work completed']:
                if 'unavoidable' in remark or 'other work' in remark:
                    flags.append({
                        'work_id': row['work_id'],
                        'violation_type': 'Diversion of Funds',
                        'severity': 'HIGH',
                        'description': f"Funds diverted - Work: '{work_name[:50]}...' but remark shows: '{remark}'",
                        'amount': exp.get('bill_amount', 0),
                        'agency': exp.get('agency', 'Unknown')
                    })
        
        return flags
    
    def check_wasteful_survey_expenditure(self, row):
        """
        RED FLAG 2: Wasteful Expenditure on Survey Works
        If "Remark" includes Survey Works and RA Bills have Nil payment for other items
        """
        flags = []
        
        for exp in row.get('expenditure_details', []):
            remark = exp.get('remark', '').lower()
            
            if 'survey' in remark and exp.get('bill_amount', 0) > 0:
                # Check if this is the only expenditure
                total_non_survey = sum([e['bill_amount'] for e in row.get('expenditure_details', []) 
                                       if 'survey' not in e.get('remark', '').lower()])
                
                if total_non_survey == 0 or total_non_survey < exp['bill_amount'] * 0.1:
                    flags.append({
                        'work_id': row['work_id'],
                        'violation_type': 'Unfruitful Expenditure on Survey',
                        'severity': 'MEDIUM',
                        'description': f"Survey expenditure of ₹{exp['bill_amount']:,.2f} incurred but no substantial work done",
                        'amount': exp['bill_amount'],
                        'agency': exp.get('agency', 'Unknown')
                    })
        
        return flags
    
    def check_excess_expenditure(self, row):
        """
        RED FLAG 3: Excess Expenditure without Approval
        If "Up-to-date expenditure" is more than AA Amount by 10%
        """
        flags = []
        aa_amount = row.get('aa_amount', 0)
        expenditure = row.get('expenditure', 0)
        
        if aa_amount > 0:
            excess_percentage = ((expenditure - aa_amount) / aa_amount) * 100
            
            if excess_percentage > 10:
                flags.append({
                    'work_id': row['work_id'],
                    'violation_type': 'Excess Expenditure without Approval',
                    'severity': 'HIGH',
                    'description': f"Expenditure ₹{expenditure:,.2f} exceeds AA Amount ₹{aa_amount:,.2f} by {excess_percentage:.2f}%",
                    'amount': expenditure - aa_amount,
                    'agency': 'Multiple'
                })
        
        return flags
    
    def check_non_recovery_centage(self, row):
        """
        RED FLAG 7: Non-recovery of Centage Charges
        If "Centage Amount" is Nil but "Bill Amount" shows some amount
        """
        flags = []
        
        if row.get('work_type') == 'DEPOSIT':
            total_bill_amount = sum([exp.get('bill_amount', 0) for exp in row.get('expenditure_details', [])])
            centage_charges = row.get('centage_charges', 0)
            
            if total_bill_amount > 0 and centage_charges == 0:
                expected_centage = total_bill_amount * 0.05  # 5% centage
                
                flags.append({
                    'work_id': row['work_id'],
                    'violation_type': 'Non-recovery of Centage Charges',
                    'severity': 'MEDIUM',
                    'description': f"Centage charges of ₹{expected_centage:,.2f} (5%) not recovered on bill amount ₹{total_bill_amount:,.2f}",
                    'amount': expected_centage,
                    'agency': 'Multiple'
                })
        
        return flags
    
    def check_unspent_balance(self, row):
        """
        RED FLAG 8: Unspent Balance not returned
        If Balance > ₹1,00,000 and work is completed
        """
        flags = []
        balance = row.get('balance', 0)
        
        # Check if work is completed
        work_completed = False
        for exp in row.get('expenditure_details', []):
            remark = exp.get('remark', '').lower()
            if 'completed' in remark:
                work_completed = True
                break
        
        if work_completed and balance > 100000:
            flags.append({
                'work_id': row['work_id'],
                'violation_type': 'Unspent Balance Not Returned',
                'severity': 'MEDIUM',
                'description': f"Work completed but unspent balance of ₹{balance:,.2f} not returned to user department",
                'amount': balance,
                'agency': 'N/A'
            })
        
        return flags
    
    def check_work_splitting(self, tender_df):
        """
        RED FLAG 6: Splitting of Works
        If similar works with same road/building in continuation awarded to same contractor
        """
        flags = []
        
        # Group by contractor and year
        grouped = tender_df.groupby(['contractor', 'year'])
        
        for (contractor, year), group in grouped:
            # Check for similar works
            court_building_works = group[group['work_name'].str.contains('Court Building', case=False, na=False)]
            
            if len(court_building_works) > 1:
                # Check if all are below ₹10 lakh
                below_limit = court_building_works[court_building_works['agreement_amount'] < 1000000]
                
                if len(below_limit) > 1:
                    total_amount = below_limit['agreement_amount'].sum()
                    work_list = ', '.join(below_limit['agreement_no'].tolist())
                    
                    flags.append({
                        'work_id': work_list,
                        'violation_type': 'Splitting of Works',
                        'severity': 'HIGH',
                        'description': f"Similar works at Court Building Deoni split into {len(below_limit)} contracts (Total: ₹{total_amount:,.2f}) to same contractor '{contractor}' in {year}, each below ₹10 lakh limit",
                        'amount': total_amount,
                        'agency': contractor
                    })
        
        return flags
    
    def check_delay_in_completion(self, row):
        """
        RED FLAG 5: Delay in Completion of Work
        If Stipulated Date of completion is less than Present Date
        """
        flags = []
        
        stipulated = row.get('stipulated_completion')
        if stipulated:
            try:
                stipulated_date = datetime.strptime(stipulated, '%d/%m/%Y')
                
                if stipulated_date < self.current_date:
                    days_delayed = (self.current_date - stipulated_date).days
                    
                    # Check if work is still in progress
                    still_in_progress = False
                    for exp in row.get('expenditure_details', []):
                        remark = exp.get('remark', '').lower()
                        if 'in progress' in remark:
                            still_in_progress = True
                            break
                    
                    if still_in_progress:
                        flags.append({
                            'work_id': row['work_id'],
                            'violation_type': 'Delay in Completion',
                            'severity': 'MEDIUM',
                            'description': f"Work delayed by {days_delayed} days. Stipulated completion: {stipulated}, Current date: {self.current_date.strftime('%d/%m/%Y')}",
                            'amount': 0,
                            'agency': row.get('main_agency', 'Unknown')
                        })
            except:
                pass
        
        return flags
    
    def analyze_all_projects(self, uc_df, capital_df, tender_df):
        """Run all audit checks"""
        all_flags = []
        
        # Analyze Utilisation Certificates
        for _, row in uc_df.iterrows():
            all_flags.extend(self.check_diversion_of_funds(row))
            all_flags.extend(self.check_non_recovery_centage(row))
            all_flags.extend(self.check_unspent_balance(row))
        
        # Analyze Capital Works
        for _, row in capital_df.iterrows():
            all_flags.extend(self.check_wasteful_survey_expenditure(row))
            all_flags.extend(self.check_excess_expenditure(row))
            all_flags.extend(self.check_delay_in_completion(row))
        
        # Analyze Tender/Agreement Data
        splitting_flags = self.check_work_splitting(tender_df)
        all_flags.extend(splitting_flags)
        
        self.red_flags = all_flags
        return all_flags


# ============================================================================
# STEP 6: RESULT AGGREGATION & EDA
# ============================================================================

class AuditEDA:
    """Exploratory Data Analysis on audit results"""
    
    @staticmethod
    def generate_summary(red_flags, uc_df, capital_df):
        """Generate summary statistics"""
        summary = {
            'total_projects_audited': len(uc_df) + len(capital_df),
            'total_red_flags': len(red_flags),
            'total_amount_at_risk': sum([flag['amount'] for flag in red_flags]),
            'high_severity_count': len([f for f in red_flags if f['severity'] == 'HIGH']),
            'medium_severity_count': len([f for f in red_flags if f['severity'] == 'MEDIUM']),
            'low_severity_count': len([f for f in red_flags if f['severity'] == 'LOW']),
        }
        
        # Violation type breakdown
        violation_types = {}
        for flag in red_flags:
            vtype = flag['violation_type']
            if vtype not in violation_types:
                violation_types[vtype] = {'count': 0, 'amount': 0}
            violation_types[vtype]['count'] += 1
            violation_types[vtype]['amount'] += flag['amount']
        
        summary['violation_breakdown'] = violation_types
        
        # Taluka-wise analysis
        taluka_flags = {}
        all_projects = pd.concat([uc_df[['work_id', 'taluka']], 
                                  capital_df[['work_id', 'taluka']]], ignore_index=True)
        
        for flag in red_flags:
            work_id = flag['work_id'].split(',')[0]  # Handle multiple work IDs
            project = all_projects[all_projects['work_id'] == work_id]
            
            if not project.empty:
                taluka = project.iloc[0]['taluka']
                if taluka not in taluka_flags:
                    taluka_flags[taluka] = 0
                taluka_flags[taluka] += 1
        
        summary['taluka_analysis'] = taluka_flags
        
        return summary




    print("\nTotal Red Flags Identified:", len(results['red_flags']))
    print("Amount at Risk: ₹{:,.2f}".format(results['summary']['total_amount_at_risk']))
    print("\n" + "="*80)
