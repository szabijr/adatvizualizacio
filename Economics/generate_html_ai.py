import json

data_dir = 'data'
output_file = 'index_ai.html'

data_files = {
    'metrics': json.load(open(f'{data_dir}/metrics.json')),
    'conclusions': json.load(open(f'{data_dir}/conclusions.json')),
    'major': json.load(open(f'{data_dir}/major_distribution.json')),
    'policy': json.load(open(f'{data_dir}/policy_burnout.json')),
    'genai': json.load(open(f'{data_dir}/genai_gpa_change.json')),
    'skill': json.load(open(f'{data_dir}/skill_diversity.json')),
    'study': json.load(open(f'{data_dir}/study_gpa.json')),
    'burnout': json.load(open(f'{data_dir}/burnout_by_major.json')),
    'use_case': json.load(open(f'{data_dir}/use_case_distribution.json')),
    'retention': json.load(open(f'{data_dir}/retention_by_skill.json')),
    'retention_div': json.load(open(f'{data_dir}/retention_diversity.json'))
}

def make_js_var(name, data):
    return f'const {name} = {json.dumps(data)};'

js_vars = '\n'.join([
    make_js_var('metrics', data_files['metrics']),
    make_js_var('conclusions', data_files['conclusions']),
    make_js_var('majorData', data_files['major']),
    make_js_var('policyData', data_files['policy']),
    make_js_var('genaiData', data_files['genai']),
    make_js_var('skillData', data_files['skill']),
    make_js_var('studyData', data_files['study']),
    make_js_var('burnoutData', data_files['burnout']),
    make_js_var('useCaseData', data_files['use_case']),
    make_js_var('retentionBySkill', data_files['retention']),
    make_js_var('retentionDivData', data_files['retention_div'])
])

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Student Impact Analysis Dashboard</title>
    <link rel="stylesheet" href="css/styles.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <header>
        <h1>AI Student Impact Analysis Dashboard</h1>
        <p class="subtitle">Analyzing the relationship between Generative AI usage and academic outcomes</p>
    </header>

    <main>
        <section id="metrics">
            <h2>Dataset Overview</h2>
            <div class="metrics-grid" id="metrics-container"></div>
        </section>

        <section id="conclusions">
            <h2>Key Insights & Conclusions</h2>
            <div class="conclusions-grid" id="conclusions-container"></div>
        </section>

        <section id="visualizations">
            <h2>Interactive Visualizations</h2>
            <div class="cards-grid">
                <div class="flip-card" onclick="flipCard(this)">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <h3>Major Distribution</h3>
                            <div class="card-icon">🎓</div>
                            <p>Distribution of students across major categories</p>
                        </div>
                        <div class="flip-card-back">
                            <canvas id="majorChart"></canvas>
                        </div>
                    </div>
                </div>

                <div class="flip-card" onclick="flipCard(this)">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <h3>Policy vs Burnout Risk</h3>
                            <div class="card-icon">📊</div>
                            <p>Burnout risk distribution by institutional policy</p>
                        </div>
                        <div class="flip-card-back">
                            <canvas id="policyChart"></canvas>
                        </div>
                    </div>
                </div>

                <div class="flip-card" onclick="flipCard(this)">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <h3>GenAI Hours vs GPA Change</h3>
                            <div class="card-icon">📈</div>
                            <p>Relationship between GenAI usage and GPA improvement</p>
                        </div>
                        <div class="flip-card-back">
                            <canvas id="genaiChart"></canvas>
                        </div>
                    </div>
                </div>

                <div class="flip-card" onclick="flipCard(this)">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <h3>Skill Retention Patterns</h3>
                            <div class="card-icon">📊</div>
                            <p>Skill retention across proficiency levels</p>
                        </div>
                        <div class="flip-card-back">
                            <canvas id="retentionChart"></canvas>
                        </div>
                    </div>
                </div>

                <div class="flip-card" onclick="flipCard(this)">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <h3>Skill vs Tool Diversity</h3>
                            <div class="card-icon">🔧</div>
                            <p>How skill level correlates with tool diversity</p>
                        </div>
                        <div class="flip-card-back">
                            <canvas id="skillChart"></canvas>
                        </div>
                    </div>
                </div>

                <div class="flip-card" onclick="flipCard(this)">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <h3>Study Hours vs GPA</h3>
                            <div class="card-icon">📚</div>
                            <p>Traditional study time vs post-semester GPA</p>
                        </div>
                        <div class="flip-card-back">
                            <canvas id="studyChart"></canvas>
                        </div>
                    </div>
                </div>

                <div class="flip-card" onclick="flipCard(this)">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <h3>Burnout by Major</h3>
                            <div class="card-icon">🔥</div>
                            <p>Burnout risk levels across different majors</p>
                        </div>
                        <div class="flip-card-back">
                            <canvas id="burnoutChart"></canvas>
                        </div>
                    </div>
                </div>

                <div class="flip-card" onclick="flipCard(this)">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <h3>Use Case Distribution</h3>
                            <div class="card-icon">🤖</div>
                            <p>Primary GenAI use cases among students</p>
                        </div>
                        <div class="flip-card-back">
                            <canvas id="useCaseChart"></canvas>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <p>Data Source: <a href="https://www.kaggle.com/datasets" target="_blank">Kaggle AI Student Impact Dataset</a> | <a href="https://github.com/szabijr/adatvizualizacio" target="_blank">GitHub Repository</a></p>
        <p class="abbreviations">GPA: Grade Point Average | GenAI: Generative AI | Pre_GPA: Before semester | Post_GPA: After semester</p>
    </footer>

    <script>
{js_vars}

