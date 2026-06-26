import json
import csv
from collections import defaultdict

csv_file = 'ai_student_impact_dataset.csv'
data_dir = 'data'

records = []
with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        records.append(row)

total_records = len(records)

# 1. Major Distribution
major_counts = defaultdict(int)
for r in records:
    major_counts[r['Major_Category']] += 1
with open(f'{data_dir}/major_distribution.json', 'w') as f:
    json.dump(dict(major_counts), f)

# 2. Policy vs Burnout
policy_burnout = defaultdict(lambda: defaultdict(int))
for r in records:
    policy_burnout[r['Institutional_Policy']][r['Burnout_Risk_Level']] += 1
with open(f'{data_dir}/policy_burnout.json', 'w') as f:
    json.dump(dict(policy_burnout), f)

# 3. GenAI Hours vs GPA Change
genai_gpa = {
    'gen_ai_hours': [float(r['Weekly_GenAI_Hours']) for r in records],
    'gpa_change': [float(r['Post_Semester_GPA']) - float(r['Pre_Semester_GPA']) for r in records]
}
with open(f'{data_dir}/genai_gpa_change.json', 'w') as f:
    json.dump(genai_gpa, f)

# 4. Skill vs Tool Diversity
skill_diversity = {
    'skill': [r['Prompt_Engineering_Skill'] for r in records],
    'diversity': [int(r['Tool_Diversity']) for r in records],
    'avg_diversity_by_skill': {}
}
div_by_skill = defaultdict(list)
for r in records:
    div_by_skill[r['Prompt_Engineering_Skill']].append(int(r['Tool_Diversity']))
skill_diversity['avg_diversity_by_skill'] = {k: sum(v)/len(v) for k, v in div_by_skill.items()}
with open(f'{data_dir}/skill_diversity.json', 'w') as f:
    json.dump(skill_diversity, f)

# 5. Traditional Study Hours vs Post GPA
study_gpa = {
    'study_hours': [float(r['Traditional_Study_Hours']) for r in records],
    'post_gpa': [float(r['Post_Semester_GPA']) for r in records]
}
with open(f'{data_dir}/study_gpa.json', 'w') as f:
    json.dump(study_gpa, f)

# 6. Burnout by Major
burnout_by_major = defaultdict(lambda: defaultdict(int))
for r in records:
    burnout_by_major[r['Major_Category']][r['Burnout_Risk_Level']] += 1
with open(f'{data_dir}/burnout_by_major.json', 'w') as f:
    json.dump(dict(burnout_by_major), f)

# 7. Use Case Distribution
use_case_counts = defaultdict(int)
for r in records:
    use_case_counts[r['Primary_Use_Case']] += 1
with open(f'{data_dir}/use_case_distribution.json', 'w') as f:
    json.dump(dict(use_case_counts), f)

# 8. Skill Retention vs Tool Diversity (colored by Burnout Risk)
retention_diversity = {
    'tool_diversity': [int(r['Tool_Diversity']) for r in records],
    'skill_retention': [float(r['Skill_Retention_Score']) for r in records],
    'burnout': [r['Burnout_Risk_Level'] for r in records]
}
with open(f'{data_dir}/retention_diversity.json', 'w') as f:
    json.dump(retention_diversity, f)

# 9. Skill Retention by Skill Level
retention_by_skill = {
    'skill': [r['Prompt_Engineering_Skill'] for r in records],
    'retention': [float(r['Skill_Retention_Score']) for r in records]
}
with open(f'{data_dir}/retention_by_skill.json', 'w') as f:
    json.dump(retention_by_skill, f)

# Metrics summary
pre_gpa_sum = sum(float(r['Pre_Semester_GPA']) for r in records)
post_gpa_sum = sum(float(r['Post_Semester_GPA']) for r in records)
gen_ai_hours_sum = sum(float(r['Weekly_GenAI_Hours']) for r in records)
anxiety_sum = sum(int(r['Anxiety_Level_During_Exams']) for r in records)

burnout_counts = defaultdict(int)
for r in records:
    burnout_counts[r['Burnout_Risk_Level']] += 1
policy_counts = defaultdict(int)
for r in records:
    policy_counts[r['Institutional_Policy']] += 1

metrics = {
    'total_records': total_records,
    'avg_pre_gpa': round(pre_gpa_sum / total_records, 2),
    'avg_post_gpa': round(post_gpa_sum / total_records, 2),
    'avg_gen_ai_hours': round(gen_ai_hours_sum / total_records, 1),
    'avg_anxiety': round(anxiety_sum / total_records, 1)
}
with open(f'{data_dir}/metrics.json', 'w') as f:
    json.dump(metrics, f)

conclusions = [
    f"Dataset contains {total_records} student records across {len(major_counts)} major categories.",
    f"Average pre-semester GPA: {metrics['avg_pre_gpa']}, post-semester GPA: {metrics['avg_post_gpa']}.",
    f"Students average {metrics['avg_gen_ai_hours']} hours of GenAI usage per week.",
    f"Most common institutional policy: {max(policy_counts, key=policy_counts.get)}.",
    f"Highest burnout risk level: {max(burnout_counts, key=burnout_counts.get)}."
]
with open(f'{data_dir}/conclusions.json', 'w') as f:
    json.dump(conclusions, f)

print("Generated AI student impact visualization data files")