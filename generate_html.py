import json

data_dir = 'data'
output_file = 'index.html'

data_files = {
    'metrics': json.load(open(f'{data_dir}/metrics.json')),
    'conclusions': json.load(open(f'{data_dir}/conclusions.json')),
    'regime': json.load(open(f'{data_dir}/regime_segmentation.json')),
    'stress': json.load(open(f'{data_dir}/market_stress.json')),
    'unemp': json.load(open(f'{data_dir}/unemployment_vs_performance.json')),
    'infl': json.load(open(f'{data_dir}/inflation_vs_returns.json')),
    'gdp': json.load(open(f'{data_dir}/gdp_vs_performance.json')),
    'vol': json.load(open(f'{data_dir}/volume_vs_price.json')),
    'daily_vol': json.load(open(f'{data_dir}/daily_volatility.json')),
    'trends': json.load(open(f'{data_dir}/stock_trends.json'))
}

def make_js_var(name, data):
    return f'const {name} = {json.dumps(data)};'

js_vars = '\n'.join([
    make_js_var('metrics', data_files['metrics']),
    make_js_var('conclusions', data_files['conclusions']),
    make_js_var('regimeData', data_files['regime']),
    make_js_var('stressData', data_files['stress']),
    make_js_var('unempData', data_files['unemp']),
    make_js_var('inflData', data_files['infl']),
    make_js_var('gdpData', data_files['gdp']),
    make_js_var('volData', data_files['vol']),
    make_js_var('dailyVolData', data_files['daily_vol']),
    make_js_var('trendData', data_files['trends'])
])

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Economic Market Analysis Dashboard</title>
    <link rel="stylesheet" href="css/styles.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <header>
        <h1>Economic Market Analysis Dashboard</h1>
        <p class="subtitle">Interactive visualizations of macroeconomic indicators and stock market performance</p>
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
                            <h3>Macro-economic Regime Segmentation</h3>
                            <div class="card-icon">📊</div>
                            <p>Daily market regime classification based on economic indicators</p>
                        </div>
                        <div class="flip-card-back">
                            <canvas id="regimeChart"></canvas>
                        </div>
                    </div>
                </div>

                <div class="flip-card" onclick="flipCard(this)">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <h3>Market Stress Periods</h3>
                            <div class="card-icon">⚠️</div>
                            <p>Identification of high volatility periods</p>
                        </div>
                        <div class="flip-card-back">
                            <canvas id="stressChart"></canvas>
                        </div>
                    </div>
                </div>

                <div class="flip-card" onclick="flipCard(this)">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <h3>Unemployment vs Performance</h3>
                            <div class="card-icon">📉</div>
                            <p>Unemployment rate correlation with market performance</p>
                        </div>
                        <div class="flip-card-back">
                            <canvas id="unemploymentChart"></canvas>
                        </div>
                    </div>
                </div>

                <div class="flip-card" onclick="flipCard(this)">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <h3>Inflation vs Returns</h3>
                            <div class="card-icon">💹</div>
                            <p>Inflation rate impact on stock index returns</p>
                        </div>
                        <div class="flip-card-back">
                            <canvas id="inflationChart"></canvas>
                        </div>
                    </div>
                </div>

                <div class="flip-card" onclick="flipCard(this)">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <h3>GDP Growth vs Performance</h3>
                            <div class="card-icon">📈</div>
                            <p>GDP growth trend vs stock index performance</p>
                        </div>
                        <div class="flip-card-back">
                            <canvas id="gdpChart"></canvas>
                        </div>
                    </div>
                </div>

                <div class="flip-card" onclick="flipCard(this)">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <h3>Volume vs Price Movement</h3>
                            <div class="card-icon">📊</div>
                            <p>Trading volume relationship with price changes</p>
                        </div>
                        <div class="flip-card-back">
                            <canvas id="volumeChart"></canvas>
                        </div>
                    </div>
                </div>

                <div class="flip-card" onclick="flipCard(this)">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <h3>Daily Volatility</h3>
                            <div class="card-icon">📉</div>
                            <p>Volatility trends across all indices</p>
                        </div>
                        <div class="flip-card-back">
                            <canvas id="volatilityChart"></canvas>
                        </div>
                    </div>
                </div>

                <div class="flip-card" onclick="flipCard(this)">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <h3>Stock Price Trends</h3>
                            <div class="card-icon">📈</div>
                            <p>Historical price trends for all indices</p>
                        </div>
                        <div class="flip-card-back">
                            <canvas id="trendsChart"></canvas>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <p>Data Source: <a href="https://www.kaggle.com/datasets" target="_blank">Kaggle Finance & Economics Dataset</a> | <a href="https://github.com/szabijr/adatvizualizacio" target="_blank">GitHub Repository</a> | Analysis Period: 2000-2008</p>
    </footer>

    <script>
{js_vars}