document.addEventListener('DOMContentLoaded', function() {{
    var metricsContainer = document.getElementById('metrics-container');
    metricsContainer.innerHTML = '<div class="metric-card"><strong>Total Students</strong><span>' + metrics.total_records + '</span></div>' +
        '<div class="metric-card"><strong>Avg Pre-GPA</strong><span>' + metrics.avg_pre_gpa + '</span></div>' +
        '<div class="metric-card"><strong>Avg Post-GPA</strong><span>' + metrics.avg_post_gpa + '</span></div>' +
        '<div class="metric-card"><strong>Avg GenAI Hours</strong><span>' + metrics.avg_gen_ai_hours + '/week</span></div>' +
        '<div class="metric-card"><strong>Avg Anxiety</strong><span>' + metrics.avg_anxiety + '/9</span></div>';

    var conclusionsContainer = document.getElementById('conclusions-container');
    conclusionsContainer.innerHTML = conclusions.map(function(item) {{
        return '<div class="conclusion-card"><p>' + item + '</p></div>';
    }}).join('');
}});

window.flipCard = function(card) {{
    card.classList.toggle('flipped');
    setTimeout(function() {{ initChart(card); }}, 300);
}};

function initChart(card) {{
    var canvas = card.querySelector('canvas');
    if (!canvas || canvas.chartInstance) return;
    
    var chartType = canvas.id;
    var ctx = canvas.getContext('2d');
    if (!ctx) return;
    
    if (chartType === 'majorChart') {{
        canvas.chartInstance = new Chart(ctx, {{
            type: 'doughnut',
            data: {{
                labels: Object.keys(majorData),
                datasets: [{{
                    data: Object.values(majorData),
                    backgroundColor: ['#008080', '#006666', '#00d4d4', '#00aaaa', '#4ecdc4'],
                    borderColor: '#1a1a2e',
                    borderWidth: 2
                }}]
            }},
            options: {{ responsive: true, maintainAspectRatio: false, plugins: {{ legend: {{ position: 'bottom', labels: {{ color: '#e0e0e0', padding: 10 }} }}, title: {{ display: true, text: 'Student Distribution by Major', color: '#e0e0e0' }}}} }}
        }});
    }} else if (chartType === 'policyChart') {{
        var policies = Object.keys(policyData);
        var burnoutLevels = ['Low', 'Medium', 'High'];
        var datasets = burnoutLevels.map(function(level, i) {{
            return {{
                label: level + ' Burnout',
                data: policies.map(function(p) {{ return policyData[p][level] || 0; }}),
                backgroundColor: ['#4ecdc4', '#ffd93d', '#ff6b6b'][i]
            }};
        }});
        canvas.chartInstance = new Chart(ctx, {{
            type: 'bar',
            data: {{ labels: policies, datasets: datasets }},
            options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ ticks: {{ color: '#e0e0e0', maxRotation: 45 }}, title: {{ display: true, text: 'Institutional Policy', color: '#e0e0e0' }} }}, y: {{ ticks: {{ color: '#e0e0e0' }}, title: {{ display: true, text: 'Number of Students', color: '#e0e0e0' }} }} }}, plugins: {{ title: {{ display: true, text: 'Burnout Risk by Institutional Policy', color: '#e0e0e0' }} }} }}
        }});
    }} else if (chartType === 'genaiChart') {{
        var sampleStep = 50;
        var filtered = genaiData.gen_ai_hours.filter(function(_, i) {{ return i % sampleStep === 0; }}).map(function(_, i) {{
            return {{ x: genaiData.gen_ai_hours[i * sampleStep], y: genaiData.gpa_change[i * sampleStep] }};
        }});
        canvas.chartInstance = new Chart(ctx, {{
            type: 'scatter',
            data: {{ datasets: [{{ label: 'GPA Change', data: filtered, backgroundColor: '#45b7d180' }}] }},
            options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ ticks: {{ color: '#e0e0e0' }}, title: {{ display: true, text: 'Weekly GenAI Hours', color: '#e0e0e0' }} }}, y: {{ ticks: {{ color: '#e0e0e0' }}, title: {{ display: true, text: 'GPA Change (Post - Pre)', color: '#e0e0e0' }} }} }}, plugins: {{ title: {{ display: true, text: 'GenAI Usage vs GPA Change', color: '#e0e0e0' }} }} }}
        }});
    }} else if (chartType === 'retentionChart') {{
        var sampleStep = 50;
        var burnoutLevels = ['Low', 'Medium', 'High'];
        var colors = ['#4ecdc4', '#ffd93d', '#ff6b6b'];
        var datasets = burnoutLevels.map(function(level, i) {{
            var filtered = retentionDivData.tool_diversity.filter(function(_, j) {{ return j % sampleStep === 0; }}).map(function(d, j) {{
                var idx = j * sampleStep;
                if (retentionDivData.burnout[idx] === level) {{
                    return {{ x: retentionDivData.tool_diversity[idx], y: retentionDivData.skill_retention[idx] }};
                }}
            }}).filter(function(d) {{ return d !== undefined; }});
            return {{
                label: level + ' Burnout Risk',
                data: filtered,
                backgroundColor: colors[i] + '80'
            }};
        }});
        canvas.chartInstance = new Chart(ctx, {{
            type: 'scatter',
            data: {{ datasets: datasets }},
            options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ ticks: {{ color: '#e0e0e0' }}, title: {{ display: true, text: 'Tool Diversity Index (1-5)', color: '#e0e0e0' }} }}, y: {{ ticks: {{ color: '#e0e0e0' }}, title: {{ display: true, text: 'Skill Retention Score (%)', color: '#e0e0e0' }} }} }}, plugins: {{ title: {{ display: true, text: 'Skill Retention by Tool Diversity & Burnout Risk', color: '#e0e0e0' }} }} }}
        }});
    }} else if (chartType === 'skillChart') {{
        var skills = ['Beginner', 'Intermediate', 'Advanced'];
        var avgData = skills.map(function(s) {{ return skillData.avg_diversity_by_skill[s] || 0; }});
        canvas.chartInstance = new Chart(ctx, {{
            type: 'bar',
            data: {{ labels: skills, datasets: [{{ label: 'Avg Tool Diversity', data: avgData, backgroundColor: '#96ceb4' }}] }},
            options: {{ responsive: true, maintainAspectRatio: false, scales: {{ y: {{ ticks: {{ color: '#e0e0e0' }}, title: {{ display: true, text: 'Avg Tool Diversity Index', color: '#e0e0e0' }} }}, x: {{ ticks: {{ color: '#e0e0e0' }}, title: {{ display: true, text: 'Prompt Engineering Skill Level', color: '#e0e0e0' }} }} }}, plugins: {{ title: {{ display: true, text: 'Tool Diversity vs Skill Level', color: '#e0e0e0' }} }} }}
        }});
    }} else if (chartType === 'studyChart') {{
        var sampleStep = 50;
        var filtered = studyData.study_hours.filter(function(_, i) {{ return i % sampleStep === 0; }}).map(function(_, i) {{
            return {{ x: studyData.study_hours[i * sampleStep], y: studyData.post_gpa[i * sampleStep] }};
        }});
        canvas.chartInstance = new Chart(ctx, {{
            type: 'scatter',
            data: {{ datasets: [{{ label: 'Post GPA', data: filtered, backgroundColor: '#4ecdc480' }}] }},
            options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ ticks: {{ color: '#e0e0e0' }}, title: {{ display: true, text: 'Weekly Study Hours', color: '#e0e0e0' }} }}, y: {{ ticks: {{ color: '#e0e0e0' }}, title: {{ display: true, text: 'Post-Semester GPA', color: '#e0e0e0' }} }} }}, plugins: {{ title: {{ display: true, text: 'Study Hours vs Post-Semester GPA', color: '#e0e0e0' }} }} }}
        }});
    }} else if (chartType === 'burnoutChart') {{
        var majors = Object.keys(burnoutData);
        var burnoutLevels = ['Low', 'Medium', 'High'];
        var datasets = burnoutLevels.map(function(level, i) {{
            return {{
                label: level,
                data: majors.map(function(m) {{ return burnoutData[m][level] || 0; }}),
                backgroundColor: ['#4ecdc4', '#ffd93d', '#ff6b6b'][i]
            }};
        }});
        canvas.chartInstance = new Chart(ctx, {{
            type: 'bar',
            data: {{ labels: majors, datasets: datasets }},
            options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ ticks: {{ color: '#e0e0e0', maxRotation: 45 }}, title: {{ display: true, text: 'Major Category', color: '#e0e0e0' }} }}, y: {{ ticks: {{ color: '#e0e0e0' }}, title: {{ display: true, text: 'Number of Students', color: '#e0e0e0' }} }} }}, plugins: {{ title: {{ display: true, text: 'Burnout Risk by Major', color: '#e0e0e0' }} }} }}
        }});
    }} else if (chartType === 'useCaseChart') {{
        canvas.chartInstance = new Chart(ctx, {{
            type: 'doughnut',
            data: {{
                labels: Object.keys(useCaseData),
                datasets: [{{
                    data: Object.values(useCaseData),
                    backgroundColor: ['#008080', '#00d4d4', '#4ecdc4', '#45b7d1', '#96ceb4'],
                    borderColor: '#1a1a2e',
                    borderWidth: 2
                }}]
            }},
            options: {{ responsive: true, maintainAspectRatio: false, plugins: {{ legend: {{ position: 'bottom', labels: {{ color: '#e0e0e0', padding: 10 }} }}, title: {{ display: true, text: 'GenAI Use Cases Distribution', color: '#e0e0e0' }}}} }}
        }});
    }}
}}
    </script>
</body>
</html>'''

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Generated {output_file}")