document.addEventListener('DOMContentLoaded', function() {{
    var metricsContainer = document.getElementById('metrics-container');
    metricsContainer.innerHTML = '<div class="metric-card"><strong>Total Records</strong><span>' + metrics.total_records + '</span></div>' +
        '<div class="metric-card"><strong>Date Range</strong><span>' + metrics.start_date + ' - ' + metrics.end_date + '</span></div>' +
        '<div class="metric-card"><strong>Stock Indexes</strong><span>' + metrics.stock_indexes.join(', ') + '</span></div>' +
        '<div class="metric-card"><strong>Avg Daily Return</strong><span>' + metrics.average_daily_return + '%</span></div>' +
        '<div class="metric-card"><strong>Max Unemployment</strong><span>' + metrics.max_unemployment + '%</span></div>' +
        '<div class="metric-card"><strong>Avg Inflation</strong><span>' + metrics.avg_inflation + '%</span></div>';

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
    
    if (chartType === 'regimeChart') {{
        canvas.chartInstance = new Chart(ctx, {{
            type: 'doughnut',
            data: {{
                labels: Object.keys(regimeData),
                datasets: [{{
                    data: Object.values(regimeData),
                    backgroundColor: ['#008080', '#006666', '#009999', '#00aaaa'],
                    borderColor: '#1a1a2e',
                    borderWidth: 2
                }}]
            }},
            options: {{ responsive: true, maintainAspectRatio: false, plugins: {{ legend: {{ position: 'bottom', labels: {{ color: '#e0e0e0', padding: 10 }} }} }} }}
        }});
    }} else if (chartType === 'stressChart') {{
        canvas.chartInstance = new Chart(ctx, {{
            type: 'bar',
            data: {{
                labels: stressData.stress_periods,
                datasets: [{{
                    label: 'Monthly Volatility',
                    data: stressData.volatility_avg,
                    backgroundColor: '#ff6b6b'
                }}]
            }},
            options: {{ responsive: true, maintainAspectRatio: false, scales: {{ y: {{ ticks: {{ color: '#e0e0e0' }} }}, x: {{ ticks: {{ color: '#e0e0e0', maxRotation: 45 }} }} }} }}
        }});
    }} else if (chartType === 'unemploymentChart') {{
        var sampleStep = 100;
        var filtered = unempData.dates.filter(function(_, i) {{ return i % sampleStep === 0; }}).map(function(d, i) {{
            return {{ x: unempData.unemployment[i * sampleStep], y: unempData.close_price[i * sampleStep] }};
        }});
        canvas.chartInstance = new Chart(ctx, {{
            type: 'scatter',
            data: {{ datasets: [{{ label: 'Unemployment vs Price', data: filtered, backgroundColor: '#ff6b6b80' }}] }},
            options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ ticks: {{ color: '#e0e0e0' }} }}, y: {{ ticks: {{ color: '#e0e0e0' }} }} }} }}
        }});
    }} else if (chartType === 'inflationChart') {{
        var sampleStep = 100;
        var filtered = inflData.dates.filter(function(_, i) {{ return i % sampleStep === 0; }}).map(function(d, i) {{
            return {{ x: inflData.inflation[i * sampleStep], y: inflData.daily_returns[i * sampleStep] || 0 }};
        }});
        canvas.chartInstance = new Chart(ctx, {{
            type: 'scatter',
            data: {{ datasets: [{{ label: 'Inflation vs Returns', data: filtered, backgroundColor: '#4ecdc480' }}] }},
            options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ ticks: {{ color: '#e0e0e0' }} }}, y: {{ ticks: {{ color: '#e0e0e0' }} }} }} }}
        }});
    }} else if (chartType === 'gdpChart') {{
        var sampleStep = 100;
        var filtered = gdpData.dates.filter(function(_, i) {{ return i % sampleStep === 0; }}).map(function(d, i) {{
            return {{ x: gdpData.gdp_growth[i * sampleStep], y: gdpData.close_price[i * sampleStep] }};
        }});
        canvas.chartInstance = new Chart(ctx, {{
            type: 'scatter',
            data: {{ datasets: [{{ label: 'GDP vs Price', data: filtered, backgroundColor: '#45b7d180' }}] }},
            options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ ticks: {{ color: '#e0e0e0' }} }}, y: {{ ticks: {{ color: '#e0e0e0' }} }} }} }}
        }});
    }} else if (chartType === 'volumeChart') {{
        var sampleStep = 100;
        var filtered = volData.dates.filter(function(_, i) {{ return i % sampleStep === 0; }}).map(function(d, i) {{
            return {{ x: volData.volume[i * sampleStep], y: volData.close_price[i * sampleStep] }};
        }});
        canvas.chartInstance = new Chart(ctx, {{
            type: 'scatter',
            data: {{ datasets: [{{ label: 'Volume vs Price', data: filtered, backgroundColor: '#96ceb480' }}] }},
            options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ ticks: {{ color: '#e0e0e0' }} }}, y: {{ ticks: {{ color: '#e0e0e0' }} }} }} }}
        }});
    }} else if (chartType === 'volatilityChart') {{
        var sampleStep = 100;
        var filtered = dailyVolData.dates.filter(function(_, i) {{ return i % sampleStep === 0; }}).map(function(d, i) {{
            return {{ x: dailyVolData.dates[i * sampleStep], y: dailyVolData.volatility[i * sampleStep] || 0 }};
        }});
        canvas.chartInstance = new Chart(ctx, {{
            type: 'line',
            data: {{ datasets: [{{ label: 'Volatility', data: filtered, borderColor: '#ffd93d', fill: true }}] }},
            options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ ticks: {{ color: '#e0e0e0' }} }}, y: {{ ticks: {{ color: '#e0e0e0' }} }} }} }}
        }});
    }} else if (chartType === 'trendsChart') {{
        var colors = ['#008080', '#006666', '#00d4d4'];
        var datasets = Object.entries(trendData).map(function(entry, i) {{
            var name = entry[0];
            var d = entry[1];
            return {{
                label: name,
                data: d.dates.map(function(date, j) {{ return {{ x: date, y: d.close[j] }}; }}),
                borderColor: colors[i],
                borderWidth: 2,
                pointRadius: 0,
                fill: false
            }};
        }});
        canvas.chartInstance = new Chart(ctx, {{
            type: 'line',
            data: {{ datasets: datasets }},
            options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ ticks: {{ color: '#e0e0e0' }} }}, y: {{ ticks: {{ color: '#e0e0e0' }} }} }} }}
        }});
    }}
}}
    </script>
</body>
</html>'''

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Generated {output_file}")